#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

loop = asyncio.get_event_loop()
print(loop.run_until_complete(wait_n(5, 5)))
print(loop.run_until_complete(wait_n(10, 7)))
print(loop.run_until_complete(wait_n(10, 0)))
