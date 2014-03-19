# coding: utf-8
import re

class PhoneNumber(object):
    '''
    PhoneNumber é usado para tratar números telefonicos.

    PhoneNumber(number, ddd_default):
        number: número do telefone sem formatação
        ddd_default: DDD padrão para preenchimento
    
    PhoneNumber.number:
        Número já formatado

    PhoneNumber.type():
        Tipo do número ('celular' ou 'fixo')
    '''

    DDI_DEFAULT = '55'

    def __init__(self, number, ddd_default):
        super(PhoneNumber, self).__init__()
        self.number = number
        self.original_number = number
        self.ddd_default = ddd_default
        self.clean()

    def __put_mask(self, number):
        num = number
        if len(num) == 11:
            return '(' + num[0:3] + ') ' + num[3:7] + '-' + num[7:12]
        if len(num) == 12:
            return '(' + num[0:3] + ') ' + num[3:8] + '-' + num[8:13]
        if num[0] == '1' and (len(num) == 3 or len(num) == 5):
            return num

    def clean(self):
        num = self.original_number.strip()
        if num == '':
            return ''
        if num[0:2] == '00' and len(num) >= 10:
            num = '+' + num[2:]
        if num[0:3] == '+' + self.DDI_DEFAULT:
            num = num.replace('+' + self.DDI_DEFAULT, '0')
        if num[0] == '+':
            self.number = num
        else:
            num = re.sub('[^0-9]', '', str(num))
            if num[0] == '9' and len(num) in (12,13):
                num = num[1:]
            if len(num) == 8:
                num = '0' + self.ddd_default + num
            if num[0] in ['3','6'] and len(num) == 7:
                num = '0' + self.ddd_default + '3' + num
            if len(num) == 10:
                num = '0' + num
            if num[0] != '0' and len(num) == 11:
                num = '0' + num
            if num[0] == '0' and len(num) == 13:
                num = num[0] + num[3:]
            if num[1:3] == '11' and num[3] in ['8','9'] and len(num) == 11:
                num = num[0:3] + '9' + num[3:13]
            self.number = self.__put_mask(num)
        return self.number

    def type(self):
        if self.clean():
            if self.number[6] in ['2','3','4','5']:
                return 'fixo'
            if self.number[6] in ['6','7','8','9']:
                return 'celular'

    def operator(self):
        pass



