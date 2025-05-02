from jsonschema import validate
import inspect
from typing import Dict, Any

class FunctionSchemaValidator:
    @classmethod
    def generate_schema(cls, func: callable) -> dict[str, any]:
        """Generate JSON schema from function signature"""
        sig = inspect.signature(func)
        schema = {
            "name": func.__name__,
            "description": func.__doc__ or "",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
        
        for name, param in sig.parameters.items():
            param_schema = {
                "type": "string"  # Default type
            }
            if param.annotation != inspect.Parameter.empty:
                param_schema["type"] = param.annotation.__name__
            
            schema["parameters"]["properties"][name] = param_schema
            if param.default == inspect.Parameter.empty:
                schema["parameters"]["required"].append(name)
                
        return schema