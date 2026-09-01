import sys, asyncio
sys.path.append('.')

from Oneforall.platforms.Youtube import YouTubeAPI

async def test():
    yt = YouTubeAPI()
    print(await yt.title("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

asyncio.run(test())
