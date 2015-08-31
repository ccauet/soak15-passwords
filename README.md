# SoAk15 talk about password security (and example scripts)

Talk and resources about password security and common attack methods to guess password hashes. The talk was held at the [PeP et al. e.V.](http://pep-dortmund.org) Sommerakademie 2015 at Tschagguns, Austria.

*Disclaimer*: Everything is intended to be used for educational purposes only! I am no password security expert!

## PDF slides

The presentation slides can be found [here](/talk/passwords.pdf).

## Examples

More examples are listed in [hc-configurations.md](/hc-configurations.md)

## Software

To attack password hashes the [hashcat](https://hashcat.net/hashcat/) software was used. 

## How to proceed

1. brute force attack with full charset, only words with < 6 characters

```
./hc -a3 --increment --hex-charset --remove --potfile-disable --outfile=recovered_hashes.txt --outfile-format=1 hashes.txt '?a?a?a?a?a'
```

2. prepare word list

concatenate some popular dictionaries, remove duplicates, only words > 5 characters

```
cat *.txt | egrep '.{6,}' | sort -u -o words.txt
```

add some context specific words, e.g. names, local places, professional vocabulary.

3. dictionary attack with prepared word list

```
./hc -a0 --hex-charset --remove --potfile-disable --outfile=recovered_hashes.txt --outfile-format=1 hashes.txt words.txt
```

4. Let's see…