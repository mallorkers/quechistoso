import redis
import random

r = redis.StrictRedis(host='localhost', port='6379', db=0)

'''
for i in range(0, 1000000):
	r.rpush("caca", str(random.randint(1000, 1000000)) )
'''

print r.dbsize()