import redis

key = 'products'

r = redis.Redis(host='172.18.0.6', port=6379, password='foobared', db=15)
r.lpush(key, 'product-15263655')
r.lpush(key, 'product-25636478')
print('list length: ' + str(r.llen(key)))
print(r.rpop(key))
print(r.rpop(key))
print('complete.')
