"""
주어진 format에 맞춰 문자열을 생성하는 함수를 생성
"""


def number_maker(length=0, align='RIGHT', padding='', precision=0):
    """
    param으로 받은 length, align, padding으로 문자열 format을 설정
    """
    ALIGN_SIGN = {
        'LEFT': '<',
        'RIGHT': '',
        'MID': '^',
    }

    def wrapper(data):
        return "{:{align}{padding}{len}.{precision}f}".format(
            data,
            padding=padding,
            align=ALIGN_SIGN.get(align),
            len=length,
            precision=precision)
    return wrapper


if __name__ == '__main__':
    data_sample = {
        'PRICE1': 10002,
        'PRICE2': 123.123,
    }

    price1 = number_maker(length=10)
    price2 = number_maker(length=10, align='LEFT')
    price3 = number_maker(length=10, align='RIGHT', padding='0')
    price4 = number_maker(length=20, align='RIGHT', precision=5)
    layout = [
        price1(data_sample.get('PRICE1')),
        price2(data_sample.get('PRICE1')),
        price3(data_sample.get('PRICE1')),
        price4(data_sample.get('PRICE1')),
        ]

    print(''.join([f'{item}' for item in layout]))
