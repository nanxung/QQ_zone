#coding:utf-8
from  selenium import webdriver
import requests
import time
import os
from urllib import parse
import configparser

class Spider(object):
    def __init__(self):
        self.web=webdriver.Chrome()
        self.web.get('https://user.qzone.qq.com')
        config = configparser.ConfigParser(allow_no_value=False)
        config.read('userinfo.ini')
        self.__username =config.get('qq_info','qq_number')
        self.__password=config.get('qq_info','qq_password')
        self.headers={
                'host': 'h5.qzone.qq.com',
                'accept-encoding':'gzip, deflate, br',
                'accept-language':'zh-CN,zh;q=0.8',
                'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
                'connection': 'keep-alive'
        }
        self.req=requests.Session()
        self.cookies={}

    

    def login(self):
        self.web.switch_to_frame('login_frame')
        log=self.web.find_element_by_id("switcher_plogin")
        log.click()
        time.sleep(1)
        username=self.web.find_element_by_id('u')
        username.send_keys(self.__username)
        ps=self.web.find_element_by_id('p')
        ps.send_keys(self.__password)
        btn=self.web.find_element_by_id('login_button')
        time.sleep(1)
        btn.click()
        time.sleep(2)
        self.web.get('https://user.qzone.qq.com/{}'.format(self.__username))
        cookie=''
        for elem in self.web.get_cookies():
            cookie+=elem["name"]+"="+ elem["value"]+";"
        self.cookies=cookie
        self.get_g_tk()
        self.headers['Cookie']=self.cookies
        self.web.quit()
        
    
    def get_frends_url(self):
        url='https://h5.qzone.qq.com/proxy/domain/base.qzone.qq.com/cgi-bin/right/get_entryuinlist.cgi?'
        params = {"uin": self.__username,
              "fupdate": 1,
              "action": 1,
              "g_tk": self.g_tk}
        url = url + parse.urlencode(params)
        return url

    def get_frends_num(self):
        t=True
        offset=0
        url=self.get_frends_url()
        while(t):
            url_=url+'&offset='+str(offset)
            page=self.req.get(url=url_,headers=self.headers)
            if "\"uinlist\":[]" in page.text:
                t=False
            else:

                if not os.path.exists("./frends/"):
                    os.mkdir("frends/")
                with open('./frends/'+str(offset)+'.json','w',encoding='utf-8') as w:
                    w.write(page.text)
                offset += 50

    def get_mood_url(self):
        url='https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?'
        params = {
              "sort":0,
                  "start":0,
              "num":20,
            "cgi_host": "http://taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6",
              "replynum":100,
              "callback":"_preloadCallback",
              "code_version":1,
            "inCharset": "utf-8",
            "outCharset": "utf-8",
            "notice": 0,
              "format":"jsonp",
              "need_private_comment":1,
              "g_tk": self.g_tk
              }
        url = url + parse.urlencode(params)
        return url


    def get_mood_detail(self):
        from getFrends import frends_list
        url = self.get_mood_url()
        for u in frends_list[245:]:
            t = True
            QQ_number=u['data']
            url_ = url + '&uin=' + str(QQ_number)
            pos = 0
            while (t):
                url__ = url_ + '&pos=' + str(pos)
                mood_detail = self.req.get(url=url__, headers=self.headers)
                print(QQ_number,u['label'],pos)
                if "\"msglist\":null" in mood_detail.text or "\"message\":\"对不起,主人设置了保密,您没有权限查看\"" in mood_detail.text:
                    t = False
                else:
                    if not os.path.exists("./mood_detail/"):
                        os.mkdir("mood_detail/")
                    if not os.path.exists("./mood_detail/"+u['label']):
                        os.mkdir("mood_detail/"+u['label'])
                    with open('./mood_detail/'+u['label']+"/" +str(QQ_number)+"_"+ str(pos) + '.json', 'w',encoding='utf-8') as w:
                        w.write(mood_detail.text)
                    pos += 20
            time.sleep(2)


    def get_g_tk(self):
        p_skey = self.cookies[self.cookies.find('p_skey=')+7: self.cookies.find(';', self.cookies.find('p_skey='))]
        h=5381
        for i in p_skey:
            h+=(h<<5)+ord(i)
        print('g_tk',h&2147483647)
        self.g_tk=h&2147483647


        

if __name__=='__main__':
    sp=Spider()
    sp.login()
    sp.get_frends_num()
    sp.get_mood_detail()
    from data_analys import dataToExcel
