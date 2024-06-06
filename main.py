import requests
# 注意 这个函数如何导入的
from send_email import send_email
topic = 'tesla'
# 这个地址 调不同
# api_key = '890603a55bfa47048e4490069ebee18c'
# url = "https://newsapi.org/v2/everything?q=f'{topic}'&sortBy=publishedAt' \
#       '&apiKey=890603a55bfa47048e4490069ebee18c&language=en"
#
# request = requests.get(url)
# print('request',request)

# 改个思路 模拟 拿到 request 数据
request = {
    "status": "ok",
    "totalResults": 3,
    "articles": [
        {
            "source": {
                "id": "1",
                "name": "Fake News Network"
            },
            "author": "John Doe",
            "title": "特斯拉发布最新款电动汽车",
            "description": "特斯拉公司今天发布了他们最新款的电动汽车，预计将在下个月开始交付。",
            "url": "http://fakenews.com/article1",
            "urlToImage": "http://fakenews.com/images/article1.jpg",
            "publishedAt": "2024-06-05T08:00:00Z",
            "content": "特斯拉公司今天发布了他们最新款的电动汽车，预计将在下个月开始交付。这款新车将采用先进的自动驾驶技术，并配备了最新款的电池技术，让用户可以享受更长的续航里程。"
        },
        {
            "source": {
                "id": "2",
                "name": "Tesla News"
            },
            "author": "Jane Smith",
            "title": "特斯拉宣布在中国建设新工厂",
            "description": "特斯拉公司计划在中国建设一座新的工厂，以满足对电动汽车的日益增长的需求。",
            "url": "http://fakenews.com/article2",
            "urlToImage": "http://fakenews.com/images/article2.jpg",
            "publishedAt": "2024-06-04T10:30:00Z",
            "content": "特斯拉公司计划在中国建设一座新的工厂，以满足对电动汽车的日益增长的需求。该工厂预计将在未来两年内投入使用，并将创造大量就业机会。"
        },
        {
            "source": {
                "id": "3",
                "name": "Tech World"
            },
            "author": "Alan Johnson",
            "title": "特斯拉推出新的自动驾驶软件更新",
            "description": "特斯拉公司发布了一项新的自动驾驶软件更新，提供更快、更安全的驾驶体验。",
            "url": "http://fakenews.com/article3",
            "urlToImage": "http://fakenews.com/images/article3.jpg",
            "publishedAt": "2024-06-03T15:45:00Z",
            "content": "特斯拉公司发布了一项新的自动驾驶软件更新，提供更快、更安全的驾驶体验。这项更新将通过无线网络自动安装到特斯拉车辆上，让用户可以立即体验到最新的驾驶技术。"
        }
    ]
}

content = request

body = ""
# 限制 接收几条
for article in content['articles'][:2]:
    # 检查不是 None  不然会报错
    if article['title'] is not None:
        body = "Subject: Today's news" + '\n' + body + article['title'] + '\n' + article['content'] + '\n'\
               + article['url'] + 2 * '\n'

# UTF-8编码来确保字符串中的非ASCII字符能够正确地被处理
body = body.encode('utf-8')
send_email(message=body)
