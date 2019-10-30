#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import math
import sys

try:
    from terminaltables import AsciiTable
except:
    print("You need the terminaltables module to run this script. Install with pip:")
    print("pip install terminaltables")
    sys.exit()


def seconds_to_printable(seconds):
    seconds = math.floor(seconds)
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365

    if years == 0 and days == 0 and hours == 0 and minutes == 0:
        return "{0} s".format(seconds)
    elif years == 0 and days == 0 and hours == 0:
        return "{0} m".format(minutes)
    elif years == 0 and days == 0:
        return "{0} h".format(hours)
    elif years == 0:
        return "{0} d".format(days)
    elif years < 1000:
        return "{0} y".format(years)
    elif years < 1000000:
        return "{0:.1f}k y".format(years / 1000)
    elif years < 1000000000:
        return "{0}M y".format(math.floor(years / 1000000))
    elif years < 1000000000000:
        return "{0}B y".format(math.floor(years / 1000000000))
    else:
        return "{0:.2e} y".format(years)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "size", metavar="size", type=int, help="Number of words in wordlist"
    )
    args = parser.parse_args()

    # Here's what we know
    wordlist_size = args.size
    entropy_per_word = math.log(wordlist_size, 2)
    aws_guesses_per_second_per_instance = 193900
    aws_instance_cost_per_hour = 24.48
    aws_instance_cost_per_day = aws_instance_cost_per_hour * 24
    attacker_budget_per_day = 1000000000
    total_aws_instances = math.floor(
        attacker_budget_per_day / aws_instance_cost_per_day
    )
    total_aws_guesses_per_second = (
        aws_guesses_per_second_per_instance * total_aws_instances
    )

    # Display these details
    print("Number of words: {}".format(wordlist_size))
    print("Entropy per word: {}".format(entropy_per_word))
    print(
        "Each AWS instance has this many guesses per second: {}".format(
            aws_guesses_per_second_per_instance
        )
    )
    print("Attacker can afford this many AWS instances: {}".format(total_aws_instances))
    print(
        "Attacker's total guesses per second: {}".format(total_aws_guesses_per_second)
    )
    print("")

    # Build the passphrase strength table
    row_num_words = ["Number of words"]
    row_entropy = ["Entropy"]
    row_time = ["Average time"]
    for num_words in range(1, 11):
        entropy = num_words * entropy_per_word
        total_keyspace = wordlist_size ** num_words
        time_seconds = total_keyspace / total_aws_guesses_per_second
        avg_time_seconds = (
            time_seconds / 2
        )  # attacks have to search half the keyspace on average

        row_num_words.append("{0}".format(num_words))
        row_entropy.append("{0:.1f}".format(num_words * entropy_per_word))
        row_time.append(seconds_to_printable(avg_time_seconds))

    table_data = [row_num_words, row_entropy, row_time]
    table = AsciiTable(table_data)

    print("Passphrase strength table:")
    print(table.table)


if __name__ == "__main__":
    main()
