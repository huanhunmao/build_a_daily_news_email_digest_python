import requests

url = 'https://i2.chuimg.com/f6b53648250311e7bc9d0242ac110002_1280w_1024h.jpg' \
      '?imageView2/1/w/640/h/520/q/75/format/jpg'
request = requests.get(url)

print('request', request)  # request <Response [200]>

# 这样能拿到图片 并下载下下来图片  名字就叫 image.jpg
with open('image.jpg', 'wb') as file:
    file.write(request.content)