import asyncio
from datetime import datetime

class AsyncLogger:
    @staticmethod
    async def log(level="INFO", message="", context=None):
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Format output string safely to avoid encoding errors with emojis/unicode
        log_line = f"[{timestamp}] [{level.upper()}] {message}" 
        
        if not context: 
            print(log_line, end='\n') # Simple console output for demo
            
        else:
             print(f"{log_line} | Context ID: {context}") 

# Usage Example inside main.py or services:
# await AsyncLogger.log("DEBUG", "Starting FRP bypass sequence...", context="job_1098")
