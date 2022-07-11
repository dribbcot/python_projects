#!/usr/bin/env python3
#Quick scanner to see if you can login anonymously to an FTP server

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous')
        print('\n [+] ' + str(hostname) + ' FTP Anonymous Login Succeeded.')
        ftp.quit()
        return True
    except Exception:
        print('\n [-] ' + str(hostname) + ' FTP Anonymous Login Fails.')
        return False


if __name__ == '__main__':
    anonLogin('192.168.1.186')