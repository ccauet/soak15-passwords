#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Checks if a given password matches with a list of md5 password hashes

This script is intended to be used for educational purposes only!

Author: Christophe Cauet
Date:   2015-07-29
Email:  contact@christophe.cauet.de
"""

import getpass
import md5

hash_list = []
check_passwords = True

# read hashes from file
with open('hashes.txt') as hash_file:
        for line in hash_file:
          hash_list.append(line.rstrip())

# while loop to check for hashes in file
while check_passwords:
  hash1 = md5.new(getpass.getpass("Bitte ein Passwort eingeben: ")).hexdigest()
  hash2 = md5.new(getpass.getpass("Passwort bitte erneut eingeben: ")).hexdigest()

  # check if user entered password correctly
  if hash1 == hash2:
    # print "Passwort-Hash erzeugt:", hash1, "\n"

    # check if hash is found in file
    if hash1 in hash_list:
      print "\nDas Passwort wurde gefunden!\n"
    else:
      print "\nDas Passwort wurde NICHT gefunden!\n"

  else:
    print "Passwörter stimmen nicht überein!\n"  

  check = raw_input("Soll ein weiteres Passwort abgefragt werden? [y]/n: ") or "y"
  if check == "n":
    check_passwords = False