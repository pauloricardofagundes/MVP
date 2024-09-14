import os
from filesplit.split import Split

LINES_PER_FILE = 93_000  # see PEP515 for readable numeric literals 
filename = 'D:/Documentos/iCloud/iCloudDrive/Dev/credit_card_transactions.csv'
outdir = 'D:/Documentos/iCloud/iCloudDrive/Dev'  # to store split-files `myinput_1.txt` etc.

Split(filename, outdir).bylinecount(LINES_PER_FILE)