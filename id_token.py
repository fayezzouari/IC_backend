import requests

def getIdToken(refresh_token):
    url = "https://securetoken.googleapis.com/v1/token?key=AIzaSyC4vl0DJrf2rmk6PNDv6XuQsrFR1FmIMI4"
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    for i in range(3):
        response = requests.post(url, data=payload, headers=headers)
        try:
            response.raise_for_status()
            return response.json()['id_token']
        except (requests.exceptions.HTTPError, KeyError) as e:
            print(f"[Python] Error fetching ID token: {e}")
    print("[Python] Failed to fetch ID token after 3 attempts")
    return None

def load_refresh_token():
    with open('refresh_token.txt', 'r') as file:
        refresh_token=file.read()
        id_token=getIdToken(refresh_token)
    file.close()
    return id_token