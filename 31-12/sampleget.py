import requests

def fetch_github_info():
    url = "https://api.github.com"
    
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print("Headers:", response.headers)
    print("Response Data:")
    print(response.json())

if __name__ == "__main__":
    fetch_github_info()
