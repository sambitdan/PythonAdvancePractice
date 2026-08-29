#async python refers to asynchronous python were we use a single thread for multiple purpose.

# In multithreading we are using multtiple threads where each thread is using for each task, 
# whereas in async python a single thread is using for multiple tasks

# Eventloop will manage our thread
# Each task or async function is called coroutines.
# Whenever we run a coroutine we start the eventloop right away for each task we have a eventloop.

import asyncio #io refers to input-output as it is input output bound task
import time

def main():
    print('Hello')
    time.sleep(3)
    print('World')

# main()

async def main_1():  # The moment we write async it becomes coroutine
    print('Hello')
    asyncio.sleep(3)
    print('World')

# time module is synchronous library even if I use asyncronous function 
# and I am using syncronous library inside it, it will behave like syncronous code.
# So whatever library  we are using while writing asyncronous python code it should be asyncronous.
asyncio.run(main_1())


# If we want our function to wait and then print and while performing our task it should not loc our resources then we should use await
async def main_2():  
    print('Hello')
    await asyncio.sleep(3) # await will provide a gusrdrail before running to the next function however during this time thread is free, 
    # whereas for syncronous code thread is locked
    print('World')

asyncio.run(main_2())