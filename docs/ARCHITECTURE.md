# System Architecture

## Core Components

### Function Router
```python
from core.function_router import FunctionRouter

router = FunctionRouter()
router.register(my_function)
```

### Plugin System
```python
from core.plugin_loader import PluginManager

manager = PluginManager()
manager.load_from_path("./plugins")
```

## Integration Patterns

### Database Access
```python
from integrations.sql_database import SQLDatabase

db = SQLDatabase("postgresql://user:pass@localhost/db")
results = await db.execute_query("SELECT * FROM users")
```

### API Consumption
```python
from integrations.api_client import APIClient

client = APIClient("https://api.example.com")
data = await client.call_api("/users", method="GET")
```