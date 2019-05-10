#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

__gmail__ = '4m3s0k0.shichan@gmail.com'
__author__ = 'kira@-天底.ガジ'
__version__ = 1.1

Default = namedtuple('Default', [
    'none', 'dot', 'space', 'new', 'start', 'end',
    'c_end', 'c_blue', 'c_purple', 'c_vermelho',
    'author', 'lie', 'hope', 'feith', 'love', 'luck'

])
default = Default(
    '', '.', ' ', '\n', 11, 30,
    '\033[0m', '\033[94m', '\033[35m', '\033[31m',
    __author__, '言葉無限欺', '希信', '信仰', '愛', '運'
)
