import pytest
from core.function_router import FunctionRouter
from core.plugin_loader import PluginManager

@pytest.fixture
def function_router():
    """Provides a clean FunctionRouter instance for each test"""
    return FunctionRouter()

@pytest.fixture
def plugin_manager(tmp_path):
    """Provides a PluginManager with test plugins"""
    manager = PluginManager()
    # Create a temporary test plugin
    test_plugin = tmp_path / "test_plugin.py"
    test_plugin.write_text("""
def test_function(x: int) -> int:
    return x * 2
""")
    manager.load_from_path(str(tmp_path))
    return manager

@pytest.fixture
def sample_schema():
    """Example function schema for validation tests"""
    return {
        "name": "test_function",
        "description": "Test function",
        "parameters": {
            "type": "object",
            "properties": {
                "x": {"type": "integer"}
            },
            "required": ["x"]
        }
    }