import json
from pprint import pprint

import text_formatter


def load_format(json_file_name):
    with open(json_file_name) as json_file:
        format = json.load(json_file)
    return format

# def make_template(format_datas):
#     if format_datas['TYEP'] == 'STRING':
#         return make_string_template(format_datas)
#     if format_datas['TYEP'] == 'NUMBER':
#         return make_number_template(format_datas)

# def make_string_template(format_datas):
#     pass

# def string_router(data_name, data_attrs):
#     router = {
#         "ID": func_ID(data_attrs),
#         "PRICE_A": func_PRICE_A(data_attrs),
#     }
#     return router[data_name]


if __name__ == '__main__':
    # pprint(load_format('format_abc.json'))
    format_abc = load_format('format_abc.json')

    # pprint(format_abc['DEFAULT'])

    top_level_keys = [key for key in format_abc.keys()]
    # print(top_level_keys)

    default_id_list = []

    for top_level_key in top_level_keys:
        for item_dict in format_abc[top_level_key]:
            print(item_dict)
            # for key, items in default_dict.items():
            #     # print(key)
            #     default_id_list.append(key)

    # print(default_id_list)

