from sys import getsizeof
import pickle

posts = [['hello' + str(i), i, 'host'] for i in range(10)]

print(posts)

print(4 % 5, 2 % 1, 4 % 2)

output = pickle.dumps(54512135415343435434343434)
output1 = pickle.dumps(54633456544512135415343435434343434)
print(getsizeof(output))
print(getsizeof(output1))
