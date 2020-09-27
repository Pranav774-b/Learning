# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:40:04 2020

@author: PranavM
"""

import PyPDF2
import os
pdfFile=open(r'C:\Users\PranavM\OneDrive\upsc\GS\economic survey 2016-17.pdf','rb')
reader=PyPDF2.PdfFileReader(pdfFile)
reader.numPages
page=reader.getPage(20)
page.extractText()
