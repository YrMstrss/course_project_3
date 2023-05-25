def format_date(input_date: str):
    date_list = input_date[0:10].split('-')
    return '.'.join(date_list[::-1])
