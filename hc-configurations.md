### Standard word list attack on md5 hashed hash list

```./hc hashes.txt wordlist.txt```

### Mask attack (Brute-force with pattern definition)
Searching for all words with 4 or less characters 'a', where 'a' can be either of type lower case, upper case, digit or symbol. 

```
./hc -a3 --increment hashes.txt '?a?a?a?a'
```

### Mask attack (see above) where hashes are given in hex

```
./hc -a3 --hex-charset --increment hashes.txt '?a?a?a?a'
```

### Mask attack (see above), recovered hashes are saved in file, no .pot file will be created

```
./hc -a3 --hex-charset --increment --potfile-disable --outfile=recovered_hashes.txt --outfile-format=1 hashes.txt '?a?a?a?a'
```