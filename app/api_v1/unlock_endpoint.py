import json
from app.services.frp_manager import FrpManager
from app.services.icloud_bypass import IcloudRemover

async def unlock_device_post(device_type: str = "android", method: str = "frp"):
    """Centralized handler for all unlock requests."""
    
    try:
        # Extract IMEI from JSON body or query params in FastAPI request context
        device_id_str = f"GhostDevice_{device_type}" 
        
        if device_type == "iphone":
            remover = IcloudRemover()
            result = await remover.remove_activation_lock(imei=device_id_str) 
            return result
            
        elif device_type == "android":
            manager = FrpManager()
            result = await manager.bypass_google_frp(ip_pool_size=3, retries=2) 
            
            # If success, optionally trigger remote tracking setup automatically
            service = RemoteCommandService()
            
        return {"success": True, "job_id": 1098}

    except Exception as e:
        print(f"Error in unlock endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Unlock failed: {str(e)}")
