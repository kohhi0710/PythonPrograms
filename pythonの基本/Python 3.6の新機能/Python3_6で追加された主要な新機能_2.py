# --------------------
# 非同期ジェネレータ
# --------------------

import asyncio
import datetime

async def MyAsyncGenerator():
    while True:
        time = input('input wait time(0 to break): ')
        time = int(time)

        if time > 0:
            pass
        elif time == 0:
            break
        else:
            break

        await mysleep(time)
        # returnではなくyieldで値(と制御)を戻している
        yield time

async def mysleep(time):
    to = datetime.datetime.now() + datetime.timedelta(seconds = time)

    while True:
        await asyncio.sleep(1)
        print('*',sep = '',end = '',flush = True)

        if datetime.datetime.now() > to:
            break
    print('')

async def main():
    agen = MyAsyncGenerator()

    async for msg in agen:
        print(f'sleep time: {msg} sec(s)')
    # running = True
    # while running:
    #   try:
    #     msg = await agen.__anext__()
    #   except StopAsyncIteration as e:
    #     print('catch StopAsyncIteration')
    #     running = False
    #   else:
    #     print(f'sleep time: {msg} sec(s)')

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


