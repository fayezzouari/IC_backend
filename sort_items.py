import requests
import id_token
# Firebase configurations
def sorted_items(path):
    node_path = "https://intelligentcounter-29709-default-rtdb.europe-west1.firebasedatabase.app/qMPDfwFAnVN5J2lSmOwdfUhg20z2"

    # Retrieve data from Firebase
    response = requests.get(f"{node_path}/{path}/.json?auth={id_token.load_refresh_token()}")
    data = response.json()
    # Sort the data based on timestamps
    sorted_data = sorted(data.items(), key=lambda x: x[1].get("timestamps", 0))

    # Print the sorted data in a dictionary format
    sorted_dict = {key: value for key, value in sorted_data}
    print("sorted items")
    # print(sorted_dict)
    return sorted_dict

if __name__=='__main__':
    sorted_items("values")