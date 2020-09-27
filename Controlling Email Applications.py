# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 15:36:04 2020

@author: PranavM
"""

import smtplib
conn=smtplib.SMTP('smtp.gmail.com', 587)
conn
conn.ehlo()
conn.starttls()
conn.login('pranav.v.mayekar@gmail.com', 'G@@gleStealsD^t^')
conn.sendmail(from_addr, to_addrs, msg)