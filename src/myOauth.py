def getKey(KeyPath):
    d = dict()
    with open(KeyPath, 'r') as f:
        for line in f.readlines():
            sep_idx = line.find('=')
            key, value = line[:sep_idx], line[sep_idx+1:]
            d[key] = value.strip()
    
    return d
