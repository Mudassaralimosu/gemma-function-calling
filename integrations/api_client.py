import httpx
from typing import Dict, Any, Optional
from core.error_handler import error_handler

class APIClient:
    def __init__(self, base_url: str, timeout: int = 30):
        self.client = httpx.AsyncClient(base_url=base_url, timeout=timeout)

    @error_handler()
    async def call_api(
        self,
        endpoint: str,
        method: str = "GET",
        params: Optional[Dict] = None,
        body: Optional[Dict] = None,
        headers: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """Generic API caller with error handling"""
        response = await self.client.request(
            method,
            endpoint,
            params=params,
            json=body,
            headers=headers
        )
        response.raise_for_status()
        return response.json()

    async def get_swagger_schema(self) -> Dict:
        """Fetch API schema from Swagger/OpenAPI endpoint"""
        return await self.call_api("/swagger.json")

    async def generate_function_from_endpoint(self, endpoint: str) -> callable:
        """Create a callable function from an API endpoint"""
        schema = await self.get_swagger_schema()
        # Implementation would parse OpenAPI spec and create functions
        pass