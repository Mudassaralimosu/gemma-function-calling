# Gemma Function Calling Framework

An advanced function calling implementation for Gemma models, featuring production-ready capabilities for real-world applications. This project demonstrates:

✅ **Schema validation** with automatic OpenAPI spec generation  
✅ **Multi-turn conversations** with context preservation  
✅ **Dynamic plugin system** for extensibility  
✅ **Real-world integrations** (APIs, databases, web search)  
✅ **Benchmarking suite** for performance metrics  

## 🌟 Featured Examples

### 1. Smart Travel Agent
`examples/travel_agent.py`  
A complete trip planning assistant that:
- Searches flights/hotels  
- Checks weather forecasts  
- Recommends local attractions  
- Books reservations  
- Generates printable itineraries  

**Try it:**
```bash
python examples/travel_agent.py

### 2. Data Analysis Assistant

examples/data_analyst.py
An AI-powered data analyst that:

Loads CSV/Excel files
Filters and analyzes datasets
Generates statistics
Creates visualizations
Exports results


**Try it:**
```bash
python examples/data_analyst.py

## Architecture

gemma-function-calling/
├── core/               # Framework engine
│   ├── function_router.py    # Intelligent function dispatching
│   ├── schema_validator.py   # OpenAPI-compatible validation
│   └── error_handler.py      # Automatic retry logic
├── integrations/       # Real-world adapters
│   ├── web_search.py   # Live information retrieval
│   └── sql_database.py # ORM-style queries
├── examples/           # Production-grade implementations
├── benchmarks/         # Performance tracking
└── tests/              # Comprehensive test suite


🚀 Quick Start
Install dependencies:

bash
pip install -r requirements.txt
pip install -e .  # Install in editable mode
Run examples:

bash
# Travel planning assistant
python examples/travel_agent.py

# Data analysis tool
python examples/data_analyst.py


Extend with your own functions:


from core import FunctionRouter
router = FunctionRouter()

@router.register
async def your_function(param: str):
    """Your function's docstring becomes the API description"""
    return {"result": param.upper()}
