import requests
import urllib.request as req
import csv

url = "http://www.i-write.idv.tw/life/info/food/food.html"
request = req.Request(url , headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
})
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")

print("請輸入縣市完整名稱(ex:台北市)")
city = str(input())
city_data = ["基隆市" , "新北市" , "台北市" , "桃園市" , "新竹市" , "新竹縣" , "宜蘭縣" , "苗栗縣" , "台中市" , "彰化縣" , "雲林縣" , "南投縣" , "嘉義縣" , "嘉義市" , "台南市" , "高雄市" , "屏東縣" , "澎湖縣" , "金門縣" , "花蓮縣" , "台東縣" , "連江縣"]
for i in range(0 , 22):
    if(city_data[i] == city):
        number = i + 1
response1 = requests.get("http://www.i-write.idv.tw/life/info/food/food"+ str(number) +".html" )


keelung_area = ["仁愛區" , "信義區" , "中正區" , "中山區" , "安樂區" , "暖暖區" , "七堵區"]
newtaipei_area = ["萬里區" , "金山區" , "板橋區" , "汐止區" , "深坑區" , "石碇區" , "瑞芳區" , "平溪區" , "雙溪區" , "貢寮區" , "新店區" , "坪林區" , "烏來區" , "永和區" , "中和區" , "土城區" , "三峽區" , "樹林區" , "鶯歌區" , "三重區" , "新莊區" , "泰山區" , "林口區" , "蘆洲區" , "五股區" , "八里區" , "淡水區" , "三芝區" , "石門區"]
taipei_area = ["中正區" , "大同區" , "中山區" , "松山區" , "大安區" , "萬華區" , "信義區" , "士林區" , "北投區" , "內湖區" , "南港區" , "文山區"]
taoyuan_area = ["中壢區" , "平鎮區" , "龍潭區" , "楊梅區" , "新屋區" , "觀音區" , "桃園區" , "龜山區" , "八德區" , "大溪區" , "復興區" , "大園區" , "蘆竹區"]
hsinchu1_area = ["北區" , "東區"]
hsinchu2_area = ["竹北市" , "湖口鄉" , "新豐鄉" , "新埔鎮" , "關西鎮" , "芎林鄉" , "寶山鄉" , "竹東鎮" , "五峰鄉" , "橫山鄉" , "尖石鄉" , "北埔鄉" , "峨眉鄉"]
yilan_area = ["宜蘭市" , "頭城鎮" , "礁溪鄉" , "壯園鄉" , "員山鄉" , "羅東鎮" , "三星鄉" , "大同鄉" , "五結鄉" , "冬山鄉" , "蘇澳鎮" , "南澳鄉"]
miaoli_area = ["竹南鎮" , "頭份鎮" , "三灣鄉" , "南庄鄉" , "獅潭鄉" , "後龍鎮" , "通宵鎮" , "苑裡鎮" , "苗栗市" , "造橋鄉" , "頭屋鄉" , "公館鄉" , "大湖鄉" , "泰安鄉" , "銅鑼鄉" , "三義鄉" , "西湖鄉" , "卓蘭鎮"]
taichung_area = ["中區" , "東區" , "南區" , "西區" , "北區" , "北屯區" , "西屯區" , "南屯區" , "太平區" , "大里區" , "霧峰區" , "烏日區" , "豐原區" , "后里區" , "石岡區" , "東勢區" , "和平區" , "新社區" , "潭子區" , "大雅區" , "神岡區" , "大肚區" , "沙鹿區" , "龍井區" , "梧棲區" , "清水區" , "大甲區" , "外埔區" , "大安區"]
changhua_area = ["彰化市" , "芬園鄉" , "花壇鄉" , "秀水鄉" , "鹿港鄉" , "福興鄉" , "線西鄉" , "和美鎮" , "伸港鄉" , "員林鎮" , "社頭鄉" , "永靖鄉" , "埔心鄉" , "溪湖鎮" , "大村鄉" , "埔鹽鄉" , "田中鎮" , "北斗鎮" , "田尾鄉" , "埤頭鄉" , "溪州鄉" , "竹塘鄉" , "二林鎮" , "大城鄉" , "芳苑鄉" , "二水鄉"]
yunlin_area = ["斗南鎮" , "大埤鄉" , "虎尾鎮" , "土庫鎮" , "褒忠鄉" , "東勢鄉" , "台西鄉" , "崙背鄉" , "麥寮鄉" , "斗六鄉" , "林內鄉" , "古坑鄉" , "莿桐鄉" , "西螺鎮" , "二崙鄉" , "北港鎮" , "水林鄉" , "口湖鄉" , "四湖鄉" , "元長鄉"]
yunlin_area = ['斗南鎮' , '大埤鄉','虎尾鎮','土庫鎮','褒忠鄉','東勢鄉','台西鄉','崙背鄉','麥寮鄉','斗六市','林內鄉','古坑鄉','莿桐鄉','西螺鎮','二崙鄉','北港鎮','水林鄉','口湖鄉','四湖鄉','元長鄉']
nantou_area = ['南投市' , '中寮鄉','草屯鎮','國姓鄉','埔里鎮','仁愛鄉','名間鄉','集集鎮','水里鄉','魚池鄉','信義鄉','竹山鎮','鹿谷鄉']
chiayi1_area = ['番路鄉' , '梅山鄉','竹崎鄉','阿里山鄉','中埔鄉','大埔鄉','水上鄉','鹿草鄉','太保市','朴子市','東石鄉','六腳鄉','新港鄉','民雄鄉','大林鎮','溪口鄉','義竹鄉','布袋鎮']
chiayi2_area = ['西區' , '東區']
tainan_area = ["中西區" , "東區" , "南區" , "北區" , "安平區" , "安南區" , "永康區" , "歸仁區" , "新化區" , "左鎮區","玉井區","楠西區","楠化區","仁德區","關廟區","龍崎區","官田區","麻豆區","佳里區","西港區","七股區","將軍區","學甲區","北門區","新營區","後壁區","白河區","東山區","六甲區","下營區","柳營區","鹽水區","善化區","大內區","山上區","新市區","安定區"]
kaohsiung_area = ["新興區" , "前金區" ,"苓雅區" , "鹽埕區" , "鼓山區" , "旗津區" , "前鎮區" , "三民區" , "楠梓區","小港區","左營區","仁武區","大社區","岡山區","路竹區","阿蓮區","田寮區","燕巢區","橋頭區","梓官區","彌陀區","永安區","湖內區","鳳山區","大寮區","林園區","鳥松區","大樹區","旗山區","美濃區","六龜區","內門區","杉林區","甲仙區","桃源區","那瑪夏區","茂林區","茄萣區"]
pingtung_area = ["屏東市" , "三地門" , "霧台鄉" , "瑪家鄉" , "九如鄉" , "里港鄉" , "高樹鄉" , "鹽埔鄉" , "長治鄉","麟洛鄉","竹田鄉","內埔鄉","萬丹鄉","潮州鎮","泰武鄉","來義鄉","萬巒鄉","崁頂鄉","新埤鄉","南州鄉","林邊鄉","東港鎮","琉球鄉","佳冬鄉","新園鄉","枋寮鄉","枋山鄉","春日鄉","獅子鄉","車城鄉","牡丹鄉","恆春鎮","滿洲鄉"]
penghu_area = ["馬公市" , "西嶼鄉" , "望安鄉" , "七美鄉" , "白沙鄉" , "湖西鄉"]
kinmen_area = ["烏坵鄉" , "金城鎮" , "金湖鎮" , "金沙鎮" , "金寧鄉" , "烈嶼鄉"]
hualien_area = ["花蓮市" , "鳳林鎮" , "玉里鎮" , "新城鄉" , "吉安鄉" , "壽豐鄉" , "光復鄉" , "豐濱鄉" , "瑞穗鄉" , "富里鄉" , "秀林鄉" , "萬榮鄉" , "卓溪鄉"]
taitung_area = ["臺東市" , "成功鎮" , "關山鎮" , "卑南鄉" , "大武鄉" , "太麻里鄉" , "東河鄉" , "長濱鄉" , "鹿野鄉" , "池上鄉" , "綠島鄉" , "延平鄉" , "海端鄉" , "達仁鄉" , "金峰鄉" , "蘭嶼鄉"]
lienchiang_area = ["南竿鄉" , "北竿鄉" , "莒光鄉" , "東引鄉"]

