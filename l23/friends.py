from urllib.request import urlopen
from json import loads
from time import sleep

friends = []
your_id = "280096223"

data = urlopen(
    "https://api.vk.com/method/friends.get?user_id="+your_id+"&fields=nickname"
    ).read().decode("utf-8")

data = loads(data)
# print(data)

friends_response = data["response"]
# print(friends_response)
friends_id = [el["user_id"] for el in friends_response]
# print(friends_id)
friends_name = [name["first_name"] + " " + name["last_name"] 
    for name in friends_response]
# print(friends_name)

for f_id, f_name in zip(friends_id,friends_name):
    data = urlopen("https://api.vk.com/method/friends.get?user_id="+str(f_id)
        ).read().decode("utf-8")
    data = loads(data)
    try:
        friends_friends_id = data["response"]
    except:
        continue
    friends.append([f_name, len(set(friends_id) & set(friends_friends_id))])
    sleep(0.1)

friends.sort(key=lambda x: -x[1])
print(friends)