import os
import yaml
from redis import Redis
from redis.config import RedisConfig

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def create_redis_client(config: dict) -> Redis:
    return Redis(host=config['host'], port=config['port'], db=config['db'])

def create_redis_config(config_path: str) -> RedisConfig:
    config = load_config(config_path)
    return RedisConfig(
        host=config['host'],
        port=config['port'],
        db=config['db'],
        username=config.get('username'),
        password=config.get('password')
    )

if __name__ == '__main__':
    config_path = os.environ.get('CACHE_REDIS_CONFIG_PATH')
    if not config_path:
        raise ValueError('CACHE_REDIS_CONFIG_PATH environment variable is missing')

    config = create_redis_config(config_path)
    print(config)