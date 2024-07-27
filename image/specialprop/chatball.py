import requests, os

folderdl = "chatBall/"

def makedirr(file):
    if not os.path.exists(os.path.dirname(file)):
        try: os.makedirs(os.path.dirname(file))
        except:  pass

for i in range(100):
    a = requests.get("http://res.gn.zing.vn/image/specialprop/chatBall/chatBall{}/icon.png".format(i))
    if a.status_code == 200:
        makedirr(folderdl + "chatBall{}/icon.png".format(i))
        open(folderdl + "chatBall{}/icon.png".format(i), "wb").write(a.content)