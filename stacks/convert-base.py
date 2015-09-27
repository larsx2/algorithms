#!/usr/bin/env python

import string

def convert(n, base=2):
    alphabet = string.hexdigits
    stack = []

    while n:
        stack.append(n % base)
        n /= base

    return "".join([
        alphabet[stack.pop()]
        for idx in xrange(len(stack))
    ])

if __name__ == "__main__":

    params = {
        2: {
            4: "100",
            9: "1001"
        },
        8: {
            8: "10",
            25: "31"
        },
        16: {
            16: "10",
            5002: "138a"
        }
    }

    for base, values in params.iteritems():
        for param, result in values.iteritems():
            assert(convert(param, base=base) == result)
