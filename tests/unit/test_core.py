import unittest
from packages.core import MemoryEngine, MemoryModel

class TestCore(unittest.TestCase):
    def test_memory_engine(self) -> None:
        memory_model = MemoryModel.SIMPLE
        memory_engine = MemoryEngine(memory_model)
        self.assertEqual(memory_engine.get_memory_model(), memory_model)

        memory_engine.store('key', 'value')
        self.assertEqual(memory_engine.retrieve('key'), 'value')

        memory_engine.update('key', 'new_value')
        self.assertEqual(memory_engine.retrieve('key'), 'new_value')

        memory_engine.delete('key')
        with self.assertRaises(MemoryException):
            memory_engine.retrieve('key')

        self.assertFalse('key' in memory_engine)
        memory_engine.store('key', 'value')
        self.assertTrue('key' in memory_engine)

if __name__ == '__main__':
    unittest.main()