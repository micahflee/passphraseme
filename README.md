# passphraseme

A quick and simple cryptographically secure script to generate high entropy passphrases using [the Electronic Frontier Foundation's wordlists](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases).

## Installation

```sh
pip3 install passphraseme
```

## Usage

Run `passphraseme` with a number to generate secure passphrases, like this:

```
$ passphraseme 7
banana stopwatch appealing germinate survival retired comma
$ passphraseme 5
borrower harvest stature entity blimp
```

By default, `passphraseme` uses EFF's long wordlist. But optionally, you can choose
to use one of EFF's two short wordlists, like this:

```
$ passphraseme -s1 5
glide canal flag sage those
$ passphraseme -s2 5
optical anonymous nirvana agitate feudalist
```

You can also choose to use a custom wordlist, like this:

```
$ passphraseme -d /usr/share/dict/words 7
leading's Oz's caesareans lactate eloped interposed wowed
```

## Strength of passphrases

This table shows the strength (bits of entropy) of `passphraseme`-generated passphrases of different lengths (1-10 words).

|                                | Bits of entropy/word | 1          | 2          | 3          | 4           | 5            | 6             | 7            | 8              | 9                | 10             |
|--------------------------------|----------------------|------------|------------|------------|-------------|--------------|---------------|--------------|----------------|------------------|----------------|
| EFF large wordlist (*default*) | 12.9                 | 12.9 (0 s) | 25.8 (0 s) | 38.7 (1 s) | 51.6 (86 m) | 64.5 (1.2 y) | 77.4 (9.5k y) | 90.3 (73M y) | 103.2 (560B y) | 116.1 (4.2e15 y) | 129 (3.2e19 y) |
| EFF short wordlists            | 10.3                 | 10.3 (0 s) | 20.6 (0 s) | 30.9 (0 s) | 41.2 (4 s)  | 51.5 (80 m)  | 61.8 (70 d)   | 72.1 (243 y) | 82.4 (306k y)  | 92.7 (386M y)    | 103 (4.8e11 y) |

The brute force time is calculated like this:

I'm assuming you're using a passphrase for macOS 10.8+ (PBKDF2-SHA512) to
encrypt your disk with FileVault. According to [this post](https://medium.com/@iraklis/running-hashcat-v4-0-0-in-amazons-aws-new-p3-16xlarge-instance-e8fab4541e9b),
the password cracking tool [hashcat](https://hashcat.net/hashcat/) can guess
193,900 passphrases per second on an Amazon AWS p3.16xlarge instance, which
costs $24.48 per hour.

If an attacker is willing to spend up to $1 billion per day to guess your
passphrase, they can afford to run 1.7 million of these AWS instances at once,
meaning they can guess ~330 billion passphrases per second. On average, a brute
force attack will find the passphrase after searching half the keyspace, so the
times above are how long it takes to search half the keyspace.

Note that the time "3.2e19 y" means "3.2 x 10<sup>19</sup> years". Also note
that the brute force times will vary wildly, both much quicker or much slower,
depending on the hash function or [KDF](https://en.wikipedia.org/wiki/Key_derivation_function)
used -- basically, depending on what software you're using this passphrase with.
