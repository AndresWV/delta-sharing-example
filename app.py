import requests

def test_delta_sharing():
    url = "http://localhost:8080/shares"
    try:
        response = requests.get(url)
        response.raise_for_status()
        shares = response.json()
        print("Delta Sharing Server is running. Available shares:")
        for share in shares:
            print(f"- {share['name']}")
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to Delta Sharing server: {e}")

if __name__ == "__main__":
    test_delta_sharing()
