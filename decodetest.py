from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.parse
import time
import datetime
import sys
import traceback
import readfile


args = sys.argv
file_words = "words_" + str(args[1]) +".txt"
file_words = "words_" + '3' +".txt"
words = readfile.readWords( file_words )

for word in words:
    print(urllib.parse.unquote(word))
