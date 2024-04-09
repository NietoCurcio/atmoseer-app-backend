import asyncio
import functools
from collections.abc import Callable
from concurrent.futures import Executor


class AsyncExecutor:
    @staticmethod
    def execute(
        fn: Callable, executor: Executor | None = None, *args, **kwargs
    ) -> asyncio.Future:
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(executor, functools.partial(fn, *args, **kwargs))


async_executor = AsyncExecutor()
