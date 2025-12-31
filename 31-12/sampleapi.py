import requests

def get_user_detail(username):
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        print("User name:", user_data.get("name"))
        print("Public Repos:", user_data.get("public_repos"))
    else:
        print("Failed to retrieve data:")

if __name__ == "__main__":
    get_user_detail("lokeshprabhu257")