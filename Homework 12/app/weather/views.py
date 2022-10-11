import aiohttp_jinja2
import aiohttp
import asyncio
from .urls import url_1, url_3, url_2
from datetime import datetime
from bs4 import BeautifulSoup

now = datetime.now().date()
date = str(now)


async def find_weather_1(session, url):
    async with session.get(url, ssl=False) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        try:
            inform = soup.find('span', {'class': "wr-day-temperature__high-value"})
            temp = inform.find('span', {'class': "wr-value--temperature--c"}).text.strip()
            return temp
        except AttributeError:
            return None



async def find_weather_2(session, url):
    async with session.get(url, ssl=False) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        try:
            inform = soup.find('div', {'class': "bk-focus__qlook"})
            temp = inform.find('div', {'class': "h2"}).get_text()
            return temp
        except AttributeError:
            return None


async def find_weather_3(session, url):
    async with session.get(url, ssl=False) as response:
        html = await response.text()
        soup = BeautifulSoup(html, "html.parser")
        try:
            inform = soup.find('div', {'class': "b-metar-table__temperature-value temp-color7"})
            temp = inform.find('span', {'class': "temp"}).text
            return temp
        except AttributeError:
            return None

async def start_async():
    async with aiohttp.ClientSession() as session:
        result1, result2, result3 = await asyncio.gather(find_weather_1(session, url_1), find_weather_2(session, url_2),
                                                         find_weather_3(session, url_3))
    return result1, result2, result3


@aiohttp_jinja2.template("index.html")
async def index(request):
    result1, result2, result3 = await start_async()
    return {'result1': result1, 'result2': result2, 'result3': result3, 'url_1':url_1, 'url2':url_2, 'url3': url_3}
