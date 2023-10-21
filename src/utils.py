import httpx
import json


async def get_async_api_data(api_request_url: str) -> json:
    async with httpx.AsyncClient() as client:
        response = await client.get(api_request_url)
        data = response.json()
        return data
