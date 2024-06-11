<h3> Python Async Comprehension </h3>
<i>(Derived from PEP 530,Created on 3-September 2016)</i>
Python has extensive support for synchronous comprehensions, allowing to produce lists, dicts, and sets with a simple and concise syntax. We propose implementing similar syntactic constructions for the asynchronous code.

To illustrate the readability improvement, consider the following example:

result = []
async for i in aiter():
    if i % 2:
        result.append(i)

With the proposed asynchronous comprehensions syntax, the above code becomes as short as:

result = [i async for i in aiter() if i % 2]

Creating an Asyncronous comprehesion is, however, a bit differernt from regular list comprehension

(Derived from <a href="https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/">this blog</a>)
For example, in the code below we need to create an async function in place of the range(100) so as to call it indirectly
import asyncio

async def test(): 
    return [i async for i in range(100) if i % 2]

loop = asyncio.get_event_loop()
loop.run_until_complete(test())

Here is the example with range indirectly called

import asyncio

async def numbers(numbers):
    for i in range(numbers):
        yield i
        await asyncio.sleep(0.5)

async def main():
    odd_numbers = [i async for i in numbers(10) if i % 2]
    print(odd_numbers)

if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close() 
