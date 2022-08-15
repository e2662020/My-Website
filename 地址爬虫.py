import requests,bs4,time,logging
from logging import info,warn,error
logging.basicConfig(filename='logger.log', level=logging.INFO)

n1 = []
n2 = []
info("程序正常运行中")
try:    
    while True:
        response = requests.get("https://msedge-core.github.io/index.html")
        response.encoding = "UTF-8"
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        #作答区域2：补充下一行代码，选取标签名为a，class属性值为title的标签
        data = soup.find_all(name="div", class_="button")
        localtime = '\n---'+str(time.asctime( time.localtime(time.time()) ))+'---'
        for n in data:
            #作答区域3：补充下一行代码，打印新闻文字内容
            info("成功访问到网站")
            n2.append(n)
        if n != n1:
            n1 = []
            n1.append(n2)
            
        with open("lite.txt", "w", encoding="utf-8") as file:
            file.write(str(n1))
            info("成功写入文件")
        n2 = []
        time.sleep(10)
        info("成功完成，等待10秒下一个")
except:
    error("程序错误")

        
