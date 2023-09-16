import send_conso
import send_values
import requests
import id_token
import datetime
import json
from flask import Flask
import main
app = Flask(__name__)
@app.route('/')

def index():
    get_firebase_data()
    return "Hello, World!"

def get_firebase_data():
    url = "https://intelligentcounter-29709-default-rtdb.europe-west1.firebasedatabase.app/"
    uid = "qMPDfwFAnVN5J2lSmOwdfUhg20z2"
    response = requests.get(f"{url}/{uid}/activities/.json?auth={id_token.load_refresh_token()}")
    data = response.json()
    print(data)
    if data['isActive']==True:
        send_conso.send_firebase()
        send_values.send_firebase()
        
        time=str(datetime.datetime.now())
        data = {
            "Id_user": 1,
            "Timestamps": time,
            "isActive": False,
        }
        response=requests.put(f"{url}/{uid}/activities/.json?auth={id_token.load_refresh_token()}", json.dumps(data))
    else:
        print("nothing happens")


if __name__ == '__main__':
    app.run(debug=True)