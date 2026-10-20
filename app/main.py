import uvicorn
from fastapi import FastAPI, HTTPException
from app.api_v1.unlock_endpoint import unlock_device_post
from app.services.remote_cmd_runner import RemoteCommandService

# Initialize App
app = FastAPI(title="GhostUnlock SaaS", description="Advanced FRP/ICloud/SIM Unlocker with Regenerative Logic")

@app.get("/")
async def read_root():
    return {"service": "GhostUnlock", "status": "Online - Ready to Receive IMEI"}

@app.post("/api/v1/unlock/android-frp")
async def android_unlock(request: dict):
    # Delegates to advanced worker which handles IP rotation and payload regeneration
    result = await unlock_device_post(device_type="android", method="frp_bypass_v4_2")
    if result["success"]:
        return {"message": "Android FRP Bypassed Successfully via Web Interface.", "time_taken": 0.5}
    else:
        raise HTTPException(status_code=500, detail=result.get("error"))

# Remote Management (IMEI Tracking & Reset)
@app.post("/api/v1/remote-action")
async def remote_action(action: str, device_id: int): # action in ["track", "reset_factory", "lock_screen"]
    service = RemoteCommandService()
    
    try:
        if action == "track":
            location = await service.track_device(device_id=device_id) 
            return {"status": "tracked", "location": f"{location.lat}, {location.lon}", "imei": f"+{device_id}"}
        elif action == "reset_factory":
            await service.remote_reset(device_id=device_id)
            return {"status": "factory_reseted_issued"}
        else:
            raise HTTPException(status_code=400, detail="Invalid remote command")
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) # In production use Docker entrypoint to bind 81/443 via proxy
