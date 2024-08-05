#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

loop = asyncio.get_event_loop()
print(loop.run_until_complete(wait_random()))
print(loop.run_until_complete(wait_random(5)))
print(loop.run_until_complete(wait_random(15)))
