import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from core.function_router import FunctionRouter
from core.error_handler import error_handler
from typing import Dict, List, Optional
import json

class DataAnalyst:
    def __init__(self):
        self.router = FunctionRouter()
        self.df = None  # Current DataFrame
        self._register_functions()

    def _register_functions(self):
        """Register all available data analysis functions"""
        self.router.register(self.load_dataset)
        self.router.register(self.show_columns)
        self.router.register(self.describe_data)
        self.router.register(self.filter_data)
        self.router.register(self.generate_plot)
        self.router.register(self.save_results)

    @error_handler()
    async def load_dataset(self, file_path: str) -> str:
        """
        Load dataset from file (CSV/Excel)
        
        Args:
            file_path: Path to data file
        Returns:
            Status message with row count
        """
        if file_path.endswith('.csv'):
            self.df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            self.df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
        return f"Dataset loaded with {len(self.df)} rows and {len(self.df.columns)} columns"

    async def show_columns(self) -> List[Dict]:
        """Return list of columns with their data types"""
        if self.df is None:
            raise ValueError("No dataset loaded")
        return [{"name": col, "type": str(dtype)} 
                for col, dtype in self.df.dtypes.items()]

    async def describe_data(self, column: Optional[str] = None) -> Dict:
        """
        Generate statistics for a column or entire dataset
        
        Args:
            column: Optional specific column to analyze
        """
        if self.df is None:
            raise ValueError("No dataset loaded")
        
        if column:
            return self.df[column].describe().to_dict()
        return self.df.describe().to_dict()

    async def filter_data(self, conditions: List[Dict]) -> str:
        """
        Filter data based on conditions
        
        Args:
            conditions: List of conditions like:
                [{"column": "age", "operator": ">", "value": 30}]
        """
        if self.df is None:
            raise ValueError("No dataset loaded")
            
        for cond in conditions:
            col = cond["column"]
            op = cond["operator"]
            val = cond["value"]
            
            if op == ">":
                self.df = self.df[self.df[col] > val]
            elif op == "<":
                self.df = self.df[self.df[col] < val]
            elif op == "==":
                self.df = self.df[self.df[col] == val]
                
        return f"Filtered to {len(self.df)} rows"

    async def generate_plot(self, config: Dict) -> Dict:
        """
        Generate visualization data
        
        Args:
            config: Plot configuration like:
                {
                    "type": "histogram",
                    "column": "price",
                    "bins": 10
                }
        Returns:
            Plot data that can be rendered by frontend
        """
        plot_type = config["type"]
        if plot_type == "histogram":
            counts, bins = np.histogram(self.df[config["column"]].dropna(), 
                                     bins=config.get("bins", 10))
            return {
                "type": "histogram",
                "data": {
                    "counts": counts.tolist(),
                    "bins": bins.tolist()
                }
            }
        elif plot_type == "scatter":
            return {
                "type": "scatter",
                "data": {
                    "x": self.df[config["x"]].tolist(),
                    "y": self.df[config["y"]].tolist()
                }
            }

    async def save_results(self, output_path: str) -> str:
        """Save current dataframe to CSV"""
        self.df.to_csv(output_path, index=False)
        return f"Results saved to {output_path}"

async def main():
    analyst = DataAnalyst()
    
    # Example interaction flow
    print(await analyst.load_dataset("sales_data.csv"))
    print(json.dumps(await analyst.show_columns(), indent=2))
    print(json.dumps(await analyst.describe_data("revenue"), indent=2))
    
    await analyst.filter_data([
        {"column": "revenue", "operator": ">", "value": 1000}
    ])
    
    plot_data = await analyst.generate_plot({
        "type": "histogram",
        "column": "revenue"
    })
    print(json.dumps(plot_data, indent=2))
    
    print(await analyst.save_results("filtered_results.csv"))

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())