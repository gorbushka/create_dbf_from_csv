#!/usr/bin/python
# -*- coding: cp1251 -*-
import os, sys, csv
from dbfpy import dbf

SCHEMA = (
    ("LS",    "C", 16   ),
    ("NAME",  "C", 64   ),
    ("NUMD",  "C", 16   ),
    ("VALUE", "N", 15, 2),

)

db = dbf.Dbf("dbfile.dbf", new=True)
db.addField(*SCHEMA)
#rec = db.newRecord()
#rec["LS"] = "asds"
#rec["NAME"] = "ываываsdfsdagsdgsdfgsdfgdfgsdfgваываываыва"
#rec["NUMD"] = "2342342342"
#rec["VALUE"] = 123
#rec.store()

with open('list.csv', 'rb') as csvfile:
    mlist = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in mlist:
        rec = db.newRecord()
        rec["LS"] = row[0]
        rec["NAME"] = row[1].decode("utf-8").encode("cp1251")
        rec["NUMD"] = row[2]
        rec["VALUE"] = float(row[3])
        rec.store()


#for mstring in mlist:
#    rec = db.newRecord()
#    rec["LS"] = payment.account
#    rec["NAME"] = payment.first_name.decode("cp866")
#    rec["NUMD"] = payment.date
#    rec["VALUE"] = payment.date
#    rec.store()

db.close()


db = dbf.Dbf("dbfile.dbf")
for rec in db:
    print rec
print