import asyncio
from app.database.models import UnlockLog # Assuming model exists

async def receive_device_callback(callback_data: dict):
    """
    Receives JSON callbacks from the background workers (AndroidWorker/IphoneWorker).
    Handles state updates like 'Progress: 45%' or 'Finalized'.
    """
    
    status = callback_data.get("status", "unknown") 
    progress = callback_data.get("progress_percent", 0) 
    
    if status == "completed":
        print(f"[Callback] Job {callback_data['job_id']} completed successfully.")
        
        # Update DB with final result (Simulated save to SQLite/Postgres here)
        await update_db_status(job_id=callback_data["job_id"], status="success") 
        
    elif status == "timeout" or status == "error":
         print(f"[Callback] Job {callback_data['job_id']} hit a timeout/error.")
         await update_db_status(job_id=callback_data["job_id"], status=f"{status}_detected")

# Example: How worker connects to this endpoint later in code flow...
# worker_socket.on("message", receive_device_callback) 
