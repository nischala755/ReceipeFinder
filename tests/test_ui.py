import unittest
from app.ui import get_ingredients

class TestUI(unittest.TestCase):
    def test_get_ingredients(self):
        input_values = ['tomato, cheese']
        def mock_input(s):
            return input_values.pop(0)
        get_ingredients.input = mock_input
        ingredients = get_ingredients()
        self.assertEqual(ingredients, ['tomato', 'cheese'])

if __name__ == "__main__":
    unittest.main()
