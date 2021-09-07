def sayHello():
    print('Hello')

def getKey(KeyPath):
    d = dict()
    with open(KeyPath, 'r') as f:
        for line in f.readlines():
            row = line.split('=')
            key, value = row[0], row[1]
            d[key] = value.strip()
    
    return d
