import random
import timeit
from funcx import FuncXClient
from funcx.sdk.executor import FuncXExecutor
from double_delayed import double_delayed

fxc = FuncXClient()
fx = FuncXExecutor(fxc, batch_enabled=True, batch_interval=1.0)

# tutorial endpoint (switch to your own endpoint to run much faster)
ep_id = '4b116d3c-1703-4f8f-9f6f-39921e5864df'

def run():
    futures = []
    for _ in range(50):
        x = random.randint(0, 100)
        future = fx.submit(double_delayed, x, endpoint_id=ep_id)
        futures.append(future)

    for future in futures:
        result = future.result()
        print(f'Result: {result}')

t = timeit.timeit(run, number=1)
print(f'Time: {round(t, 2)}s')
