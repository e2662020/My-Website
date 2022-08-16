import requests,bs4,time,logging
from logging import info,warn,error
logging.basicConfig(filename='logger.log', level=logging.INFO)


try:    
    n1 = []
    n2 = []
    info("程序正常运行中")
    print("程序正常运行中")
    while True:
        response = requests.get("https://msedge-core.github.io/store.html")
        response.encoding = "UTF-8"
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        #作答区域2：补充下一行代码，选取标签名为a，class属性值为title的标签
        data = soup.find_all(name="div", id="downloadButton")
        localtime = '\n---'+str(time.asctime( time.localtime(time.time()) ))+'---'

        #作答区域3：补充下一行代码，打印新闻文字内容
        info("成功访问到网站")
        n2.append(data)
        if n2 != n1:
            n1 = []
            n1.append(n2)
    
        with open("lite.txt", "w", encoding="utf-8") as file:
            n3 = str(n1["onclick"])+"\n"
            file.write(n3)
            info("成功写入文件")
        n2 = []
        time.sleep(10)
        info("成功完成，等待10秒下一个")
except Exception as e:
    error(e)
    print("程序错误\n")

        
