# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import asyncio

async def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    await asyncio.sleep(1)
    await print_hi(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.ensure_future(print_hi('bosco'))
    asyncio.get_event_loop().run_forever()

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
