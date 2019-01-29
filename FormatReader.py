import json
from pprint import pprint


def load_format(json_file_name):
    with open(json_file_name) as json_file:
        format = json.load(json_file)
    return format

def make_template(format_datas):
    if format_datas['TYEP'] == 'STRING':
        return make_string_template(format_datas)
    if format_datas['TYEP'] == 'NUMBER':
        return make_number_template(format_datas)

def make_string_template(format_datas):
    pass

def string_router(data_name, data_attrs):
    router = {
        "ID": func_ID(data_attrs),
        "PRICE_A": func_PRICE_A(data_attrs),
    }
    return router[data_name]

def get_format_types(format_dict):
    return [key for key in format_dict.keys()];

def get_format_data(format_name, format_dict):
    return format_dict[format_name]
""""""""""""""""""""""""""""""""""""""""""""""""
def func_string_template(data_attrs):
    align_sign = {
        'LEFT': '',
        'RIGHT': '>',
        'MID': '^',
    }
    def wrapper(real_data):
        return "{:{padding}{align}{len}}".format(
            real_data,
            padding=data_attrs['PADDING'],
            align=align_sign.get(data_attrs['ALIGN']),
            len=data_attrs['LEN'])
    return wrapper


if __name__ == '__main__':
    data_dict = {
        'ID': 'ABC',
        'NICK': 'DUCK',
    }

    func_ID = func_string_template(
        {'LEN': 13, 'ALIGN': 'LEFT', 'PADDING': ''})
    func_NICK = func_string_template(
        {'LEN': 20, 'ALIGN': 'MID', 'PADDING': '*'})
    layout = [func_ID(data_dict.get('ID')),
        func_NICK(data_dict.get('NICK'))]

    # print(f'{func_ID(data_dict["ID"])}{func_NICK(data_dict["NICK"])}')

    result = list()
    for item in layout:
        result.append(f'{item}')
    print(''.join(result))
