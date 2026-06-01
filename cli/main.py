import argparse
from packages.core import MemoryEngine
from packages.utils import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Persistent Mind CLI')

parser.add_argument('--memory-model', type=str, help='Memory model to use', choices=['simple', 'distributed'])

def main() -> None:
    args = parser.parse_args()
    memory_model = MemoryEngine.MemoryModel.from_string(args.memory_model)
    memory_engine = MemoryEngine(memory_model)

    logger.info(f'Using memory model: {memory_model}')

if __name__ == '__main__':
    main()