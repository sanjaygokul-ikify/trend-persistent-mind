import unittest
from packages.core import MemoryEngine, MemoryModel
from packages.utils import logging

logger = logging.getLogger(__name__)

class TestPipeline(unittest.TestCase):
    def test_pipeline(self) -> None:
        memory_model = MemoryModel.SIMPLE
        memory_engine = MemoryEngine(memory_model)

        logger.info('Starting pipeline test')

        memory_engine.store('key1', 'value1')
        memory_engine.store('key2', 'value2')

        self.assertEqual(memory_engine.retrieve('key1'), 'value1')
        self.assertEqual(memory_engine.retrieve('key2'), 'value2')

        memory_engine.update('key1', 'new_value1')
        self.assertEqual(memory_engine.retrieve('key1'), 'new_value1')

        memory_engine.delete('key2')
        with self.assertRaises(MemoryException):
            memory_engine.retrieve('key2')

        logger.info('Finished pipeline test')

if __name__ == '__main__':
    unittest.main()