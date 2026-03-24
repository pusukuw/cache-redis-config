# cache-redis-config
=====================

[caching-redis-config]: https://github.com/[your-github-username]/cache-redis-config

## Description

cache-redis-config is a lightweight Redis configuration manager for caching applications. It provides a simple and flexible way to configure and manage Redis connections, settings, and cache policies in your Python applications.

## Features

* **Easy Redis Configuration**: Easily configure Redis connections, settings, and cache policies using a simple and intuitive API.
* **Flexible Cache Policies**: Implement custom cache policies using a modular and extensible architecture.
* **Redis Connection Management**: Easily manage and switch between multiple Redis connections with connection pooling.
* **Cache Statistics**: Monitor and track cache performance and statistics with detailed metrics.
* **Error Handling**: Gracefully handle errors and exceptions during Redis operations with retry mechanisms.
* **Environment Variable Support**: Configure Redis settings using environment variables for seamless deployment.
* **Health Checks**: Perform health checks on Redis connections to ensure availability.

## Technologies Used

* **Python 3.8+**: cache-redis-config is built using Python 3.8+ and supports the latest Python standards.
* **Redis**: cache-redis-config uses the `redis` library to interact with Redis.
* **Pydantic**: cache-redis-config uses Pydantic for data validation and modeling.
* **Dotenv**: cache-redis-config supports `.env` files for environment variable management.

## Installation

To install cache-redis-config, run the following command:

```bash
pip install cache-redis-config
```

## Usage

To use cache-redis-config, import it in your Python application and create a `CacheConfig` instance:

```python
from cache_redis_config import CacheConfig

config = CacheConfig(
    host='localhost',
    port=6379,
    db=0,
    password='my_password',
    max_connections=10,
    retry_attempts=3,
    retry_delay=1
)

# Create a Redis connection using the config instance
redis = config.get_redis_connection()

# Use the Redis connection to perform cache operations
```

## Environment Variables

You can also configure Redis settings using environment variables:

```bash
export REDIS_HOST="localhost"
export REDIS_PORT="6379"
export REDIS_DB="0"
export REDIS_PASSWORD="my_password"
```

## Contributing

Contributions to cache-redis-config are welcome! Please submit pull requests or issues to the repository.

## License

cache-redis-config is licensed under the [MIT License](LICENSE).

## Changelog

See the [Changelog](CHANGELOG.md) for a detailed history of changes and improvements to cache-redis-config.

## Support

For support and questions, please contact us at [your-email@example.com](mailto:your-email@example.com).