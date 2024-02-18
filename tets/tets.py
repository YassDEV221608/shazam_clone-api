import asyncio
from shazamio import Shazam
import os


async def main():
  shazam = Shazam()
  with open("sample.ogg", 'rb') as file:
    out = await shazam.recognize_song("sample.ogg")
    print(out)


if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  result = loop.run_until_complete(main())
  print(main)