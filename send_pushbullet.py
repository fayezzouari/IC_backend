from pushbullet import Pushbullet

API_KEY = "o.b7PfqYP3agcQLXKwW1kKkq2pM4TowRfb"
filename = 'counter.txt'

with open(filename, mode='r') as f:
    text = f.read()

pb = Pushbullet(API_KEY)
push = pb.push_note("You Counter today: ", text)
