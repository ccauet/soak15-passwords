#!/usr/bin/python
# -*- coding: utf-8 -*-

import getpass
import md5

hash_list = []
import_passwords = True

while import_passwords:
  hash1 = md5.new(getpass.getpass("Bitte ein Passwort eingeben: ")).hexdigest()
  hash2 = md5.new(getpass.getpass("Passwort bitte erneut eingeben: ")).hexdigest()

  if hash1 == hash2:
    print "Passwort-Hash erzeugt:", hash1, "\n"
    hash_list.append(hash1)
  else:
    print "Passwörter stimmen nicht überein!\n"  

  check = raw_input("Soll ein weiteres Passwort eingegeben werden? [y]/n: ") or "y"
  if check == "n":
    import_passwords = False

print "Liste der erzeugten Hashes:\n", hash_list

with open('hashes.txt', 'w') as hash_file:
  for h in hash_list:
    hash_file.write("%s\n" % h)

  hash_file.close()
