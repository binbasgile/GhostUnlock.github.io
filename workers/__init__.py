from .android_worker import AndroidWorker as AndroidWorkerClass

# Helper function for spawning workers based on load balancing config in assets/config.yaml
def start_workers(count: int):
    """Spawns 'count' number of worker processes/threads."""
    import multiprocessing # Or asyncio.create_task() for async tasks
    
    print(f"[Workers] Spawning {count} instances...") 
    return [AndroidWorker(i) for i in range(count)]
