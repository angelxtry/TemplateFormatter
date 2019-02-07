"""
주어진 format에 맞춰 문자열을 생성하는 함수를 생성
"""


def string_maker(length=0, align='LEFT', padding=''):
    """
    param으로 받은 length, align, padding으로 문자열 format을 설정
    """
    ALIGN_SIGN = {
        'LEFT': '',
        'RIGHT': '>',
        'MID': '^',
    }

    def wrapper(data):
        return "{:{padding}{align}{len}}".format(
            data[:length],
            padding=padding,
            align=ALIGN_SIGN.get(align),
            len=length)
    return wrapper


def number_maker(length=0, align='RIGHT', padding='', precision=0):
    """
    param으로 받은 length, align, padding, precision으로 문자열 format을 설정
    """
    ALIGN_SIGN = {
        'LEFT': '<',
        'RIGHT': '',
        'MID': '^',
    }

    def wrapper(data):
        text = "{:{align}{padding}{len}.{precision}f}".format(
            data,
            padding=padding,
            align=ALIGN_SIGN.get(align),
            len=length,
            precision=precision)
        return text[:length]
    return wrapper



if __name__ == '__main__':
    data_sample = {
        'NAME': 'ABC',
        'NICK': 'DUCK',
    }

    name = string_maker(length=13)
    nick = string_maker(length=20, align='MID', padding='*')
    layout = [name(data_sample.get('NAME')), nick(data_sample.get('NICK'))]

    print(''.join([f'{item}' for item in layout]))

    text_length_10 = number_maker(length=10)
    print(text_length_10(1234567890123))

    float_last_zero = number_maker(length=10, padding='0', precision=3)
    print(float_last_zero(12345.1))
