import requests
import json

def get_refresh_token(email, password):
    try:
        url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDlwh2J50wOfXxXsTx0ube3VIUOzXh1r4Q'

        headers = {'Content-Type': 'application/json'}

        payload = {
            'email': email,
            'password': password,
            'returnSecureToken': True
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            responseData = json.loads(response.text)
            refreshToken = responseData['refreshToken']
            userRefreshToken = refreshToken
            print('Refresh token:', userRefreshToken)
        else:
            print('Error:', response.status_code)
    except Exception as e:
        print('Error:', e)


get_refresh_token('fayezzouari@gmail.com', 'helloworld')