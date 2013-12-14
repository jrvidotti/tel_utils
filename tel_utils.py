# coding: utf-8
import re

def tel_clean(numero, ddd_padrao):
    def put_mask_tel(num):
        if len(num) == 11:
            return '(' + num[0:3] + ') ' + num[3:7] + '-' + num[7:12]
        if len(num) == 12:
            return '(' + num[0:3] + ') ' + num[3:8] + '-' + num[8:13]
        if num[0] == '1' and (len(num) == 3 or len(num) == 5):
            return num

    num = numero.strip()
    if num[0:2] == '00' and len(num) >= 10:
        num = '+' + num[2:]
    if num[0:3] == '+55':
        num = num.replace('+55','0')
    if num[0] == '+':
        return num
    num = re.sub('[^0-9]', '', str(num))
    if num[0] == '9' and len(num) in (12,13):
        num = num[1:]
    if len(num) == 8:
        num = '0' + ddd_padrao + num
    if len(num) == 10:
        num = '0' + num
    if num[0] != '0' and len(num) == 11:
        num = '0' + num
    if num[1:3] == '11' and num[3] in ['8','9'] and len(num) == 11:
        num = num[0:3] + '9' + num[3:13]

    return put_mask_tel(num)

def tel_operator(numero, ddd_padrao):
    pass


'''

import formata_tel
formata_tel.formata('999647493','65')

'''