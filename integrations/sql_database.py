from typing import List, Dict, Optional
import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.sql import select, text
from core.error_handler import error_handler

class SQLDatabase:
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)

    @error_handler(max_retries=3)
    async def execute_query(self, query: str) -> List[Dict]:
        """Execute raw SQL query and return results"""
        with self.engine.connect() as conn:
            result = conn.execute(text(query))
            return [dict(row) for row in result]

    async def get_table_schema(self, table_name: str) -> Dict:
        """Get schema information for a table"""
        if table_name not in self.metadata.tables:
            raise ValueError(f"Table {table_name} not found")
        
        table = self.metadata.tables[table_name]
        return {
            "columns": [
                {"name": col.name, "type": str(col.type)}
                for col in table.columns
            ],
            "primary_key": [key.name for key in table.primary_key]
        }

    async def smart_query(self, natural_language: str) -> List[Dict]:
        """Convert natural language to SQL using Gemma"""
        # This would integrate with Gemma to generate SQL
        # Implementation would use the function calling system
        pass