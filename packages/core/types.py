from typing import Dict
from enum import Enum

class MemoryModel(Enum):
    SIMPLE = 'simple'
    DISTRIBUTED = 'distributed'

    @classmethod
    def from_string(cls, value: str) -> 'MemoryModel':
        if value == 'simple':
            return cls.SIMPLE
        elif value == 'distributed':
            return cls.DISTRIBUTED
        else:
            raise ValueError(f'Invalid memory model: {value}')