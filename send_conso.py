import sort_items
import requests
import img_read
import datetime
import json
import id_token

def get_latest_data():
    res=dict()
    res=sort_items.sorted_items("values")
    res_list=list(res)
    print(res_list)
    return int(res[res_list[len(res_list)-1]]['Value'])-int(res[res_list[len(res_list)-2]]['Value'])

def send_firebase():
    url ="https://intelligentcounter-29709-default-rtdb.europe-west1.firebasedatabase.app/"
    uid ="qMPDfwFAnVN5J2lSmOwdfUhg20z2"
    id_user=1
    time=str(datetime.datetime.now())
    # Data you want to send in the POST request
    data = {
        "Value": get_latest_data(),
        "Id_user": id_user,
        "Timestamps": time,
    }
    print(data)
    # Send the POST request
    response = requests.put(f"{url}/{uid}/conso/.json?auth={id_token.load_refresh_token()}", json.dumps(data))
    print(response.json())

if __name__=='__main__':
    send_firebase()