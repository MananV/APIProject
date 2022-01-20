import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, 'name': "Test Video 1", "views": 100},
        {"likes": 100, 'name': "Test Video 2", "views": 200},
        {"likes": 1000, 'name': "Test Video 3", "views": 300},
        {"likes": 10000, 'name': "Test Video 4", "views": 400}
        ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()

response = requests.get(BASE + "video/6")
print(response.json())
