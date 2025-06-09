import asyncio

async def function_one():
    print("Function One: Start")
    await asyncio.sleep(1)
    print("Function One: End")
    return "Function One Completed"

async def function_two():   
    print("Function Two: Start")
    await asyncio.sleep(1)
    print("Function Two: End")
    return "Function Two Completed"


async def function_three():
    print("Function Three: Start")
    await asyncio.sleep(1)
    print("Function Three: End")  
    return "Function Three Completed"


async def main():
    obj = await asyncio.gather(function_one(),function_two(),function_three())
    print("Main Ended")
    print(obj)

asyncio.run(main())    
