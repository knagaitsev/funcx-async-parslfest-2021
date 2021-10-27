from funcx.sdk.client import FuncXClient
from double_delayed import double_delayed

fxc = FuncXClient(asynchronous=True)
# tutorial endpoint
ep_id = '4b116d3c-1703-4f8f-9f6f-39921e5864df'
func_id = fxc.register_function(double_delayed)

async def task():
    x = 50
    result = await fxc.run(x, endpoint_id=ep_id, function_id=func_id)
    print(result)

fxc.loop.run_until_complete(task())
# If running in Jupyter notebook, just do: await task()
