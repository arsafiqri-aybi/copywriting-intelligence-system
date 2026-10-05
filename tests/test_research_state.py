import unittest
from scripts.validate_research_state import validate

class ResearchStateIntegrityTest(unittest.TestCase):
    def test_integrity(self):
        self.assertEqual(validate(), [])

if __name__ == "__main__":
    unittest.main()
