import os
import sys
import json
import urllib.request as urllib2

access_token = ''
base = "https://api.vk.com/method/"

def comp(arg, val):
    arg = list(map(lambda x: str(urllib2.quote(str(x)).encode("utf8")), arg))
    val = list(map(lambda x: str(urllib2.quote(str(x)).encode("utf8")), val))
    return '&'.join(list(map('='.join, list(zip(arg, val)))))

def req(method, args =[], vals=[]):
    return json.loads(urllib2.urlopen(base+method+"?"+comp(args, vals)+"&access_token="+access_token+"&v=5.92").read())

p = req("messages.getConversations", ["offset"], ["0"])
