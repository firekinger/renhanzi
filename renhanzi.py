#!/usr/bin/env python
# coding: utf-8
import web
import datetime
import hashlib
import models
import re
import settings

render = settings.render
dic_radical = settings.dic_radical()

web.config.debug = True

class demo:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8")
        a = "'abc123'ABC'"
        b = web.utils.safestr(a)
        c = web.utils.safeunicode(a)
        d = web.net.websafe(a)
        #return render.error('没找到这条记录', None)
        return 'ok'

class index:
    def GET(self):
        return render.renhanzi.index()

class baidu:
    def GET(self):
        return render.renhanzi.baidu_verify_06JdVTXpoO()

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

class search:
    def GET(self, name):
        if name == 'radical':
            return render.renhanzi.search_radical()
        elif name == 'pinyin':
            return render.renhanzi.search_pinyin()
        elif name == 'strokes':
            return render.renhanzi.search_strokes()
        elif name == 'idiom':
            return render.renhanzi.search_idiom()
        else:
            return render.renhanzi.p404(name)

    def POST(self, name):
        i = web.input()
        key = i.search_key
        key = key.replace('\'','')
        key = key.replace(' ','')
        key_en = re.match(r'^[a-zA-Z]+$', key)
        if key_en:
            path = '/%s/' % key
            raise web.seeother(path)
        else:
            l = len(key)
            try:
                if l == 1:
                    path = '/%s/' % key
                else:
                    word = models.get_word_id(key)
                    path = '/word/%s/' % word.id
                raise web.seeother(path)
            except:
                return render.renhanzi.p404(key)

class strokes:
    def GET(self, id):
        hanzi = models.get_posts("dic_hanzi", "id, hanzi, pinyin, num, radical", "status = 'publish' AND num=" + id)
        return render.renhanzi.strokes(id, hanzi)

class radical:
    def GET(self, name):
        if name.isdigit():
            r = dic_radical[int(name)]
            hanzi = models.get_posts("dic_hanzi", "id, hanzi, pinyin, radical", "status = 'publish' AND radical='" + r + "'")
            return render.renhanzi.radical(r, hanzi)
        else:
            hanzi = models.get_posts("dic_hanzi", "id, hanzi, pinyin, radical", "status = 'publish' AND radical='" + name + "'")
            return render.renhanzi.radical(name, hanzi)

class pinyin:
    def GET(self, name):
        key_en = re.match(r'^[a-zA-Z]+$', name)
        if key_en:
            name = name.lower()
            hz = models.get_hanzi(name)
            return render.renhanzi.pinyin(name, hz)
        else:
            key = '%s' % name
            hz = models.get_hanzi_content(key)
            try:
                p = hz.pronunciation.split(',')[0]
                name = models.get_pinyin(p).pinyin
            except:
                name = 'i'
            words = models.get_posts("dic_word", "id, word", "hanzi='" + hz.hanzi + "'")
            #2014-7-18 ALTER TABLE `dic_word` ADD INDEX (hanzi);
            return render.renhanzi.hanzi(name, hz, words)

class hanzi:
    def GET(self, name, id):
        hz = models.get_post("dic_content", "hanzi, wubi, radical, num, pronunciation, summary, content", id)
        words = models.get_posts("dic_word", "id, word", "hanzi='" + hz.hanzi + "'")
        return render.renhanzi.hanzi(name, hz, words)
        
class word:
    def GET(self, id):
        w = models.get_post("dic_word", "hanzi, word, pinyin, traditional, description", id)
        words = models.get_posts("dic_word", "id, word", "hanzi='" + w.hanzi + "'")
        idioms = models.get_posts("dic_idiom", "id, idiom", "hanzi='" + w.hanzi + "'")
        #2014-7-18 ALTER TABLE `dic_idiom` ADD INDEX (hanzi)
        return render.renhanzi.word(w, words, idioms)
        #return 'ok22'

class idiom:
    def GET(self, id):
        ii = models.get_post("dic_idiom", "hanzi, idiom, description, source, example, synonyms, antonym, instructions, english, story, pinyin, abc", id)
        words = models.get_posts("dic_word", "id, word", "hanzi='" + ii.hanzi + "'")
        idioms = models.get_posts("dic_idiom", "id, idiom", "hanzi='" + ii.hanzi + "'")
        return render.renhanzi.idiom(ii, words, idioms)

class idiom_pinyin:
    def GET(self, name):
        idioms = models.get_posts("dic_idiom", "id, idiom", "pinyin like '" + name + "%'")
        return render.renhanzi.idiom_pinyin(name, idioms)







