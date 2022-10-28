#! /usr/bin/python3

import configparser
from distutils.log import error
import os
import getpass
import sys

# screen cleaner
os.system('cls')

# load variables from config files
config = configparser.RawConfigParser()
#config.read('/tmp/ldap-searchlight/config/searchlight.conf')
config.read('C:\GitHub\Python\LINUX\ldap-searchlight\config\searchlight.conf')

# VARIABLES
user1_name = config['USERS']['user1-name']
ldap_user1 = config['USERS']['ldap-user1']

user2_name = config['USERS']['user2-name']
ldap_user2 = config['USERS']['ldap-user2']

ldap_base_dn = config['GLOBAL']['ldap-base-dn']

# login & password input
input_name = input("Podaj imie i nazwisko:\n")
if input_name == user1_name:
    name = user1_name
    password = getpass.getpass()
elif input_name == user2_name:
    name = user2_name
    password = getpass.getpass()
else:
    print("Permission Danied")
    sys.exit(1)


LDAP_HOST = config['GLOBAL']['ldap-host']


print(LDAP_HOST)