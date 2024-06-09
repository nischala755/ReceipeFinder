
import unittest
from app.api import get_recipes

class TestAPI(unittest.TestCase):
    def test_get_recipes(self):
        ingredients = ['tomato', 'cheese']
        recipes = get_recipes(ingredients)
        self.assertIsInstance(recipes, list)

if __name__ == "__main__":
    unittest.main()
