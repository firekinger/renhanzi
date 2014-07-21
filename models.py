#!/usr/bin/env python
# coding: utf-8
import web
import datetime
import settings

db = settings.db


def get_last_id():
    sql = "SELECT LAST_INSERT_ID() AS last_id"
    s = db.query(sql)
    if not s:
        return False
    return s[0].last_id

# 单页
def get_post(table, field, id):
    try:
        return db.select(table, what=field, where="id=$id", vars=locals())[0]
    except IndexError:
        return None

# 多页
def get_posts(table, field, filter):
    return db.select(table, what=field, where=filter, order="id ASC")

# 汉字
def get_hanzi(pinyin):
    sql = "SELECT `hanzi` FROM `dic_hanzi` WHERE status=\'publish\' AND pinyin='%s'" % pinyin
    return db.query(sql)

# 拼音
def get_pinyin(pronunciation):
    try:
        #return db.select('dic_pronunciation', what='pinyin', where="pronunciation=$pronunciation", vars=locals())[0]
        return db.select('dic_tone', what='pinyin', where="pronunciation=$pronunciation", vars=locals())[0]
    except IndexError:
        return None

def get_hanzi_content(hanzi):
    try:
        return db.select('dic_content', what='hanzi, wubi, radical, num, pronunciation, summary, content', where="hanzi=$hanzi", vars=locals())[0]
    except IndexError:
        return None

def get_word_id(word):
    try:
        return db.select('dic_word', what='id', where="status=\'publish\' AND word=$word", vars=locals())[0]
    except IndexError:
        return None

#
def update_post_hits (table, id, hits):
    db.update(table, where="id=$id", vars=locals(), hits=hits)


def create_customer_event (customer, locid, table, act):
    db.insert('events', locid=locid, team=customer, table_name=table, ip=web.ctx.ip, date=datetime.datetime.utcnow(), agent=web.ctx.env["HTTP_USER_AGENT"], source=web.ctx.env["HTTP_HOST"]+web.ctx.env["PATH_INFO"], act=act, type='customer')

def create_event (locid, table, act):
    team = '0'
    if 'login_' not in act:team = session.customer_id
    db.insert('events', locid=locid, team=team, table_name=table, ip=web.ctx.ip, date=datetime.datetime.utcnow(), agent=web.ctx.env["HTTP_USER_AGENT"], source=web.ctx.env["HTTP_HOST"]+web.ctx.env["PATH_INFO"], act=act)

def get_inject_check (s):
    return s.replace('\'','')

# 分页
def get_paging(current, pages):
    index = 1
    showpages = 8
    basepages = showpages/2
    if current<1:
        current = index
    elif current>pages:
        current = pages
    start = current - basepages
    prev = current - 1
    next = current + 1
    end = current + basepages
    if pages<showpages:
        start = index
        end = pages
    elif end<showpages:
        end = showpages
    if start<index: start = index
    if prev<index: prev = index
    if next>pages: next = pages
    if end>pages: end = pages
    paging = {'index':index, 'start':start,'prev':prev,'current':current, 'next':next,'end':end,'pages':pages}
    return paging

# 添加

def create_message(locid, customer, team, message, private, type):
    db.insert('messages', locid = locid, customer = customer, team = team, message = message, private = private, type = type, status='publish', date = datetime.datetime.utcnow())


def create_guestbook(prefix, customer, aname, aemail, aphone, aaddress, title, content, type):
#    u = uname.decode('u8','ignore')
    ip = web.ctx.ip
    agent = web.ctx.env.get('HTTP_USER_AGENT')
    db.insert('guestbooks', prefix = prefix, customer=customer, author = aname, author_mt = aphone, author_email = aemail, author_address = aaddress, author_ip = ip, title = title, content = content, reply = '', type = type, date = datetime.datetime.utcnow(), agent = agent)




