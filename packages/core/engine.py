import logging
from typing import List, Dict
from .types import MemoryModel
from .exceptions import MemoryException
import threading

logger = logging.getLogger(__name__)

class MemoryEngine:
    def __init__(self, memory_model: MemoryModel):
        self.memory_model = memory_model
        self.memory_store = {}
        self.lock = threading.Lock()
        self.cache = {}
        self.cache_size = 100
        self.hits = 0
        self.misses = 0

    def store(self, key: str, value: str) -> None:
        with self.lock:
            try:
                self.memory_store[key] = value
                if len(self.cache) < self.cache_size:
                    self.cache[key] = value
                logger.info(f'Stored key {key} with value {value}')
            except Exception as e:
                logger.error(f'Error storing key {key}: {str(e)}')
                raise MemoryException(f'Error storing key {key}: {str(e)}')

    def retrieve(self, key: str) -> str:
        with self.lock:
            try:
                if key in self.cache:
                    self.hits += 1
                    return self.cache[key]
                elif key in self.memory_store:
                    self.misses += 1
                    value = self.memory_store[key]
                    if len(self.cache) < self.cache_size:
                        self.cache[key] = value
                    return value
                else:
                    logger.error(f'Key {key} not found')
                    raise MemoryException(f'Key {key} not found')
            except Exception as e:
                logger.error(f'Error retrieving key {key}: {str(e)}')
                raise MemoryException(f'Error retrieving key {key}: {str(e)}')

    def delete(self, key: str) -> None:
        with self.lock:
            try:
                if key in self.memory_store:
                    del self.memory_store[key]
                    if key in self.cache:
                        del self.cache[key]
                    logger.info(f'Deleted key {key}')
                else:
                    logger.error(f'Key {key} not found')
                    raise MemoryException(f'Key {key} not found')
            except Exception as e:
                logger.error(f'Error deleting key {key}: {str(e)}')
                raise MemoryException(f'Error deleting key {key}: {str(e)}')

    def update(self, key: str, value: str) -> None:
        with self.lock:
            try:
                if key in self.memory_store:
                    self.memory_store[key] = value
                    if key in self.cache:
                        self.cache[key] = value
                    logger.info(f'Updated key {key} with value {value}')
                else:
                    logger.error(f'Key {key} not found')
                    raise MemoryException(f'Key {key} not found')
            except Exception as e:
                logger.error(f'Error updating key {key}: {str(e)}')
                raise MemoryException(f'Error updating key {key}: {str(e)}')

    def get_memory_model(self) -> MemoryModel:
        return self.memory_model

    def __contains__(self, key: str) -> bool:
        with self.lock:
            return key in self.memory_store