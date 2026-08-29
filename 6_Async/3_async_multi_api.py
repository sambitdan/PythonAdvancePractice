import asyncio

async def api_call(url : str):
    print("fetching data from: ",url)
    await asyncio.sleep(3)
    print("Data fetched from: ",url)


# def api_call():
#     time.sleep(3)
#     return "orders data"

async def main():
    # urls = ["https://api1.com","https//api2.com","https://api3.com"]
    # Creating Taks with Gather
    tasks = await asyncio.gather(
        api_call("https://api1.com"),
        api_call("https://api2.com"),
        api_call("https://api3.com")
    )

    print("All api calls completed")
# Another way to create tasks with list comprehension
    # tasks= [api_call(url) for url in ["https://api1.com","https//api2.com","https://api3.com"]]
    # results = await asyncio.gather(*tasks)



asyncio.run(main())