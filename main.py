import requests
from bs4 import BeautifulSoup
import random
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service

# 获取图书信息
# 参数：
#   图书链接
# 返回：
#   无返回值，调用存储函数存储数据到数据库
def getBookInfo(url,data):
    option = webdriver.ChromeOptions()
    option.add_argument(r'--user-data-dir=C:\Users\NUDTer\AppData\Local\Google\Chrome\User Data')
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    try:
        driver.set_window_size(1000,30000)
        driver.get(url)
        time.sleep(5)
        # 存储本书信息
        book = []
        # 图书标题
        bookName = driver.find_element(By.XPATH, '//*[@id="product_info"]/div[1]/h1').text.strip()
        # 图书副标题（促销语）
        bookViceName = driver.find_element(By.XPATH, '//*[@id="product_info"]/div[1]/h2/span[1]').text.strip()
        # 图书作者
        bookAuthor = driver.find_element(By.XPATH, '//*[@id="author"]/a[1]').text.strip()
        # 图书出版社
        bookPress = driver.find_element(By.XPATH, '//*[@id="product_info"]/div[2]/span[2]/a').text.strip()
        # 价格
        bookPrice = driver.find_element(By.XPATH, '//*[@id="e-book-price"]').text.strip()
        # 编辑推荐理由
        bookRecommend = driver.find_element(By.XPATH, '//*[@id="abstract"]/div[2]/p').text.strip()
        # 图书简介
        bookIntro = driver.find_element(By.XPATH, '//*[@id="content-show"]').text.strip()
        # 作者简介
        authorIntro = driver.find_element(By.XPATH, '//*[@id="authorIntroduction"]/div[2]/p').text.strip()
        # 图书目录
        bookCatalog = driver.find_element(By.XPATH, '//*[@id="catalog-show"]').text.strip()
        # 媒体评价
        #mediaComment = driver.find_element(By.XPATH, '//*[@id="mediaFeedback-show"]/text()[1]').text.strip()
        # 存储数据
        book.append(bookName)
        book.append(bookViceName)
        book.append(bookAuthor)
        book.append(bookPress)
        book.append(bookPrice)
        book.append(bookRecommend)
        book.append(bookIntro)
        book.append(authorIntro)
        book.append(bookCatalog)
        #book.append(mediaComment)
        mediaComment = "暂无评价"
        print(f"获取数据成功:{bookName,bookViceName,bookAuthor,bookPress,bookPrice,bookRecommend,bookIntro,authorIntro,bookCatalog,mediaComment}")
        data.append(book)
        return data
    except Exception as e:
        print(e)
    finally:
        driver.quit()  # 确保关闭浏览器









def getBookInfo_old(url):
    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    ]

    url = "https://product.dangdang.com/29659154.html"
    headers = {
        'User-Agent':random.choice(USER_AGENTS),
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2'
        }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    # 保存获取的HTML内容到文件
    with open("output.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
    exit(0)
    bookInfo1 = soup.find("div", class_="sale_box_left",id="product_info")
    bookInfo2= soup.find("div",class_="product_content clearfix").find("div",class_="t_box",id="product_tab",ddaccregion="slist").find("div",class_="t_box_left",id="detail_all",dd_name="商品详情").find("div",class_="section",id="detail")
    print(bookInfo2)
    exit(0)

    # 图书标题
    bookName = bookInfo1.find("h1").text.strip()
    # 图书副标题（促销语）
    bookViceName = bookInfo1.find("span",class_="head_title_name").text.strip()
    # 图书作者
    bookAuthor = bookInfo1.find("span", class_="t1",id="author").text.strip()
    # 图书出版社
    bookPress = bookInfo1.find("span", class_="t1",dd_name="出版社").text.strip()
    # 价格
    bookPrice = bookInfo1.find("a", id="e-book-price",dd_name="电子书价").text.strip()
    try:
        # # 图书简介
        # bookIntro = bookInfo2.find("span", id="content-all").text.strip()
        # # 作者简介
        # authorIntro = bookInfo2.find("span", id="authorIntroduction-all").text.strip()
        # # 图书目录
        # bookCatalog = bookInfo2.find("span", id="catalog-show")
        # 图书前言
        bookPreface = bookInfo2.find("div", id="preface",class_="section").find("div",class_="descrip").text.strip()
        print(bookPreface)
    except Exception as e:
        print(e)

# 通过关键字获取页面内容
# 参数：
#   关键字
#   页码（默认1）
# 返回：
#   无返回值，调用函数获取具体图书页面的图书信息
def getPage(keyWord,index=1):
    url = f"http://search.dangdang.com/?key={keyWord}&act=input&page_index={index}"
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # 获取当前页面的图书列表的链接信息
    bookList = soup.find("div", id="search_nature_rg")
    data = [['图书标题', '图书副标题', '图书作者', '图书出版社', '价格', '编辑推荐理由', '图书简介', '作者简介', '图书目录', '媒体评价']]
    if bookList:
        links = bookList.find_all('a', href=True)
        oldWeb = ""
        for link in links:
            linkUrl = "https:"+link['href']
            # 判断其是否属于图书链接
            if linkUrl.endswith(".html"):
                # 判断是否获取重复链接
                if oldWeb.find(linkUrl)!=-1:
                    continue
                print("获取链接："+linkUrl)
                data = getBookInfo(linkUrl,data)
                # 更新旧链接
                oldWeb = linkUrl
                time.sleep(1)

    else:
        print("没有找到指定的<div>标签")

    # 递归调用，获取后续页面的内容
    for i in range(index+1,101):
        getPage(keyWord,i)


# 调用函数
start_time = time.time()
keyWord = book_categories = [
    "科幻小说",
    "奇幻小说",
    "悬疑小说",
    "惊悚小说",
    "恐怖小说",
    "爱情小说",
    "历史小说",
    "现实主义小说",

    "自传",
    "传记",
    "历史",
    "科学",
    "哲学",
    "心理学",
    "社会学",
    "经济学",
    "政治学",
    "艺术",
    "旅行",
    "烹饪",
    "健康与健身",

    "绘本",
    "儿童小说",
    "青少年小说",

    "教科书",
    "学术研究",
    "教育理论",

    "宗教文本",
    "灵性指导",

    "诗歌",
    "剧本",

    "漫画",
    "图像小说",

    "自助指南",
    "励志书籍"
]
for i in keyWord:
    getPage(i)
# 记录程序结束时间
end_time = time.time()

# 计算总运行时间
total_time = end_time - start_time
print(f"程序总运行时间: {total_time:.2f} 秒")
