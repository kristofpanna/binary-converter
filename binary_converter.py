#!/usr/bin/env python3
import sys


def binary_to_decimal(binary):
    d = sum(2**i for i, bit in enumerate(binary[::-1]) if bit == "1")
    return str(d)


def decimal_to_binary(decimal):
    if decimal == "0":
        return "0"

    dec = int(decimal)
    bin = ""
    while dec > 0:
        bin += str(dec % 2)
        dec = dec // 2
    return bin[::-1]


def print_table(*args):
    middle = " | ".join(args)
    line = "-" * (len(middle) + 2)
    print(f"/{line}\\")
    print(f"| {middle} |")
    print(f"\\{line}/")


def sign(number):
    """handle negative integers"""
    if number[0] == "-":
        sign = "-"
        number = number[1:]
    else:
        sign = ""
    return sign


system = sys.argv[2]
number = sys.argv[1]

sign = sign(number)

BINARY_BASE = "2"
DECIMAL_BASE = "10"

if system == BINARY_BASE:
    decimal = sign + binary_to_decimal(number)
    print_table(decimal, DECIMAL_BASE)
else:
    binary = sign + decimal_to_binary(number)
    print_table(binary, BINARY_BASE)


# This is a comment just to try pushing without password (using SSH)

