from typing import Optional, Dict, Any
import logging
from functools import wraps

logger = logging.getLogger(__name__)

class FunctionCallError(Exception):
    """Base exception for function calling errors"""
    def __init__(self, message: str, metadata: Optional[Dict] = None):
        self.metadata = metadata or {}
        super().__init__(message)

class InvalidFunctionCall(FunctionCallError):
    """Raised when function call doesn't match schema"""

class FunctionNotFound(FunctionCallError):
    """Raised when requested function isn't registered"""

class ExecutionTimeout(FunctionCallError):
    """Raised when function execution times out"""

def error_handler(max_retries: int = 3):
    """Decorator to add retry logic to function execution"""
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    logger.warning(f"Attempt {attempt} failed: {str(e)}")
                    if attempt == max_retries:
                        break
            raise ExecutionTimeout(
                f"Failed after {max_retries} attempts",
                {"last_error": str(last_error)}
            ) from last_error
        return wrapper
    return decorator