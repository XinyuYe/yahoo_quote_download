# -*- coding: utf-8 -*-
from urllib import error
from yahoo_quote_download import yqd


def write_csv(ticker):
    """Load ticker to csv from 2015 to 2016."""
    f = open('./data/'+ticker+'.csv', 'w+')
    try:
        print(yqd.load_yahoo_quote(ticker, '20150102', '20160104'), file=f)
        print('Write Succeed')
    except error.HTTPError:
        print('<'+ticker+'> not found or HTTP cant resolve the token')
    f.close()


def read(filename):
    # Download quote for stocks
    file = open(filename, 'r')
    symbols = []
    for line in file:
        symbols.append(line[:-1])
    for symbol in symbols:
        print(symbol)
        write_csv(symbol)


if __name__ == '__main__':
    read('symbols.txt')
    # read('others.txt')
