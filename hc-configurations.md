### Standard word list attack on md5 hashed hash list

```./hc hashes.txt wordlist.txt```

### Mask attack (Brute-force with pattern definition)
Searching for all words with 4 or less characters 'a', where 'a' can be either of type lower case, upper case, digit or symbol. 

```
./hc -a3 --increment hashes.txt '?a?a?a?a'
```

### Mask attack where hashes are given in hex (see above)

```
./hc -a3 --hex-charset --increment hashes.txt '?a?a?a?a'
```

