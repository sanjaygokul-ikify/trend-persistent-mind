from packages.core import MemoryEngine
from packages.utils import logging

logger = logging.getLogger(__name__)

class Orchestrator:
    def __init__(self, memory_engine: MemoryEngine):
        self.memory_engine = memory_engine
        self.logger = logger

    def start(self) -> None:
        self.logger.info('Orchestrator started')

    def stop(self) -> None:
        self.logger.info('Orchestrator stopped')