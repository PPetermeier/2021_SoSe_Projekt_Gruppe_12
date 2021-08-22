import pymongo
import urllib


username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('uafh5S/zNxHW')

conn_str = ('mongodb://%s:%s@192.168.178.42' % (username, password))

client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)