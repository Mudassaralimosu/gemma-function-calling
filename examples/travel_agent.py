from datetime import datetime, timedelta
from typing import List, Dict, Optional
from core.function_router import FunctionRouter
from core.error_handler import error_handler
import random
import json

class TravelAgent:

    def __init__(self):
        self.router = FunctionRouter()
        self.user_preferences = {}
        self._register_functions()

    def _register_functions(self):
        """Register all travel-related functions"""
        self.router.register(self.search_flights)
        self.router.register(self.search_hotels)
        self.router.register(self.get_weather_forecast)
        self.router.register(self.get_local_attractions)
        self.router.register(self.book_ticket)
        self.router.register(self.save_itinerary)

    @error_handler()
    async def search_flights(self, 
                          origin: str, 
                          destination: str, 
                          date: str,
                          preferences: Optional[Dict] = None) -> List[Dict]:
        """
        Search available flights (mock implementation)
        
        Args:
            origin: Departure city code
            destination: Arrival city code
            date: Departure date (YYYY-MM-DD)
            preferences: Optional filters like:
                {"max_price": 500, "airlines": ["Delta"]}
        """
        # In real implementation, this would call a flight API
        airlines = ["Delta", "United", "American", "Southwest"]
        flights = []
        for i in range(3):
            flights.append({
                "airline": random.choice(airlines),
                "price": random.randint(200, 800),
                "departure": f"{date}T{random.randint(6,20)}:00:00",
                "duration": f"{random.randint(1,6)}h {random.randint(0,59)}m"
            })
        return sorted(flights, key=lambda x: x["price"])


    async def search_hotels(self, 
                          location: str, 
                          check_in: str,
                          check_out: str,
                          guests: int = 1) -> List[Dict]:
        """Search hotels (mock implementation)"""
        hotels = []
        for i in range(3):
            hotels.append({
                "name": f"{random.choice(['Grand', 'Plaza', 'Sunset'])} Hotel",
                "price": random.randint(80, 300),
                "rating": round(random.uniform(3.5, 5), 1),
                "amenities": random.sample(["pool", "gym", "wifi", "breakfast"], 2)
            })
        return sorted(hotels, key=lambda x: -x["rating"])


    async def get_weather_forecast(self, 
                                 location: str, 
                                 date: str) -> Dict:
        """Get weather forecast (mock implementation)"""
        conditions = ["sunny", "rainy", "cloudy", "snowy"]
        return {
            "date": date,
            "condition": random.choice(conditions),
            "high": random.randint(60, 90),
            "low": random.randint(30, 60)
        }


    async def get_local_attractions(self, 
                                  location: str, 
                                  interests: List[str]) -> List[Dict]:
        """Get recommended attractions (mock implementation)"""
        attractions = []
        types = {
            "cultural": ["Museum", "Art Gallery", "Historic Site"],
            "outdoor": ["Park", "Hiking Trail", "Beach"],
            "food": ["Restaurant", "Food Tour", "Market"]
        }
        
        for interest in interests[:3]:
            if interest in types:
                name = f"{random.choice(types[interest])} {random.choice(['of', 'at'])} {location}"
                attractions.append({
                    "name": name,
                    "type": interest,
                    "price": "$" if random.random() > 0.5 else "Free"
                })
        return attractions


    async def book_ticket(self, 
                        item_type: str, 
                        item_id: str, 
                        user_details: Dict) -> Dict:
        """Mock booking function"""
        return {
            "confirmation": f"{item_type.upper()}-{random.randint(1000,9999)}",
            "status": "confirmed",
            "price": random.randint(50, 500)
        }


    async def save_itinerary(self, 
                           bookings: List[Dict], 
                           file_path: str) -> str:
        """Save travel plan to file"""
        with open(file_path, 'w') as f:
            json.dump(bookings, f, indent=2)
        return f"Itinerary saved to {file_path}"


async def plan_trip():
    agent = TravelAgent()
    
    # Example trip planning flow
    print("Searching flights from NYC to London...")
    flights = await agent.search_flights(
        origin="JFK", 
        destination="LHR", 
        date="2024-07-15"
    )
    print(json.dumps(flights, indent=2))
    
    print("\nSearching hotels in London...")
    hotels = await agent.search_hotels(
        location="London",
        check_in="2024-07-15",
        check_out="2024-07-20"
    )
    print(json.dumps(hotels, indent=2))
    
    print("\nGetting weather forecast...")
    weather = await agent.get_weather_forecast(
        location="London",
        date="2024-07-16"
    )
    print(json.dumps(weather, indent=2))
    
    print("\nFinding attractions...")
    attractions = await agent.get_local_attractions(
        location="London",
        interests=["cultural", "food"]
    )
    print(json.dumps(attractions, indent=2))
    
    print("\nBooking selections...")
    booking = await agent.book_ticket(
        item_type="hotel",
        item_id="hotel-123",
        user_details={"name": "Mudassar Ali Ansari"}
    )
    print(json.dumps(booking, indent=2))
    
    print("\nSaving itinerary...")
    print(await agent.save_itinerary(
        bookings=[flights[0], hotels[0], booking],
        file_path="london_trip.json"
    ))


if __name__ == "__main__":
    import asyncio
    asyncio.run(plan_trip())