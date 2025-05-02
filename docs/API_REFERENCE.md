# API Reference

## Core Modules

### `FunctionRouter`
```python
class FunctionRouter:
    def register(self, func: callable) -> None:
        """Register a callable function"""

    async def execute(self, call: dict) -> Any:
        """Execute a function call"""
```

### `PluginManager`
```python
class PluginManager:
    def load_from_path(self, path: str) -> None:
        """Load plugins from directory"""

    def get_function(self, name: str) -> callable:
        """Get registered function"""
```

## Decorators

### `@error_handler`
```python
@error_handler(max_retries=3)
async def risky_operation():
    """Example of error-handled function"""
```

## Common Exceptions
- `FunctionCallError`: Base exception
- `InvalidFunctionCall`: Schema validation failed
- `FunctionNotFound`: Requested function not registered