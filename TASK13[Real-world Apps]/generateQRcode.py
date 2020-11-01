import pyqrcode

github = "https://github.com/muskanjindal24"
blog = "https://medium.com/@muskanjindal242"
url1 = pyqrcode.create(github)
url2 = pyqrcode.create(blog)
url1.png('muskan_github.png', scale=6)
url2.png('muskan_blog.png', scale=6)