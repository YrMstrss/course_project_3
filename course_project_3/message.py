from course_project_3 import format_accounts
from course_project_3 import format_date

def get_message(operation: dict):
    date = format_date.format_date(operation['date'])
    description = operation['description']
    from_account = format_accounts.format_from_account(operation['from'])
    to_account = format_accounts.format_to_account(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    first_line_list = [date, description]
    second_line_list = [from_account, '->', to_account]
    third_line_list = [amount, currency]

    first_line = ' '.join(first_line_list)
    second_line = ' '.join(second_line_list)
    third_line = ' '.join(third_line_list)

    return '\n'.join([first_line, second_line, third_line])

# """
# 26.08.2019 Перевод организации
# Maestro 1596 83** **** 5199 -> Счет **9589
# 31957.58 руб.
#     """