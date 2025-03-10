from database.json_storage import JSONStorage
from database.redis import CacheManager

db = JSONStorage()
cache = CacheManager()
