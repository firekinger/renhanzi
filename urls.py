#!/usr/bin/python
# coding:utf-8 

renhanzi = (
    '/', 'renhanzi.index',
    '/demo', 'renhanzi.demo',
    '/baidu_verify_06JdVTXpoO.html', 'renhanzi.baidu',
    '/search/(radical|pinyin|strokes|idiom|post)/', 'renhanzi.search',
    '/idiom/(\D*)/', 'renhanzi.idiom_pinyin',
    '/strokes/(\d*)/', 'renhanzi.strokes',
    '/radical/(.*)/', 'renhanzi.radical',
    '/word/(\d*)/', 'renhanzi.word',
    '/idiom/(\d*)/', 'renhanzi.idiom',
    '/(\D*)/(\d*)/', 'renhanzi.hanzi',
    '/(\D*)/', 'renhanzi.pinyin',


    #'/(.*)/', 'renhanzi.redirect',
)