# -*- coding: utf-8 -*-
import sqlite3
'''
GBK   UNIC  UTF-8
B8A3  798F  E7 A6 8F  福
D6DD  5DDE  E5 B7 9E  州
'''

con = sqlite3.connect("test.db")
# con = sqlite3.connect("D:\\text_factory1.db3")
# con.executescript('PRAGMA encoding = "UTF-16";')
cur = con.cursor()


a_text      = "Fu Zhou"
gb_text     = "\xB8\xA3\xD6\xDD"
utf8_text   = "\xE7\xA6\x8F\xE5\xB7\x9E"
unicode_text= u"\u798F\u5DDE"

print 'Part 1: con.text_factory=str'
con.text_factory = str
print type(con.text_factory)
cur.execute("CREATE TABLE table1 (city);")
cur.execute("INSERT INTO table1 (city) VALUES (?);",(a_text,))
cur.execute("INSERT INTO table1 (city) VALUES (?);",(gb_text,))
cur.execute("INSERT INTO table1 (city) VALUES (?);",(utf8_text,))
cur.execute("INSERT INTO table1 (city) VALUES (?);",(unicode_text,))
cur.execute("select city from table1")
res = cur.fetchall()
print "--  result: %s"%(res)

print 'Part 2: con.text_factory=unicode'
con.text_factory = unicode
print type(con.text_factory)
cur.execute("CREATE TABLE table2 (city);")
cur.execute("INSERT INTO table2 (city) VALUES (?);",(a_text,))
# cur.execute("INSERT INTO table2 (city) VALUES (?);",(gb_text,))
# cur.execute("INSERT INTO table2 (city) VALUES (?);",(utf8_text,))
cur.execute("INSERT INTO table2 (city) VALUES (?);",(unicode_text,))
cur.execute("select city from table2")
res = cur.fetchall()
print "--  result: %s"%(res)

print 'Part 3: OptimizedUnicode'
con.text_factory = str
cur.execute("CREATE TABLE table3 (city);")
cur.execute("INSERT INTO table3 (city) VALUES (?);",(a_text,))
#cur.execute("INSERT INTO table3 (city) VALUES (?);",(gb_text,))
cur.execute("INSERT INTO table3 (city) VALUES (?);",(utf8_text,))
cur.execute("INSERT INTO table3 (city) VALUES (?);",(unicode_text,))
con.text_factory = sqlite3.OptimizedUnicode
print type(con.text_factory)
cur.execute("select city from table3")
res = cur.fetchall()
print "--  result: %s"%(res)

print 'Part 4: custom fuction'
con.text_factory = lambda x: unicode(x, "gbk", "ignore")
print type(con.text_factory)
cur.execute("CREATE TABLE table4 (city);")
cur.execute("INSERT INTO table4 (city) VALUES (?);",(a_text,))
cur.execute("INSERT INTO table4 (city) VALUES (?);",(gb_text,))
cur.execute("INSERT INTO table4 (city) VALUES (?);",(utf8_text,))
cur.execute("INSERT INTO table4 (city) VALUES (?);",(unicode_text,))
cur.execute("select city from table4")
res = cur.fetchall()
print "--  result: %s"%(res)