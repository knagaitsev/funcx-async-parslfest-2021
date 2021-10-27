import time
from funcx.sdk.client import FuncXClient
from funcx.utils.errors import TaskPending
from double_delayed import double_delayed

fxc = FuncXClient()

# tutorial endpoint
ep_id = '4b116d3c-1703-4f8f-9f6f-39921e5864df'
func_id = fxc.register_function(double_delayed)

x = 50
task_id = fxc.run(x, endpoint_id=ep_id, function_id=func_id)

while True:
    try:
        # HTTP task query
        result = fxc.get_result(task_id)
        print(result)
        break
    except TaskPending:
        # task is still pending, continue waiting
        print('Task pending')
    time.sleep(1)
