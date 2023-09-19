#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import inspect
import os

try:
    from secrets import choice
except:
    from random import SystemRandom


def generate(filenames, word_count, sep):
    words = set()
    for filename in filenames:
        with open(filename) as f:
            words = words.union([line.rstrip("\n") for line in f])
    words = list(words)

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
    parser.add_argument(
        "-l", "--large", action="store_true", help="Use EFF's general large wordlist"
    )
    parser.add_argument(
        "-s1", "--short1", action="store_true", help="Use EFF's general short wordlist"
    )
    parser.add_argument(
        "-s2",
        "--short2",
        action="store_true",
        help="Use EFF's short wordlist with unique prefixes",
    )
    parser.add_argument(
        "-got",
        "--game-of-thrones",
        action="store_true",
        help="Use EFF's Game of Thrones wordlist (Passwords of Westeros)",
    )
    parser.add_argument(
        "-hp",
        "--harry-potter",
        action="store_true",
        help="Use EFF's Harry Potter wordlist (Accio Passphrase!)",
    )
    parser.add_argument(
        "-st",
        "--star-trek",
        action="store_true",
        help="Use EFF's Star Trek wordlist (Live Long and Passphrase)",
    )
    parser.add_argument(
        "-sw",
        "--star-wars",
        action="store_true",
        help="Use EFF's Star Wars wordlist (The Passphrase Is Strong With This One)",
    )
    parser.add_argument(
        "-d",
        "--dictionary",
        nargs="?",
        metavar="dictionary",
        type=str,
        help="Path to custom wordlist file",
    )
    args = parser.parse_args()

    wordlists_path = os.path.join(
        os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))),
        "wordlists",
    )

    filenames = []
    if args.dictionary is not None:
        filenames.append(args.dictionary)
    if args.large:
        filenames.append(os.path.join(wordlists_path, "eff_large_wordlist.txt"))
    if args.short1:
        filenames.append(os.path.join(wordlists_path, "eff_short_wordlist_1.txt"))
    if args.short2:
        filenames.append(os.path.join(wordlists_path, "eff_short_wordlist_2_0.txt"))
    if args.game_of_thrones:
        filenames.append(os.path.join(wordlists_path, "gameofthrones-2018.txt"))
    if args.harry_potter:
        filenames.append(os.path.join(wordlists_path, "harrypotter-2018.txt"))
    if args.star_trek:
        filenames.append(os.path.join(wordlists_path, "startrek-2018.txt"))
    if args.star_wars:
        filenames.append(os.path.join(wordlists_path, "starwars-2018.txt"))
    if not filenames:
        filenames.append(os.path.join(wordlists_path, "eff_short_wordlist_1.txt"))

    passphrase = generate(filenames, args.word_count, args.sep)
    print(passphrase)


if __name__ == "__main__":
    main()
