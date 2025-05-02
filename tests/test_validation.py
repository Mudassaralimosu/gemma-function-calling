import pytest
from core.schema_validator import FunctionSchemaValidator

def test_valid_function_call(sample_schema):
    valid_call = {
        "name": "test_function",
        "arguments": {"x": 5}
    }
    assert FunctionSchemaValidator.validate_call(valid_call, sample_schema)

def test_missing_required_param(sample_schema):
    invalid_call = {
        "name": "test_function",
        "arguments": {}
    }
    assert not FunctionSchemaValidator.validate_call(invalid_call, sample_schema)

def test_wrong_param_type(sample_schema):
    invalid_call = {
        "name": "test_function",
        "arguments": {"x": "string"}
    }
    assert not FunctionSchemaValidator.validate_call(invalid_call, sample_schema)