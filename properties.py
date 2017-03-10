#!/usr/bin/python3


class PropClass:
    def __init__(self, val = 0):
        self._myval = val

    def get_myvalue(self):
        print("Getting value")
        return self._myval

    def set_myvalue(self, val):
        print("Setting value")
        self._myval = val

    myvalue = property(get_myvalue, set_myvalue)


if __name__ == '__main__':

    one_val = PropClass(12)
    print("printing one_val.myvalue : %s" % one_val.myvalue)
    print("setting one_val.myvalue")
    one_val.myvalue = 10
    print("printing one_val.myvalue : %s" % one_val.myvalue)
