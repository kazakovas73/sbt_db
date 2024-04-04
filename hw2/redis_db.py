import redis
import json
import time

# Подключение к базе данных Redis
r = redis.Redis(host='localhost', port=6379, db=0)


def store_json_in_redis_set(data, prefix='in_set'):
    for num, elem in enumerate(data):
        # full_key = f'{prefix}:{num}'
        r.sadd(prefix, json.dumps(elem))
    print(f"\nElements in set: {r.scard(prefix)}")


def store_json_in_redis_hset(data, prefix='in_hset'):
    for num, elem in enumerate(data):
        # full_key = f'{prefix}:{num}'
        r.hset(prefix, str(num), json.dumps(elem))
    print(f"\nElements in hset: {r.hlen(prefix)}")
    

def store_json_in_redis_zset(data, prefix='in_zset'):
    for num, elem in enumerate(data):
        # full_key = f'{prefix}:{num}'
        r.zadd(prefix, {json.dumps(elem): num})
    print(f"\nElements in zset: {r.zcard(prefix)}")


def store_json_in_redis_list(data, prefix='in_list'):
    for num, elem in enumerate(data):
        # full_key = f'{prefix}:{num}'
        r.lpush(prefix, json.dumps(elem))
    print(f"\nElements in list: {r.llen(prefix)}")


def main():
    # Чтение JSON-файла с различными типами данных
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        print(f'Dataset size: {len(data)} elements\n')

    type_funcs = [
        store_json_in_redis_set,
        store_json_in_redis_hset,
        store_json_in_redis_zset,
        store_json_in_redis_list
    ]

    for func in type_funcs:
        start_time = time.time()
        func(data)
        print(f"--- {time.time() - start_time} seconds ---")
        r.flushdb()  


if __name__ == '__main__':
    main()