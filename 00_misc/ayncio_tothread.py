import asyncio
import time

def blocking_function(seconds):
    """A synchronous, blocking function."""
    print(f"Thread started for {seconds} seconds...")
    time.sleep(seconds)  # time.sleep() is blocking
    print(f"Thread finished after {seconds} seconds.")
    return f"Result: {seconds}"

async def main():
    start_time = time.time()

    # Run blocking functions concurrently in separate threads
    task1 = asyncio.to_thread(blocking_function, 3)
    task2 = asyncio.to_thread(blocking_function, 1)

    # Await the results
    results = await asyncio.gather(task1, task2)

    end_time = time.time()
    print(f"Results: {results}")
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Run the main coroutine
if __name__ == "__main__":
    asyncio.run(main())
