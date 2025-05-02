import httpx
from dataclasses import dataclass

@dataclass
class SearchResult:
    title: str
    url: str
    snippet: str

class WebSearchIntegration:
    def __init__(self, api_key: str):
        self.session = httpx.AsyncClient()
        self.api_key = api_key

    @FunctionSchemaValidator.register_schema(
        description="Search the web for current information",
        parameters={
            "query": {"type": "string"},
            "num_results": {"type": "integer", "default": 3}
        }
    )
    async def web_search(self, query: str, num_results: int = 3) -> List[SearchResult]:
        """Perform a live web search"""
        results = await self._call_search_api(query, num_results)
        return [
            SearchResult(
                title=r.get("title"),
                url=r.get("link"),
                snippet=r.get("snippet")
            )
            for r in results
        ]