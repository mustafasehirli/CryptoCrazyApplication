

import requests


def get_crypto():
    response = requests.get("https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    if response.status_code == 200:
        return response.json()


crypto_response = get_crypto()
user_input = input("Enter Crypto : ")

for cryto in crypto_response:
    if cryto["currency"] == user_input:
        print(cryto["price"])
        break
