#!/usr/bin/env python
# coding: utf-8
import sae
import web
import os.path

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

db = web.database(dbn='mysql', host=sae.const.MYSQL_HOST,port=int(sae.const.MYSQL_PORT), user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS, db=sae.const.MYSQL_DB)

# 获取属性
# ü > v
dic_pinyin = {
'a' : 'a,ai,an,ang,ao',
'b' : 'ba,bai,ban,bang,bao,bei,ben,beng,bi,bian,biao,bie,bin,bing,bo,bu',
'c' : 'ca,cai,can,cang,cao,ce,cen,ceng,cha,chai,chan,chang,chao,che,chen,cheng,chi,chong,chou,chu,chua,chuai,chuan,chuang,chui,chun,chuo,ci,cong,cou,cu,cuan,cui,cun,cuo',
'd' : 'da,dai,dan,dang,dao,de,den,dei,deng,di,dia,dian,diao,die,ding,diu,dong,dou,du,duan,dui,dun,duo',
'e' : 'e,ei,en,eng,er',
'f' : 'fa,fan,fang,fei,fen,feng,fo,fou,fu',
'g' : 'ga,gai,gan,gang,gao,ge,gei,gen,geng,gong,gou,gu,gua,guai,guan,guang,gui,gun,guo',
'h' : 'ha,hai,han,hang,hao,he,hei,hen,heng,hong,hou,hu,hua,huai,huan,huang,hui,hun,huo',
'j' : 'ji,jia,jian,jiang,jiao,jie,jin,jing,jiong,jiu,ju,juan,jue,jun',
'k' : 'ka,kai,kan,kang,kao,ke,ken,keng,kong,kou,ku,kua,kuai,kuan,kuang,kui,kun,kuo',
'l' : 'la,lai,lan,lang,lao,le,lei,leng,li,lia,lian,liang,liao,lie,lin,ling,liu,long,lou,lu,lü,luan,lue,lüe,lun,luo',
'm' : 'm,ma,mai,man,mang,mao,me,mei,men,meng,mi,mian,miao,mie,min,ming,miu,mo,mou,mu',
'n' : 'na,nai,nan,nang,nao,ne,nei,nen,neng,ng,ni,nian,niang,niao,nie,nin,ning,niu,nong,nou,nu,nü,nuan,nüe,nuo,nun',
'o' : 'o,ou',
'p' : 'pa,pai,pan,pang,pao,pei,pen,peng,pi,pian,piao,pie,pin,ping,po,pou,pu',
'q' : 'qi,qia,qian,qiang,qiao,qie,qin,qing,qiong,qiu,qu,quan,que,qun',
'r' : 'ran,rang,rao,re,ren,reng,ri,rong,rou,ru,ruan,rui,run,ruo',
's' : 'sa,sai,san,sang,sao,se,sen,seng,sha,shai,shan,shang,shao,she,shei,shen,sheng,shi,shou,shu,shua,shuai,shuan,shuang,shui,shun,shuo,si,song,sou,su,suan,sui,sun,suo',
't' : 'ta,tai,tan,tang,tao,te,teng,ti,tian,tiao,tie,ting,tong,tou,tu,tuan,tui,tun,tuo',
'w' : 'wa,wai,wan,wang,wei,wen,weng,wo,wu',
'x' : 'xi,xia,xian,xiang,xiao,xie,xin,xing,xiong,xiu,xu,xuan,xue,xun',
'y' : 'ya,yan,yang,yao,ye,yi,yin,ying,yo,yong,you,yu,yuan,yue,yun',
'z' : 'za,zai,zan,zang,zao,ze,zei,zen,zeng,zha,zhai,zhan,zhang,zhao,zhe,zhei,zhen,zheng,zhi,zhong,zhou,zhu,zhua,zhuai,zhuan,zhuang,zhui,zhun,zhuo,zi,zong,zou,zu,zuan,zui,zun,zuo'
}

list_strokes = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '39', '51')

def list_radical_num ():
    list = []
    options = db.select('dic_radical', what='DISTINCT num')
    for o in options:
        list.append(o.num)
    return list

def dic_radical ():
    dic = {}
    options = db.select('dic_radical', what='id, radical')
    for o in options:
        dic[o.id] = o.radical
    return dic

def dic_radicals ():
    dics = {}
    for l in list_radical_num():
        dic = {}
        options = db.select('dic_radical', what='id, radical', where='num = $l', vars=locals())
        for o in options:
            dic[o.id] = o.radical
        dics[l] = dic
    return dics

def list_abcd ():
    list = []
    options = db.select('dic_pinyin', what='DISTINCT slug')
    for o in options:
        list.append(o.slug)
    return list

def list_type (s):
    list = []
    ul = s.split(',')
    for u in ul:
        l = u.split(':')
        list.append(l)
    return list

def get_sstr(s):
    return '%s' % s

def get_tov(s):
    return s.replace('ü', 'v')

def get_week(s):
    r = '日'
    if s == '1':r = '一'
    if s == '2':r = '二'
    if s == '3':r = '三'
    if s == '4':r = '四'
    if s == '5':r = '五'
    if s == '6':r = '六'
    return r

def get_gbk(s):
    return s.decode('gbk').rstrip()

def get_html(s):
    content = s
    content = content.replace('\r\n','')
#    content = content.replace('\xa1\xa1','')
#    content = get_gbk(content)
    content = content.replace('<strong><br />','<strong>')
    content = content.replace('<br />','</p><p>')
    content = content.replace('</p><p>','</p>\n<p>')
#    content = content.replace('&lt;br /&gt;','&lt;/p&gt;&lt;p&gt;')
#    content = '<p>'+ content + '</p>'
#    content = content.replace('<p><p>','<p>')
#    content = content.replace('</p></p>','</p>')
    return content

def get_title(s, num):
    if len(s)>num:return s[:num] + '...'
    return s

def get_date(s):
    return s.strftime('%Y-%m-%d')

def get_one(s):
    r = s.split(',')
    return r[0]

def get_mp4(s):
    r = get_one(s)
    r = r.replace('flv','mp4')
    return r

def get_path(i):
    r = web.ctx.path
    r = r.split('/')
    return r[i]

def get_sqlv(s):
    r = s
    r = r.replace("'","''")
    return r

def is_agent(s):
    r = web.ctx.env["HTTP_USER_AGENT"]
    if r.find(s) > 0:
        return True
    else:
        return False







web.template.Template.globals['isagent'] = is_agent
web.template.Template.globals['sstr'] = get_sstr
web.template.Template.globals['tov'] = get_tov
web.template.Template.globals['gbk'] = get_gbk
web.template.Template.globals['html'] = get_html
web.template.Template.globals['title'] = get_title
web.template.Template.globals['date'] = get_date
web.template.Template.globals['one'] = get_one
web.template.Template.globals['mp4'] = get_mp4
web.template.Template.globals['path'] = get_path
web.template.Template.globals['pinyin'] = dic_pinyin
web.template.Template.globals['radicals'] = dic_radicals()
web.template.Template.globals['radical_num'] = list_radical_num()
web.template.Template.globals['abcd'] = list_abcd()
web.template.Template.globals['strokes'] = list_strokes
web.template.Template.globals['render'] = render




