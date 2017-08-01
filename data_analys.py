import json
import os
import xlwt
import pymysql
#存入Excel
# def dataToExcel():
#     d=[i for i in os.listdir('mood_detail') if not i.endswith('.xls')]
#     for ii in d:
#         wb=xlwt.Workbook()
#         sheet=wb.add_sheet('sheet1',cell_overwrite_ok=True)
#         sheet.write(0,0,'content')
#         sheet.write(0,1,'createTime')
#         sheet.write(0,2,'commentlist')
#         sheet.write(0,3,'source_name')
#         sheet.write(0,4,'cmtnum')
#         fl=[i for i in os.listdir('mood_detail/'+ii) if i.endswith('.json')]
#         print('mood_detail/'+ii)
#         k=1
#         for i in fl:
#             with open('mood_detail/'+ii+"/"+i,'r',encoding='latin-1') as w:
#                 s=w.read()[17:-2]
#                 js=json.loads(s)
#                 print(i)
#                 for s in js['msglist']:
#                     m=-1
#                     sheet.write(k,m+1,str(s['content']))
#                     sheet.write(k,m+2,str(s['createTime']))
#                     if not s['commentlist']:
#                         s['commentlist']=list()
#                     sheet.write(k,m+3,str([(x['content'],x['createTime2'],x['name'],x['uin']) for x in list(s['commentlist'])]))
#                     sheet.write(k,m+4,str(s['source_name']))
#                     sheet.write(k,m+5,str(s['cmtnum']))
#                     k+=1
#         if not os.path.exists('mood_detail/Excel/'):
#             os.mkdir('mood_detail/Excel/')
#         try:
#             wb.save('mood_detail/Excel/'+ii+'.xls')
#         except Exception:
#             print("error")
#


def dataToExcel():
    ll=0
    d=[i for i in os.listdir('mood_detail') if not i.endswith('.xls')]
    for ii in d:
        # wb=xlwt.Workbook()
        # sheet=wb.add_sheet('sheet1',cell_overwrite_ok=True)
        # sheet.write(0,0,'content')
        # sheet.write(0,1,'createTime')
        # sheet.write(0,2,'commentlist')
        # sheet.write(0,3,'source_name')
        # sheet.write(0,4,'cmtnum')
        fl=[i for i in os.listdir('mood_detail/'+ii) if i.endswith('.json')]
        print('mood_detail/'+ii)
        k=1
        for i in fl:
            with open('mood_detail/'+ii+"/"+i,'r',encoding='latin-1') as w:
                s=w.read()[17:-2]
                js=json.loads(s)
                print(i)
                for s in js['msglist']:
                    ll+=1
                    m=-1
                    # sheet.write(k,m+1,str(s['content']))
                    # sheet.write(k,m+2,str(s['createTime']))
                    if not s['commentlist']:
                        s['commentlist']=list()
                    # sheet.write(k,m+3,str([(x['content'],x['createTime2'],x['name'],x['uin']) for x in list(s['commentlist'])]))
                    # sheet.write(k,m+4,str(s['source_name']))
                    # sheet.write(k,m+5,str(s['cmtnum']))
                    k+=1
        if not os.path.exists('mood_detail/Excel/'):
            os.mkdir('mood_detail/Excel/')
    print(ll)
        # try:
        #     wb.save('mood_detail/Excel/'+ii+'.xls')
        # except Exception:
        #     print("error")

dataToExcel()




'''
存入数据库
def dataToExcel():
    con=pymysql.connect(
        host='127.0.0.1',
        user='root',
        password="×××",
        database='qq_z',
        port=3306,
    )
    cur=con.cursor()
    sql="insert into info (qq_number,created_time,content,commentlist,source_name,cmtnum,name) values ({},{},{},{},{},{},{});"

    d=[i for i in os.listdir('mood_detail') if not i.endswith('.xls')]
    for ii in d:
        fl=[i for i in os.listdir('mood_detail/'+ii) if i.endswith('.json')]
        print('mood_detail/'+ii)
        k=1
        for i in fl:
            with open('mood_detail/'+ii+"/"+i,'r',encoding='latin-1') as w:
                s=w.read()[17:-2]
                js=json.loads(s)
                print(i)
                for s in js['msglist']:
                    m=-1
                    if not s['commentlist']:
                        s['commentlist']=list()
                    cur.execute(sql.format(int(i[:i.find('_')]),s['created_time'],str(s['content']),str([(x['content'],x['createTime2'],x['name'],x['uin']) for x in list(s['commentlist'])]),str(s['source_name']),int(s['cmtnum']),str(s['name'])))
                    k+=1
        con.commit()
        con.close()
'''