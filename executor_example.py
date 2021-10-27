from funcx import FuncXClient
from funcx.sdk.executor import FuncXExecutor
from double_delayed import double_delayed

fxc = FuncXClient()
fx = FuncXExecutor(fxc)

# tutorial endpoint
ep_id = '4b116d3c-1703-4f8f-9f6f-39921e5864df'

x = 50
future = fx.submit(double_delayed, x, endpoint_id=ep_id)
result = future.result()
print(result)
