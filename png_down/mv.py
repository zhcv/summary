import re
import requests
import urllib.request

def getHtml(url):
    page = requests.get(url)
    html = page.text
    return html

def mv(url):
    #分离，获取id
    mvid = url.split('/')[-1]
    #下载链接url组合
    url = 'http://www.yinyuetai.com/insite/get-video-info?flex=true&videoId={}'.format(mvid)
    #网页数据请求
    html = getHtml(url)
    print(html)
    #正则表达式，查找符合条件的下载链接
    reg = r'http://\w*?\.yinyuetai\.com/uploads/videos/common/.*?(?=&br)'
    pattern = re.compile(reg)
    findlist = re.findall(pattern, html)
    #获取最后一个会员超清下载链接
    print(findlist[-1])
    mvurl = findlist[-1]

    #分离，提取后缀，保存方式mp4
    mp4 = mvurl.split('?')[0]
    mp4 = mp4[-4:]

    print('正在下载MV')
    urllib.request.urlretrieve(mvurl, '2{}'.format(mp4))


if __name__ == '__main__':
    #当前mv所在的url
    url = "http://v.yinyuetai.com/video/3284044?vid=3266563"
    mv(url)
