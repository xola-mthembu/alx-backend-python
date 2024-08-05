#!/usr/bin/env python3

import asyncio

task_wait_n = __import__('4-tasks').task_wait_n

n = 5
max_delay = 6
loop = asyncio.get_event_loop()
print(loop.run_until_complete(task_wait_n(n, max_delay)))
