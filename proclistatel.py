# coding: utf-8
import sys
import getopt
#from tel_utils import tel_clean

def main(argv=None):
    if argv is None:
        argv = sys.argv

    f = open(argv[1])
    arr = []

    for line in f:
        line = line.replace('\r','').replace('\n','')
        reg = [line.split(';')[0:7]]
        arr += reg

    for x in arr:
        print x

if __name__ == "__main__":
    sys.exit(main())

