#!/usr/bin/env python3
import sys


def binary_to_decimal(binary):
    return sum(2**i for i, bit in enumerate(binary[::-1]) if bit == "1")


def decimal_to_binary(decimal):
    dec = int(decimal)
    bin = ""
    while dec > 0:
        bin += str(dec % 2)
        dec = dec // 2
    return bin[::-1]


def print_table(*args):
    middle = " | ".join(map(str, args))
    line = "-" * (len(middle) + 2)
    print(f"/{line}\\")
    print(f"| {middle} |")
    print(f"\\{line}/")



system = sys.argv[2]
number = sys.argv[1]

if system == "2":
    decimal = binary_to_decimal(number)
    print_table(decimal, 10)
else:
    binary = decimal_to_binary(number)
    print_table(binary, 2)

