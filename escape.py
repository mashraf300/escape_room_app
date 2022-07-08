import collections
from client import client
import pickle

frequencies = collections.OrderedDict()
n = 5
for i in range(n):
    word = input()
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1

print(len(frequencies))

for word in frequencies:
    print("{} count is {} ".format( word, frequencies[word]));

Client = client()
Client.chat_room()

data = pickle.dumps(frequencies)
Client.send_sms(data)

message = input()

