import asyncio
import aiohttp
import time

urls = [
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2",
    "https://httpbin.org/delay/2"
]

async def fetch(session, url):
    start = time.time()

    async with session.get(url) as response:
        await response.text()

    print(f"Finished in {time.time()-start:.2f}s")

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            fetch(session, urls[0]),
            fetch(session, urls[1]),
            fetch(session, urls[2])
        )

start = time.time()
asyncio.run(main())
print("Total:", round(time.time()-start, 2), "seconds")