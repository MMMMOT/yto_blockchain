from ftplib import FTP

#host = '112.65.156.58'
#username = 'nanyouuser1'
#password = 'Ny888'

def ftpconnect(host, username, password):
    # 建立ftp连接
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

def downloadfile(ftp, remotepath, localpath):
    # 从ftp下载文件
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

if __name__ == "__main__":
    ftp = ftpconnect("112.65.156.58", "nanyouuser1", "Ny888")
    remotep = "/xmachine/000000001/20181017_145812_001.JPG"
    localp = "E:/mygit/yto/yto_V2.0(li)/image/20181017_145812_001.JPG"
    downloadfile(ftp, remotep,localp)

    ftp.quit()