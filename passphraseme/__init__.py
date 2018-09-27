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
    parser.add_argument('-s1', '--short1', action="store_true", help="Use EFF's general short wordlist")
    parser.add_argument('-s2', '--short2', action="store_true", help="Use EFF's short wordlist with unique prefixes")
    parser.add_argument('-d', '--dictionary', nargs='?', metavar='dictionary', help='Custom wordlist filename')
    args = parser.parse_args()

    if args.dictionary is not None:
        filename = args.dictionary
    else:
        wordlists_path = os.path.join(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))), 'wordlists')

        if args.short1 and args.short2:
            print("Select only one wordlist")
            sys.exit()

        if args.short1:
            filename = os.path.join(wordlists_path, 'eff_short_wordlist_1.txt')
        elif args.short2:
            filename = os.path.join(wordlists_path, 'eff_short_wordlist_2_0.txt')
        else:
            filename = os.path.join(wordlists_path, 'eff_large_wordlist.txt')

    if not args.word_count.isdigit():
        print("Please input a valid number.")
        sys.exit()

    passphrase = generate(filename, int(args.word_count))
    print(passphrase)


if __name__ == '__main__':
    main()
