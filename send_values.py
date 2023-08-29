import requests
import img_read
import datetime
import json
import id_token

def send_firebase():
    # Define the URL of your database API endpoint
    # url = "http://localhost/Intelligent_Counter/ai_project/send_data.php"
    url ="https://intelligentcounter-29709-default-rtdb.europe-west1.firebasedatabase.app/"
    uid ="qMPDfwFAnVN5J2lSmOwdfUhg20z2"
    id_user=1
    time=str(datetime.datetime.now())
    # Data you want to send in the POST request
    data = {
        "Value": img_read.image(),
        "Id_user": id_user,
        "Timestamps": time,
    }
    print(data)
    # Send the POST request
    response = requests.post(f"{url}/{uid}/values/.json?auth={id_token.load_refresh_token()}", json.dumps(data))

    # Check the response
    if response.status_code == 200:
        print("POST request successful!")
        print("Response: ", response.text)
    else:
        print("POST request failed. Status code:", response.status_code)
        print("Response:", response.text)

if __name__=='__main__':
    send_firebase()