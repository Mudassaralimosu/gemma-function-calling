import time
from statistics import mean
from typing import List, Dict

class FunctionCallBenchmark:
    def __init__(self, router: FunctionRouter):
        self.router = router

    async def run_test(self, test_cases: List[Dict]) -> Dict[str, float]:
        results = {}
        for case in test_cases:
            latencies = []
            for _ in range(10):  # Run 10 trials
                start = time.perf_counter()
                await self.router.execute(case)
                latencies.append(time.perf_counter() - start)
            results[case["name"]] = mean(latencies)
        
        return {
            "average_latency": mean(results.values()),
            "function_breakdown": results
        }