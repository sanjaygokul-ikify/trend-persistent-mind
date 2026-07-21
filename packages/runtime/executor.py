from typing import Dict
from logging import Logger
from packages.core.engine import MemoryEngine
from packages.core.types import MemoryModel
from packages.core.exceptions import MemoryException
import logging
import time
import threading

logger: Logger = logging.getLogger(__name__)

class RuntimeExecutor:
    def __init__(self, memory_engine: MemoryEngine):
        self.memory_engine = memory_engine
        self.cache_hits = 0
        self.cache_misses = 0
        self.timeout: int = 5  # Added default timeout
        self.lock = threading.Lock()

    def execute(self, command: str, timeout: int = None, **kwargs) -> Dict:
        if timeout is None:
            timeout = self.timeout
        try:
            start_time = time.time()
            if command == 'store':
                key = kwargs.get('key')
                value = kwargs.get('value')
                if key is None or value is None:
                    logger.error('Missing key or value')
                    raise MemoryException('Missing key or value')
                with self.lock:
                    self.memory_engine.store(key, value)
                return {'result': 'success'}
            elif command == 'retrieve':
                key = kwargs.get('key')
                if key is None:
                    logger.error('Missing key')
                    raise MemoryException('Missing key')
                try:
                    with self.lock:
                        value = self.memory_engine.retrieve(key)
                    return {'result': 'success', 'value': value}
                except MemoryException as e:
                    logger.error(str(e))
                    raise
            elif command == 'delete':
                key = kwargs.get('key')
                if key is None:
                    logger.error('Missing key')
                    raise MemoryException('Missing key')
                with self.lock:
                    self.memory_engine.delete(key)
                return {'result': 'success'}
            elif command == 'update':
                key = kwargs.get('key')
                value = kwargs.get('value')
                if key is None or value is None:
                    logger.error('Missing key or value')
                    raise MemoryException('Missing key or value')
                with self.lock:
                    self.memory_engine.update(key, value)
                return {'result': 'success'}
            else:
                logger.error(f'Unknown command: {command}')
                raise MemoryException(f'Unknown command: {command}')
        except MemoryException as e:
            end_time = time.time()
            with open("metrics.txt", "a") as f:
                f.write(f"Command {command} took {end_time - start_time} seconds to execute.\n")
            logger.error(f'Error executing command: {str(e)}')
            raise MemoryException(f'Error executing command: {str(e)}')
        except Exception as e:
            end_time = time.time()
            with open("metrics.txt", "a") as f:
                f.write(f"Command {command} took {end_time - start_time} seconds to execute.\n")
            logger.error(f'Error executing command: {str(e)}')
            raise