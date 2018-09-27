# PassphraseMe

A quick and simple cryptographically secure script to generate high entropy passphrases using [the Electronic Frontier Foundation's wordlists](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases).

## Usage

```sh
$ passphraseme 7
banana stopwatch appealing germinate survival retired comma
$ passphraseme 5
borrower harvest stature entity blimp
```

## Installation

_TODO: Upload to PyPI. Then the instructions will just be to install with pip3._

## Strength of passphrases

This table shows the strength (bits of entropy) of `passphraseme`-generated passphrases of different lengths (1-10 words).

|                                | Bits of entropy/word | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8     | 9     | 10  |
|--------------------------------|----------------------|------|------|------|------|------|------|------|-------|-------|-----|
| EFF large wordlist (*default*) | 12.9                 | 12.9 | 25.8 | 38.7 | 51.6 | 64.5 | 77.4 | 90.3 | 103.2 | 116.1 | 129 |
| EFF short wordlists            | 10.3                 | 10.3 | 20.6 | 30.9 | 41.2 | 51.5 | 61.8 | 72.1 | 82.4  | 92.7  | 103 |
