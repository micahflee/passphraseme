#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import sys
import os
import inspect
from secrets import choice


def generate(filename, word_count=7):
    try:
        with open(filename) as f:
            words = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print("The wordlist filename doesn't exist.")
        sys.exit()

    return ' '.join(choice(words) for _ in range(word_count))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('word_count', metavar='word_count', default=7, help='Word count')
    parser.add_argument('-d', '--dictionary', nargs='?', metavar='dictionary', help='Dictionary file')
    args = parser.parse_args()

    if args.dictionary is not None:
        filename = args.dictionary
    else:
        wordlists_path = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), 'wordlists')
        filename = os.path.join(wordlists_path, 'eff_large_wordlist.txt')

    if not args.word_count.isdigit():
        print("Please input a valid number.")
        sys.exit()

    passphrase = generate(filename, int(args.word_count))
    print(passphrase)


if __name__ == '__main__':
    main()
