# Normal Syncronous API calls
# import time

# def api_call():
#     time.sleep(3)
#     return "orders data"


# def execute():
#     print("Executing API call")
#     result = api_call()
#     print("Data Fetched: ",result)

# execute()

# Asyncronous Api Call

import asyncio

async def api_call():
    await asyncio.sleep(3)
    return "orders data"

# def api_call():
#     time.sleep(3)
#     return "orders data"

async def execute():
    print("Executing API call")
    result = await api_call() # If I don't use await we will get error as thread will go to the execute 
    # the print the result before storing the result
    print ("Data Fetched: ",result)


asyncio.run(execute())