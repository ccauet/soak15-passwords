### Standard word list attack on md5 hashed hash list
```./hc hashes.txt wordlist.txt```

### Mask attack (Brute-force with pattern definition)
Searching for all words with at least 
```./hc -a3 --increment hashes.txt '?a?a?a?a'```
