from app.api import get_recipes
from app.ui import get_ingredients, display_recipes

def main():
    ingredients = get_ingredients()
    recipes = get_recipes(ingredients)
    display_recipes(recipes)

if __name__ == "__main__":
    main()