if(number == 1):
    for i in range(0 , 7):
        print("%d:%s" %(i+1 , keelung_area[i]) , end = " ")
elif(number == 2):
    for i in range(0 , 29):
        print("%d:%s" %(i+1 , newtaipei_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 3):
    for i in range(0 , 12):
        print("%d:%s" %(i+1 , taipei_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 4):
    for i in range(0 , 13):
        print("%d:%s" %(i+1 , taoyuan_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 5):
    for i in range(0 , 2):
        print("%d:%s" %(i+1 , hsinchu1_area[i]) , end = " ")
elif(number == 6):
    for i in range(0 , 13):
        print("%d:%s" %(i+1 , hsinchu2_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 7):
    for i in range(0 , 12):
        print("%d:%s" %(i+1 , yilan_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 8):
    for i in range(0 , 18):
        print("%d:%s" %(i+1 , miaoli_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 9):
    for i in range(0 , 29):
        print("%d:%s" %(i+1 , taichung_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 10):
    for i in range(0 , 26):
        print("%d:%s" %(i+1 , changhua_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 11):
    for i in range(0 , 20):
        print("%d:%s" %(i+1 , yunlin_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 12):
    for i in range(0 , 13):
        print("%d:%s" %(i+1 , nantou_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")                
elif(number == 13):
    for i in range(0 , 18):
        print("%d:%s" %(i+1 , chiayi1_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 14):
    for i in range(0 , 2):
        print("%d:%s" %(i+1 , chiayi2_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 15):
    for i in range(0 , 37):
        print("%d:%s" %(i+1 , tainan_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 16):
    for i in range(0 , 38):
        print("%d:%s" %(i+1 , kaohsiung_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 17):
    for i in range(0 , 33):
        print("%d:%s" %(i+1 , pingtung_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 18):
    for i in range(0 , 6):
        print("%d:%s" %(i+1 , penghu_area[i]) , end = " ")
elif(number == 19):
    for i in range(0 , 6):
        print("%d:%s" %(i+1 , kinmen_area[i]) , end = " ")
elif(number == 20):
    for i in range(0 , 13):
        print("%d:%s" %(i+1 , hualien_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 21):
    for i in range(0 , 16):
        print("%d:%s" %(i+1 , taitung_area[i]) , end = " ")
        if(i % 9 == 0 and i != 0):
            print("\n")
elif(number == 22):
    for i in range(0 , 4):
        print("%d:%s" %(i+1 , lienchiang_area[i]) , end = " ")

print("\n")
print("請依照上表，輸入各區代碼")
area = int(input())

# 抓取地區網頁
response2 = requests.get("http://www.i-write.idv.tw/life/info/food/food" + str(number) + "-" + str(area) + ".html")
url2 = "http://www.i-write.idv.tw/life/info/food/food" + str(number) + "-" + str(area) + ".html"
request2 = req.Request(url2 , headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
})
with req.urlopen(request2) as response2:
    data2 = response2.read().decode("utf-8")

from bs4 import BeautifulSoup
soup = BeautifulSoup(data2,"html.parser")


# 用標籤抓內容-法一
# namelist = ["店名"]
# name = soup.find_all(target = "_blank")
# for s in name:
#     namelist.append(s.text)
# str_match = [s for s in namelist if "地圖" in s] 
# if(len(str_match) != 0):
#     namelist.remove(str_match[0])

# phonelist = []
# phone = soup.find_all(width = "82")
# for s in phone:
#     phonelist.append(s.string)

# addresslist = []
# address = soup.find_all(width = "174")
# for s in address:
#     addresslist.append(s.string)

# runtimelist = []
# runtime = soup.find_all(width = "124")
# for s in runtime:
#     runtimelist.append(s.string)

# l = len(namelist)

# for i in range(1,l):
    # print(namelist[i] , end = " ")
    # print(phonelist[i] , end = " ")
    # print(addresslist[i] , end = " ")
    # print(runtimelist[i] , end = " ")
    # print("\n")

# 法二
# anslist = []
# totallist = []
# total = soup.find_all("table" , cellspacing="0" , cellpadding="0")
# for s in total:
#     totallist.append(s.text)
# totallist.remove(totallist[0])
# print("%s " %totallist[0])

# 法三
# namelist = []
# addresslist = []
# timelist = []
# phonelist = []
# foodlist = []
# numlist = []
# totallist = []

# for i in range(64,251) :
#     for total in soup.find_all("td" , width=i) :
#         totallist.append(total.text)
# l = len(totallist)

# for i in range(l):  
#     if(totallist[i] == '店名'):
#         name = i
#         numlist.append(i)
#     if(totallist[i] == '地址'):
#         address = i
#         numlist.append(i)
#     if(totallist[i] == '營業時間'):
#         time = i
#         numlist.append(i)
#     if(totallist[i] == '電話'):
#         phone = i
#         numlist.append(i)
#     if(totallist[i] == '招牌美食'):
#         food = i
#         numlist.append(i)
#     if(totallist[i] == 'GPS座標'):
#         gps = i
#         numlist.append(i)

# numlist.sort()
# num = numlist[1] - numlist[0] - 1

# for i in range(name+1 , name+1+num):
#     namelist.append(totallist[i])
# for i in range(address+1 , address+1+num):
#     addresslist.append(totallist[i])
# for i in range(time+1 , time+1+num):
#     timelist.append(totallist[i])
# for i in range(phone+1 , phone+1+num):
#     phonelist.append(totallist[i])
# for i in range(food+1 , food+1+num):
#     foodlist.append(totallist[i])

# for i in range(num):
#     print("%s %s %s %s %s\n" %(namelist[i] , addresslist[i] , timelist[i] , phonelist[i] , foodlist[i]))

# 法四
totallist = []
for i in range(22,67,22) :
    for total in soup.find_all("tr" , height = i) :
        totallist.append(total.text)

box = '\n店名\n電話\n地址\n招牌美食\n營業時間\nGPS座標\n'
totallist.remove(box)

l = len(totallist)

for i in range(l):
    print(totallist[i])

# print(l)
# print(totallist)
# print("%d %d %d %d %d\n" %(name , address , time , phone , food))
# print("%d %d %d %d %d %d\n" %(numlist[0] , numlist[1] , numlist[2] , numlist[3] , numlist[4] , numlist[5]))
# print("%d\n" %num)


with open('當地美食.csv', 'w' , encoding='utf-8' , newline='') as csv_file:
    writer = csv.writer(csv_file , delimiter=' ')
    
    for i in range(l):
        writer.writerow([totallist[i]])