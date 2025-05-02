import importlib
import inspect
from pathlib import Path
from typing import Dict, Type, Any
from core.schema_validator import FunctionSchemaValidator

class PluginManager:
    def __init__(self):
        self.plugins: Dict[str, Any] = {}
        self.schemas: Dict[str, Dict] = {}

    def load_from_path(self, path: str):
        """Load all Python files in a directory as plugins"""
        plugin_path = Path(path)
        for file in plugin_path.glob('*.py'):
            if file.name.startswith('_'):
                continue
            
            module_name = file.stem
            spec = importlib.util.spec_from_file_location(module_name, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            self._register_functions(module)

    def _register_functions(self, module):
        """Register all callable functions in a module"""
        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj):
                self.plugins[name] = obj
                self.schemas[name] = FunctionSchemaValidator.generate_schema(obj)
                logger.info(f"Registered function: {name}")

    def get_function(self, name: str):
        """Retrieve a registered function"""
        if name not in self.plugins:
            raise FunctionNotFound(f"Function {name} not found in plugins")
        return self.plugins[name]

    def get_schema(self, name: str):
        """Retrieve a function's JSON schema"""
        if name not in self.schemas:
            raise FunctionNotFound(f"Schema for {name} not found")
        return self.schemas[name]