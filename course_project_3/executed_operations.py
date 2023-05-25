def get_executed_operations(operation_list: list):
    executed_operations = []
    for operation in operation_list:
        if operation['state'] == 'EXECUTED':
            executed_operations.append(operation)
    return executed_operations[0:5]
