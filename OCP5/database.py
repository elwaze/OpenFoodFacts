#! /usr/bin env python3
# coding: utf-8

import records

db = records.Database('mysql://root:@localhost:3306/OFF')

# var d'environnement pour ne pas écrire mon mdp en clair.
# => "mysql://username:{}@hostname:port/table".format(os.environ.get('P5_MYSQL_PASSWORD')
