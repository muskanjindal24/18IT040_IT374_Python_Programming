d = {'British Raj': 200, 'Mughal Empire': 350, 'Delhi Sultanate': 100, 'Maurya Vansh': 150}
print(sorted(d.items(), key = lambda k:(k[1], k[0])))
