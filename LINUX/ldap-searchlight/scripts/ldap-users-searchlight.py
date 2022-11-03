#! /usr/bin/python3

import configparser
import os
import getpass
import sys
import ssl
from ldap3 import Server, Connection, Tls, ALL_ATTRIBUTES
import json

# screen cleaner
os.system('cls')

# load variables from config files
config = configparser.RawConfigParser()
config.read('/tmp/ldap-searchlight/config/searchlight.conf')
ldap_base_dn = config['GLOBAL']['ldap_base_dn']
user1_name = config['USERS']['user1_name']
user2_name = config['USERS']['user2_name']
ldap_users_dn = config['USERS']['ldap_users_dn']

# user's choice
print(
    "Sing in as:\n" +
    "[ 1 ] for " + user1_name + "\n" +
    "[ 2 ] for " + user2_name + "\n"
)
input_value = input("Select the user's number:")
if input_value == "1":
    user = config['USERS']['ldap_user1']
elif input_value == "2":
    user = config['USERS']['ldap_user1']
else:
    print("PERMISSION DANIED\n")
    sys.exit(1)

# getting password
password = getpass.getpass()

# LDAP
# ldap variables
LDAP_HOST = config['GLOBAL']['ldap-host']
LDAP_BASE_DN = ldap_users +","+ ldap_base_dn
LDAP_USER = user +","+ ldap_users +","+ ldap_base_dn
LDAP_PASSWORD = password
LDAP_OBJECT_FILTER = '(objectclass=user)'
tls_configuration = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1)
# users attributes list
user_attr_list=[ \
    'cn', \
    'givenName', \
    'instanceType', \
    'whenCreated', \
    'displayName', \
    'uSNCreated', \
    'name', \
    'objectGUID', \
    'badPwdCount', \
    'codePage', \
    'countryCode', \
    'badPasswordTime', \
    'lastLogoff', \
    'lastLogon',\
    'primaryGroupID', \
    'objectSid', \
    'accountExpires', \
    'logonCount', \
    'sAMAccountName', \
    'sAMAccountType', \
    'userPrincipalName', \
    'objectCategory', \
    'pwdLastSet', \
    'userAccountControl', \
    'lastLogonTimestamp', \
    'whenChanged', \
    'uSNChanged', \
    'memberOf', \
    'distinguishedName' ]

# connecting to the domain controller
def ldap_server():
    return Server(LDAP_HOST,
                  use_ssl=True,
                  tls=tls_configuration,
                  get_info=ALL_ATTRIBUTES)

def ldap_connection():
    server = ldap_server(), 
    return Connection(server, user=LDAP_USER,
                      password=LDAP_PASSWORD,
                      auto_bind=True)

conn = ldap_connection()
conn.search(LDAP_BASE_DN, LDAP_OBJECT_FILTER, attributes=user_attr_list)

# output to json file
json_file_path = '/tmp/ldap-searchlight/data/ldap_users.json'
data = json.loads(conn.response_to_json())
with open(json_file_path, 'w') as jsonfile:
    json.dump(data, jsonfile)

# end
print("SUCCES, data saved in: " + json_file_path)