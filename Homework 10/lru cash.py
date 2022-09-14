import redis

max_size=5

db_redis = redis.Redis(
    host='localhost',
    port=6379,
    db=0
)


class LruCache:
    def __init__(self, func, max_size, db_redis):
        self.func = func
        self.max_size = max_size
        self.db_redis = db_redis
        self.key = self.func.__name__

    def __call__(self, *args, **kwargs):
        try:
            # получаем строковое выражение аргументов функции для уникального ключа
            func_param = ''
            for i in args:
                func_param += f':{str(i)}'
            for key, value in kwargs.items():
                func_param += f':{str(key)}\{str(value)}'

            full_key = f'{self.key}::{func_param}'

            if self.db_redis.get(full_key):
                result = self.db_redis.get(full_key)

            else:
                result = self.func(*args, **kwargs)
                self.db_redis.set(full_key, result)

            self.db_redis.lrem(self.key, -1, func_param)
            self.db_redis.lpush(self.key, func_param)

            if self.db_redis.llen(self.key) > self.max_size:
                last_elem = self.db_redis.rpop(self.key)
                self.db_redis.delete(f'{self.key}::{last_elem}')

            return result

        except Exception as error:
            print('Wrong input')
            raise error

            
def lru_cache(max_size):
    def wrapper(func):
        cache = LruCache(func, max_size, db_redis)
        return cache
    return wrapper