import unittest
from packages.core import MemoryException

class TestRuntime(unittest.TestCase):
    def test_memory_exception(self) -> None:
        with self.assertRaises(MemoryException):
            raise MemoryException('Test exception')

if __name__ == '__main__':
    unittest.main()