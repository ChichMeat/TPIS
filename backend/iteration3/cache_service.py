import time
from functools import wraps

class CacheService:
    """Сервис для кэширования результатов"""
    
    _cache = {}
    
    @staticmethod
    def cache_result(ttl_seconds=300):
        """Декоратор для кэширования результатов функций"""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                # Создаём ключ кэша
                cache_key = f"{func.__name__}_{str(args)}_{str(kwargs)}"
                
                # Проверяем кэш
                if cache_key in CacheService._cache:
                    cached_value, timestamp = CacheService._cache[cache_key]
                    if time.time() - timestamp < ttl_seconds:
                        print(f"Cache HIT for {cache_key}")
                        return cached_value
                
                # Вычисляем и кэшируем
                result = func(*args, **kwargs)
                CacheService._cache[cache_key] = (result, time.time())
                print(f"Cache MISS for {cache_key}")
                return result
            return wrapper
        return decorator
    
    @staticmethod
    def clear_cache():
        """Очистка всего кэша"""
        CacheService._cache.clear()
        print("Кэш очищен")

if __name__ == "__main__":
    @CacheService.cache_result(ttl_seconds=60)
    def expensive_operation(x):
        time.sleep(2)  # Имитация долгой операции
        return x * x
