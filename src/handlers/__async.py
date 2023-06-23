import asyncio


def asyncio_runner(func, *args, **kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    res = loop.run_until_complete(func(*args, *kwargs))
    loop.close()
    return res
