import json, random

def read_json() :
    with open('data.json', mode='r', encoding='utf-8') as data:
        return json.loads(data.read())

data = read_json()
start=data["before"]
middle=data["famous"]
end=data["after"]
bosh=data["bullshit"]

def root() :
    root = ""
    for i in range(random.randint(1,3)):
        root += random.choice(bosh)
    root += random.choice(middle)
    root = root.replace('a',random.choice(start))
    root = root.replace('b',random.choice(end))
    return root
    
def leaf() :
    return random.choice(end)

def tree() :
    return random.choice(middle) + leaf()

def hello() :
    print('輸入你想掰的主題 ! ')
    title = input('=> ')
    print('輸入長度 ! ')
    length = input('=> ')
    res = "   "
    while len(res)<int(length) :
        res = res + root()
    res = res.replace('x',title)
    print(res)
hello()
    