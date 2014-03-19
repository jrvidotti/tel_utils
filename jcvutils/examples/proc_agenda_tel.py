#!/usr/bin/env python
# coding: utf-8
import sys
import getopt
from jcvutils.telutils import PhoneNumber

def main():
    f = open('teste-agenda.csv')

    head = ['First Name','E-mail Address','Mobile Phone','Primary Phone','Home Phone','Home Phone 2','Company Main Phone','Business Phone','Business Phone 2']
    print '"'+'","'.join(head)+'"'

    next(f)
    for line in f:
        l = line.replace('\r','').replace('\n','').split(';')
        ld = {'nome': l[0], 'tel': l[1:6], 'email': l[6], 'tel cel': [], 'tel fixo': [], 'tel err': []}
        for tel in ld['tel']:
            if tel != '':
                pn = PhoneNumber(tel, '65')
                if pn.number:
                    if pn.type() == 'celular':
                        ld['tel cel'] += [pn.number]
                    else:
                        ld['tel fixo'] += [pn.number]
                else:
                    ld['tel err'] += [pn.original_number]

        if ld['tel err']:
            print u'*** Numeros incorretos ***'
            print ld['nome'], ld['tel err']

        lst = ld['tel cel'] + ld['tel fixo']
        lst = lst + [''] * (7 - len(lst))
        print '"'+'","'.join([ld['nome'], ld['email']] + lst)+'"'

if __name__ == "__main__":
    sys.exit(main())

