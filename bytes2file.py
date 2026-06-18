

filer = open('fileread','r')
filew = open('filewrite','wb')


def bytes2file():
    list = filer.readlines()
    data = []
    count = 0

    for i in list:
        # deal with data
        data = i
        data = bytes.fromhex(data)
        filew.write(data)
        count += 1
