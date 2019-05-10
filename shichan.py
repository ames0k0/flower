#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

from config import default as d
from random import randint
from pickle import load


def flower(simp):
    '''Moving flower (*f_template) to the center
    '''
    result = d.none

    for each in simp.split(d.new)[1:]:
        if each:
            s_n_d = randint(d.start, d.end)
            each = f"{d.space * (d.end - s_n_d)}{d.dot * s_n_d}{each}{d.new}"
        result += each

    return d.new.join((simp.split(d.new, maxsplit=1)[0], result))


if __name__ == "__main__":
    with open('f_template.pkl', 'rb') as f:
        print(flower(load(f)).format(
            d.c_vermelho, d.c_purple, d.c_blue, d.c_end,
            d.author, d.hope, d.feith, d.love, d.luck, d.lie
        ))
