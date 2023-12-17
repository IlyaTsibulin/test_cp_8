import pytest
import allure
from app import get_json

@pytest.mark.asyncio
async def test_get_json_with_valid_url(event_loop):
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = await get_json(url)
    assert "userId" in result
    assert "id" in result
    assert "title" in result
    assert "completed" in result

@pytest.mark.asyncio
async def test_get_json_with_invalid_url(event_loop):
    url = "https://jsonplaceholder.typicode.com/invalid_endpoint"
    with pytest.raises(aiohttp.ClientResponseError):
        await get_json(url)

@allure.feature("Priority Tests")
@allure.story("High Priority Test")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.asyncio
async def test_get_json_high_priority(event_loop):
    url = "https://jsonplaceholder.typicode.com/todos/2"
    result = await get_json(url)
    assert "userId" in result
    assert "id" in result
    assert "title" in result
    assert "completed" in result

@allure.feature("Priority Tests")
@allure.story("Low Priority Test")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.asyncio
async def test_get_json_low_priority(event_loop):
    url = "https://jsonplaceholder.typicode.com/todos/3"
    result = await get_json(url)
    assert "userId" in result
    assert "id" in result
    assert "title" in result
    assert "completed" in result