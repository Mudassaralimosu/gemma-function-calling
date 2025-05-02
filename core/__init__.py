"""
Core functionality for Gemma function calling system.

Exposes the main interfaces for function registration, validation, and execution.
"""

from .function_router import FunctionRouter
from .schema_validator import FunctionSchemaValidator
from .error_handler import (
    FunctionCallError,
    InvalidFunctionCall,
    FunctionNotFound,
    ExecutionTimeout,
    error_handler
)
from .plugin_loader import PluginManager

__all__ = [
    'FunctionRouter',
    'FunctionSchemaValidator',
    'FunctionCallError',
    'InvalidFunctionCall',
    'FunctionNotFound',
    'ExecutionTimeout',
    'error_handler',
    'PluginManager'
]

__version__ = '0.1.0'