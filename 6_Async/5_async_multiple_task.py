import asyncio
import time

# First Task
async def api_call(url : str, delay : int = 2):
    print("fetching data from: ",url)
    await asyncio.sleep(delay)
    print("Data fetched from: ",url)

# Second Task

async def execution():
    time.sleep(5)
    print("Execution Completed")

# Third Task
async def transformation():
    asyncio.sleep(4)
    print("Transformation Completed")

async def main():
    # urls = ["https://api1.com","https//api2.com","https://api3.com"]
    # Creating Taks with Gather
    tasks = await asyncio.gather(
        api_call("https://api1.com"),
        execution(),
        transformation()
    )

    print("All api calls completed")
# Another way to create tasks with list comprehension
    # tasks= [api_call(url) for url in ["https://api1.com","https//api2.com","https://api3.com"]]
    # results = await asyncio.gather(*tasks)



asyncio.run(main())