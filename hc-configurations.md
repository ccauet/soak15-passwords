### Standard word list attack on md5 hashed hash list

```./hc hashes.txt wordlist.txt```

## Mask attacks (Brute-force with pattern definition)
### with increment
Searching for all words with 4 or less characters 'a', where 'a' can be either of type lower case `?l`, upper case `?u`, digit `?d` or symbol `s`. 

```
./hc -a3 --increment hashes.txt '?a?a?a?a'
```

### hashes are given in hex

```
./hc -a3 --hex-charset hashes.txt '?a?a?a?a'
```

### recovered hashes are saved in file, no .pot file will be created

```
./hc -a3 --potfile-disable --outfile=recovered_hashes.txt --outfile-format=1 hashes.txt '?a?a?a?a'
```

### custom charset, multi-threaded

```
./hc -a3 --custom-charset1='?l?d' --threads=8 hashes.txt '?1?1?1?1?1'
```

