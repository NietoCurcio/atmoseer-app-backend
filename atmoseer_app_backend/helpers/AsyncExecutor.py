import asyncio
import functools
from collections.abc import Callable
from concurrent.futures import Executor, ProcessPoolExecutor, ThreadPoolExecutor


class AsyncExecutor:
    @property
    def THREAD(self) -> Executor:
        return ThreadPoolExecutor()

    @property
    def PROCESS(self) -> Executor:
        return ProcessPoolExecutor()

    @staticmethod
    def execute(fn: Callable, *args, executor: Executor | None = None, **kwargs) -> asyncio.Future:
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(executor, functools.partial(fn, *args, **kwargs))


async_executor = AsyncExecutor()
