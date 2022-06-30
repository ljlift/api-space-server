from typing import Any
from fastapi import APIRouter, Depends
from app import schema, crud, model
import tempfile
import os
from app.api.deps import get_db
from sqlalchemy.orm import Session

import yaml
import json

router = APIRouter(prefix="/validation")


@router.post("", response_model=schema.validation.ValidationResponse)
def validate(*, db: Session = Depends(get_db), validation_in: schema.validation.ValidationPost) -> Any:
    result = "Spec file content is valid"
    spec_file = None
    ruleset_file = None
    try:
        spec_file = tempfile.mktemp(suffix=".json", prefix="spec")
        with open(spec_file, "w") as fd:
            json.dump(validation_in.spec, fd)
        
        microAPI_model = crud.microapi.get_by_uri(db, uri=validation_in.uri) # type: model.MicroAPI
        space_model = crud.space.get_by_filter(db, name=microAPI_model.space_name) # type: model.Space
        ruleset = space_model.ruleset
        ruleset_file = tempfile.mktemp(suffix=".yaml", prefix="ruleset")
        with open(ruleset_file, "w") as fd:
            yaml.dump(ruleset, fd)
        
        with os.popen(
            f"spectral lint {spec_file} --ruleset {ruleset_file}"
        ) as fp:
            bf = fp._stream.buffer.read() # type: bytes
            try:
                result = bf.decode().strip()
            except UnicodeDecodeError:
                result = bf.decode("GBK").strip()

            if "No results with a severity of 'error' found!" not in result:
                result = "\n".join(result.split("\n")[1:])
        
    finally:
        for f in [spec_file, ruleset_file]:
            if f is not None and os.path.exists(f):
                os.remove(f)

    return {"result": result}

