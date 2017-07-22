import requests
from bs4 import BeautifulSoup
import csv
import json
import xlwt
headers={
"authority":"nanjing.anjuke.com",
"method":"GET",
"path":"/sale/yuhuataiqu/",
"scheme":"https",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.8",
"cache-control":"no-cache",
"cookie":"als=0; ctid=16; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1499862039; browse_comm_ids=300957%7C145749; sessid=4DF6493B-4E37-083F-EF31-A06FCE06DF32; lps=http%3A%2F%2Fnj.zu.anjuke.com%2Ffangyuan%2Fyuhuataiqu%2F%7C; propertys=huislx-otfguk_; __xsptplusUT_8=1; _gat=1; aQQ_ajkguid=F5E13D46-3A2D-8098-F600-DB694545405D; twe=2; _ga=GA1.2.1855490890.1499861578; _gid=GA1.2.1623631238.1500522941; __xsptplus8=8.17.1500648497.1500648515.3%232%7Cbzclk.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23Do_ckBuI80irksOA1PVTbfhDL4IV1Bn8%23; 58tj_uuid=d99fa209-b38f-4d82-962d-d69540410fa1; new_session=0; init_refer=http%253A%252F%252Fbzclk.baidu.com%252Fadrc.php%253Ft%253D06KL00c00f7rRkb0qfug00PpAsjpDLFu0000052KYH300000XXZmTg.THvs_oeHEtY0UWYdP104PHDdn7tzgvq-UNqbusK15HbsuHK9uW63nj0snHRvmvD0IHdjwjFafbNawbu7fRF7PR7jrjuDfYmsrRm4fRfdPWNAP6K95gTqFhdWpyfqnWb1rH63PHbLniusThqbpyfqnHm0uHdCIZwsT1CEQLILIz49UhGdpvR8mvqVQ1qspHdfyBdBmy-bIidsmzd9UAsVmh-9ULwG0APzm1YLn1Rk%2526tpl%253Dtpl_10085_15673_1%2526l%253D1053917682%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2-%252525E5%2525259B%252525BD%252525E5%25252586%25252585%252525E9%252525A2%25252586%252525E5%25252585%25252588%252525E6%25252589%252525BE%252525E6%25252588%252525BF%252525E5%252525B9%252525B3%252525E5%2525258F%252525B0%252525EF%252525BC%2525258C%252525E5%252525AE%25252589%252525E5%252525BF%25252583%252525E6%2525258C%25252591%252526xp%25253Did%28%25252522m45b49a70%25252522%29%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D51%2526wd%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526issp%253D1%2526f%253D8%2526ie%253Dutf-8%2526rqlang%253Dcn%2526tn%253D57095150_2_oem_dg%2526inputT%253D3106; new_uv=17",
"pragma":"no-cache",
"referer":"https://nanjing.anjuke.com/sale/?from=navigation",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"
}
esf_sj2=[["name","lng","lat","price","detail"]]
def get_html(url,headers):
    try:
        r=requests.get(url,verify=False,headers=headers)
        r.raise_for_status()
        r.encoding="utf-8"
        return r.text
    except:
        print ("出了点问题哦")

def get_content(url):
        res=get_html(url,headers)
        soup=BeautifulSoup(res,"lxml")
        ul1=soup.find("ul",{"id":"houselist-mod-new"})
        ul=ul1.find_all("li",attrs={"class":"list-item"})
        for info in ul:
            esf_sj1=[]
            detail=info.find_all("div",attrs={"class":"details-item"})[0].text.lstrip("\n").replace("",'|')
            name=info.find_all("div",attrs={"class":"details-item"})[1].span["title"].replace("  ",'')
            price=info.find("div",attrs={"class":"pro-price"}).text.lstrip("\n")
            #baidumap
            bd1 = requests.get(baidu.format(name)).text
            bd = bd1.lstrip("renderOption&&renderOption(").rstrip(")")
            jd = json.loads(bd)
            try:
                # location=jd["geocodes"][0]["location"]
                lng = jd["result"]["location"]["lng"]
                lat = jd["result"]["location"]["lat"]
            except:
                lng = "none"
                lat = "none"
            esf_sj1.append(name)
            esf_sj1.append(lng)
            esf_sj1.append(lat)
            esf_sj1.append(price)
            esf_sj1.append(detail)
            esf_sj2.append(esf_sj1)
            with open("ershoufang.txt","a+",encoding="utf-8") as f:
                f.write("小区：{}\n lng：{}\n lat：{}\n价格：{}\n 资料：{}\n \n".format(name,lng,lat,price,detail))
base_url="https://nanjing.anjuke.com/sale/yuhuataiqu/"
num=int(input("请输入页数："))
baidu="http://api.map.baidu.com/geocoder/v2/?callback=renderOption&output=json&address={}&ak=GCQrmTm7fYbp1nKGGNK2aXqmKT79kCah"
url_list=[]
def main(base_url,num):
    for i in range(1,num+1):
        if i==1:
            url_list.append(base_url)
        else:
            url=base_url+"p"+str(i)
            url_list.append(url)
    for url in url_list:
        get_content(url)
if __name__ == '__main__':
    main(base_url,num)
    file_path='D:/ershoufang.xls'
    wb=xlwt.Workbook()
    sheet=wb.add_sheet('test')
    style = 'pattern: pattern solid, fore_colour yellow; '  # 背景颜色为黄色
    style += 'font: bold on; '  # 粗体字
    style += 'align: horz centre, vert center; '  # 居中
    header_style = xlwt.easyxf(style)
    row_count = len(esf_sj2)
    col_count = len(esf_sj2[0])
    for row in range(0, row_count):
        col_count = len(esf_sj2[row])
        for col in range(0, col_count):
            if row == 0:  # 设置表头单元格的格式
                sheet.write(row, col, esf_sj2[row][col], header_style)
            else:
                sheet.write(row, col, esf_sj2[row][col])
    wb.save(file_path)
