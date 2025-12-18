import json
from datetime import datetime
from random import randint, choice

class SimpleAgent:
    def __init__(self):
        self.name = "ConsoleAgent"
        self.cities = {
            "madrid": {"temp_range": (5, 25), "conditions": ["sunny", "cloudy", "rainy"]},
            "barcelona": {"temp_range": (8, 28), "conditions": ["sunny", "cloudy", "rainy"]},
            "paris": {"temp_range": (3, 22), "conditions": ["sunny", "cloudy", "rainy", "snowy"]},
            "london": {"temp_range": (2, 20), "conditions": ["cloudy", "rainy", "sunny"]},
        }
    
    def get_weather(self, city):
        """Simulate weather for a given city"""
        city_lower = city.lower()
        if city_lower not in self.cities:
            return f"Sorry, I don't have data for {city}."
        
        city_data = self.cities[city_lower]
        temp = randint(city_data["temp_range"][0], city_data["temp_range"][1])
        condition = choice(city_data["conditions"])
        
        return f"Weather in {city.title()}: {temp}°C, {condition}"
    
    def answer_question(self, question):
        """Answer basic questions"""
        question_lower = question.lower()
        
        if "weather" in question_lower or "temperature" in question_lower:
            for city in self.cities:
                if city in question_lower:
                    return self.get_weather(city)
            return "Which city would you like to know the weather for?"
        
        if "name" in question_lower:
            return f"I'm {self.name}, your assistant."
        
        if "time" in question_lower:
            return f"Current time: {datetime.now().strftime('%H:%M:%S')}"
        
        return "I can help you with weather information and basic questions. Ask me about the weather in any city!"
    
    def run(self):
        """Run the agent in console mode"""
        print(f"Welcome! I'm {self.name}. Type 'exit' to quit.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == "exit":
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            response = self.answer_question(user_input)
            print(f"Agent: {response}\n")


if __name__ == "__main__":
    agent = SimpleAgent()
    agent.run()