import time
from typing import Dict

metrics: Dict[str, float] = {}

def record_metric(name: str, value: float) -> None:
    metrics[name] = value

def get_metric(name: str) -> float:
    return metrics.get(name, 0.0)