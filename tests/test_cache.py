import pytest
from unittest.mock import patch

from server.cache import Cache, CacheKeyNotFound, get_cache

@pytest.fixture
def cache():
    return Cache()

@pytest.mark.asyncio
async def test_cache(cache):
    with patch('server.cache.Cache._get_key') as mock:
        mock.return_value = '100500'

        assert await cache.add('Payload') == mock()
        assert await cache.get('100500') == 'Payload'


@pytest.mark.asyncio
async def test_not_found_key(cache):
    with pytest.raises(CacheKeyNotFound):
        await cache.get('100500')


@pytest.mark.asyncio
async def test_get_cache_is_singelton():
    cache = await get_cache()
    assert cache is await get_cache() 
