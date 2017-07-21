import requests
from bs4 import BeautifulSoup
import csv
import json
import xlwt
headers={
"authority":"nj.zu.anjuke.com",
"method":"GET",
"path":"/fangyuan/yuhuataiqu/",
"scheme":"https",
"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding":"gzip, deflate, br",
"accept-language":"zh-CN,zh;q=0.8",
"cache-control":"no-cache",
"cookie":"als=0; ctid=16; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1499862039; propertys=ey3ltr-ot280k_emuv2i-ot0usq_; lps=http%3A%2F%2Fwww.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti%7Chttp%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7rRkb0qfug00PpAsaY2gKu0000052KYH300000TKMVrM.THvs_oeHEtY0UWYdP104PHDdn7tzgvq-UNqbusK15HbkmhcduWTYnj0snHu9PyD0IHdjwjFafbNawbu7fRF7PR7jrjuDfYmsrRm4fRfdPWNAP6K95gTqFhdWpyfqnWb1rH63PHbLniusThqbpyfqnHm0uHdCIZwsT1CEQLILIz49UhGdpvR8mvqVQ1qspHdfyBdBmy-bIidsmzd9UAsVmh-9ULwG0APzm1YkrjDYn0%26tpl%3Dtpl_10085_15673_1%26l%3D1053917682%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2-%2525E5%25259B%2525BD%2525E5%252586%252585%2525E9%2525A2%252586%2525E5%252585%252588%2525E6%252589%2525BE%2525E6%252588%2525BF%2525E5%2525B9%2525B3%2525E5%25258F%2525B0%2525EF%2525BC%25258C%2525E5%2525AE%252589%2525E5%2525BF%252583%2525E6%25258C%252591%2526xp%253Did%28%252522m45b49a70%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D51%26wd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3D57095150_2_oem_dg%26oq%3DPython%2525E7%25259A%252584content%2525E5%252592%25258Ccontents%26inputT%3D22091%26bs%3DPython%25E7%259A%2584content%25E5%2592%258Ccontents; sessid=4DF6493B-4E37-083F-EF31-A06FCE06DF32; _ga=GA1.2.1855490890.1499861578; _gid=GA1.2.1623631238.1500522941; aQQ_ajkguid=F5E13D46-3A2D-8098-F600-DB694545405D; twe=2; __xsptplus8=8.9.1500534113.1500534137.5%232%7Cbzclk.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23iElcZqPkzsxIsWKYIjq8YuSQkb9-RtRM%23; 58tj_uuid=d99fa209-b38f-4d82-962d-d69540410fa1; new_uv=9",
"pragma":"no-cache:",
"referer":"https://nj.zu.anjuke.com/fangyuan/yuhuataiqu/p2/",
"upgrade-insecure-requests":"1",
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"

}
sj2=[['name','lng','lat','price','detail']]
def get_html(url,headers):
    try:
        r=requests.get(url,verify=False,headers=headers)
        r.raise_for_status()
        r.encoding="utf-8"
        return r.text
    except:
        print ("出了点小问题哦")

def get_content(url):
    res=get_html(url,headers)
    soup=BeautifulSoup(res,'lxml')
    div1=soup.find('div',attrs={"class":"w1180"})
    div2=div1.find_all("div",attrs={"class":"zu-itemmod"})
    for info in div2:
        #获取租房信息小区、地址和基本信息
        sj1=[]
        try:
            name = "南京雨花台区" + info.select("address['class'='details-item'] a")[0].text.replace("\n", '') \
                .replace("                                        ", '')
        except:
            print("error")
        price=info.find("div",attrs={'class':'zu-side'}).text.replace("\n",'')
        detail1=info.find("div",attrs={"class":"zu-info"})
        detail=detail1.find("p",attrs={'class':'details-item tag'}).text
        #高德
        #gd=requests.get(gaode.format(name))
        #jd=json.loads(gd.text)
        bd1=requests.get(baidu.format(name)).text
        bd=bd1.lstrip("renderOption&&renderOption(").rstrip(")")
        jd=json.loads(bd)
        try:
            #location=jd["geocodes"][0]["location"]
            lng=jd["result"]["location"]["lng"]
            lat=jd["result"]["location"]["lat"]
        except:
            lng="none"
            lat="none"
        sj1.append(name)
        sj1.append(lng)
        sj1.append(lat)
        sj1.append(price)
        sj1.append(detail)
        sj2.append(sj1)

        #with open("anjuke.txt", "a+", encoding="utf-8") as file:
            #file.write("小区：{}\n lng：{}\n lat：{}\n 价格：{}\n 信息：{}\n \n".format(name,lng,lat, price,detail))

base_url="https://nj.zu.anjuke.com/fangyuan/yuhuataiqu/"
num=int(input("请输入要爬取的页数："))
#gaode="http://restapi.amap.com/v3/geocode/geo?address={}&output=json&key=dd0bd86982932cc1a7a337cc15d415fc"
baidu="http://api.map.baidu.com/geocoder/v2/?callback=renderOption&output=json&address={}&ak=GCQrmTm7fYbp1nKGGNK2aXqmKT79kCah"
url_list=[]
def main(base_url,num):
    for i in  range(1,num+1):
        if i==1:
            url_list.append(base_url)
        else:
            url=base_url+"p"+str(i)
            url_list.append(url)
    for  url in url_list:
        get_content(url)


if __name__ == '__main__':
    main(base_url,num)
    file_path='D:/test.xls'
    wb=xlwt.Workbook()
    sheet=wb.add_sheet('test')
    style = 'pattern: pattern solid, fore_colour yellow; '  # 背景颜色为黄色
    style += 'font: bold on; '  # 粗体字
    style += 'align: horz centre, vert center; '  # 居中
    header_style = xlwt.easyxf(style)
    row_count = len(sj2)
    col_count = len(sj2[0])
    for row in range(0, row_count):
        col_count = len(sj2[row])
        for col in range(0, col_count):
            if row == 0:  # 设置表头单元格的格式
                sheet.write(row, col, sj2[row][col], header_style)
            else:
                sheet.write(row, col, sj2[row][col])
    wb.save(file_path)
