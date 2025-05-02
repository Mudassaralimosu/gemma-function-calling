import pytest
from unittest.mock import AsyncMock
from core.error_handler import error_handler, ExecutionTimeout

@pytest.mark.asyncio
async def test_error_handler_retry_success():
    """Test that retry works when function eventually succeeds"""
    mock_func = AsyncMock()
    mock_func.side_effect = [Exception("Fail"), Exception("Fail"), "Success"]
    
    decorated = error_handler(max_retries=3)(mock_func)
    result = await decorated()
    
    assert result == "Success"
    assert mock_func.call_count == 3

@pytest.mark.asyncio
async def test_error_handler_retry_failure():
    """Test that exception is raised after max retries"""
    mock_func = AsyncMock()
    mock_func.side_effect = Exception("Always fails")
    
    decorated = error_handler(max_retries=2)(mock_func)
    
    with pytest.raises(ExecutionTimeout):
        await decorated()
    
    assert mock_func.call_count == 2