#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import inspect
import os

try:
    from secrets import choice
except:
    from random import SystemRandom


def generate(filename, word_count, sep):
    with open(filename) as f:
        words = [line.rstrip("\n") for line in f]

    try:
        return sep.join(choice(words) for _ in range(word_count))
    except:
        return sep.join(SystemRandom().sample(words, word_count))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "word_count",
        metavar="word_count",
        nargs="?",
        const=1,
        default=7,
        type=int,
        help="Word count",
    )
    parser.add_argument(
        "--sep",
        metavar="sep",
        nargs="?",
        const=1,
        default="-",
        type=str,
        help="Separator",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-l", "--large", action="store_true", help="Use EFF's general large wordlist"
    )
    group.add_argument(
        "-s1", "--short1", action="store_true", help="Use EFF's general short wordlist"
    )
    group.add_argument(
        "-s2",
        "--short2",
        action="store_true",
        help="Use EFF's short wordlist with unique prefixes",
    )
    group.add_argument(
        "-got",
        "--game-of-thrones",
        action="store_true",
        help="Use EFF's Game of Thrones wordlist (Passwords of Westeros)",
    )
    group.add_argument(
        "-hp",
        "--harry-potter",
        action="store_true",
        help="Use EFF's Harry Potter wordlist (Accio Passphrase!)",
    )
    group.add_argument(
        "-st",
        "--star-trek",
        action="store_true",
        help="Use EFF's Star Trek wordlist (Live Long and Passphrase)",
    )
    group.add_argument(
        "-sw",
        "--star-wars",
        action="store_true",
        help="Use EFF's Star Wars wordlist (The Passphrase Is Strong With This One)",
    )
    group.add_argument(
        "-d",
        "--dictionary",
        nargs="?",
        metavar="dictionary",
        type=argparse.FileType("r"),
        help="Custom wordlist filename",
    )
    args = parser.parse_args()

    if args.dictionary is not None:
        filename = args.dictionary.name
    else:
        wordlists_path = os.path.join(
            os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),
            "wordlists",
        )

        if args.large:
            filename = os.path.join(wordlists_path, "eff_large_wordlist.txt")
        if args.short1:
            filename = os.path.join(wordlists_path, "eff_short_wordlist_1.txt")
        elif args.short2:
            filename = os.path.join(wordlists_path, "eff_short_wordlist_2_0.txt")
        elif args.game_of_thrones:
            filename = os.path.join(wordlists_path, "gameofthrones-2018.txt")
        elif args.harry_potter:
            filename = os.path.join(wordlists_path, "harrypotter-2018.txt")
        elif args.star_trek:
            filename = os.path.join(wordlists_path, "startrek-2018.txt")
        elif args.star_wars:
            filename = os.path.join(wordlists_path, "starwars-2018.txt")
        else:
            filename = os.path.join(wordlists_path, "eff_short_wordlist_1.txt")

    passphrase = generate(filename, args.word_count, args.sep)
    print(passphrase)


if __name__ == "__main__":
    main()
