#configure user API_key and Yandex login

filename="user_infos.txt"

API_key=raw_input("Enter your API Key: ")
with open (filename, 'w') as file:
	file.write(API_key+'\n')

login=raw_input("Enter your Yandex login: ")
with open (filename, 'a') as file:
	file.write(login)