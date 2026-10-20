__version__ = "1.0.4-gheost" # Version identifier
VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_PATCH = 4

# Optional: Quick import aliases for internal modules
from app.utils.logger import logger as root_logger

root_logger.info("GhostUnlock SaaS Core Initialized.")
