#!/usr/bin/env python

import smtplib
import easyimap
from pprint import pprint
import string
import re
import nlp

def remove_html(stri):
    pattern = ".https?://[A-Za-z0-9./,;{}()*&^<>%$#@!`~|=_':+?-]+"
    stri =  re.sub(pattern,"",stri)
    return stri

login = 'eltonp3103@gmail.com'
password = 'WoMZTXXxyjGGiN3luIO2goJV#ztq4HI4d00e$EjpElL^A86ERheYBkU1EN0d@cRv'
dict = {}

imapper = easyimap.connect('imap.gmail.com', login, password)

for mail_id in imapper.listids(limit=1):
    mail = imapper.mail(mail_id)
    new_string = mail.body.replace("\n"," ")
    new_string = new_string.replace("\r"," ")
    new_string = remove_html(new_string)
    dict[(mail.title, mail.from_addr)] = new_string
    print(dict[(mail.title, mail.from_addr)])
    print()
    print()
    nlp.sentiment_analyze(dict[(mail.title, mail.from_addr)])
    nlp.entities_analyze(dict[(mail.title, mail.from_addr)])
    nlp.syntax_analyze(dict[(mail.title, mail.from_addr)])
    nlp.entity_sentiment_analyze(dict[(mail.title, mail.from_addr)])
    nlp.classify_content(dict[(mail.title, mail.from_addr)])
