import requests

API_KEY = 'e76c06f175644c27bb3b76107f40b055'  # Replace with your actual API key

def get_recipes(ingredients):
    print("Using API Key:", API_KEY)  # Debugging: Print the API key
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={','.join(ingredients)}&apiKey={API_KEY}"
    response = requests.get(url)
    print("Response Status Code:", response.status_code)  # Debugging: Print the status code
    print("Response Text:", response.text)  # Debugging: Print the response text
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return []
