import pickle

f = open('sites','rb')

sites = pickle.load(f)

print (sites,sites.__len__())