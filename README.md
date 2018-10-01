# passphraseme

A quick and simple cryptographically secure script to generate high entropy passphrases using [the Electronic Frontier Foundation's wordlists](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases), including their [fandom-inspired wordlists](https://www.eff.org/deeplinks/2018/08/dragon-con-diceware).

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

|                                | Bits of entropy/word | 1          | 2          | 3          | 4          | 5          | 6              | 7             | 8               | 9                 | 10                |
|--------------------------------|----------------------|------------|------------|------------|------------|------------|----------------|---------------|-----------------|-------------------|-------------------|
| EFF large wordlist (*default*) | 12.925               | 12.9 (0 s) | 25.8 (0 s) | 38.8 (0 s) | 51.7 (1 h) | 64.6 (1 y) | 77.5 (10.6k y) | 90.5 (82M y)  | 103.4 (642B y)  | 116.3 (4.99e15 y) | 129.2 (3.88e19 y) |
| EFF short wordlists            | 10.339               | 10.3 (0 s) | 20.7 (0 s) | 31.0 (0 s) | 41.4 (4 s) | 51.7 (1 h) | 62.0 (83 d)    | 72.4 (295 y)  | 82.7 (382.3k y) | 93.1 (495M y)     | 103.4 (642B y)    |
| EFF fandom wordlists           | 12.966               | 13.0 (0 s) | 25.9 (0 s) | 38.9 (0 s) | 51.9 (1 h) | 64.8 (1 y) | 77.8 (12.6k y) | 90.8 (100M y) | 103.7 (805B y)  | 116.7 (6.45e15 y) | 129.7 (5.16e19 y) |

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

Note that the time "5.16e19 y" means "5.16 x 10<sup>19</sup> years". Also note
that the brute force times will vary wildly, both much quicker or much slower,
depending on the hash function or [KDF](https://en.wikipedia.org/wiki/Key_derivation_function)
used -- basically, depending on what software you're using this passphrase with.

## Licenses

The wordlists included were created by Electronic Frontier Foundation, and are
distributed under the Creative Commons Attribution 3.0. For the fandom wordlists
(Game of Thrones, Harry Potter, Star Trek, and Star Wars), EFF notes that "Any
trademarks within the word list are the property of their respective trademark
holders, who are not affiliated with the Electronic Frontier Foundation and do
not sponsor or endorse these passwords."
