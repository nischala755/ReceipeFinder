def get_ingredients():
    ingredients = input("Enter ingredients separated by commas: ").split(',')
    return [ingredient.strip() for ingredient in ingredients]

def display_recipes(recipes):
    for recipe in recipes:
        print(f"Recipe: {recipe['title']}")
        print(f"Ingredients: {', '.join([ingredient['name'] for ingredient in recipe.get('missedIngredients', [])])}")
        print()
