#!/usr/bin/env python
#coding: utf8

class FooBar(object):
    def __init__(self, value=43):
        self.somevar = value



if __name__ == '__main__':
    f = FooBar('This is a class test!')
    print f.somevar
