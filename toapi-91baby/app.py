from toapi import Api
from items.hotbook import HotBook
from items.book import Book
from settings import MySettings

api = Api('https://news.ycombinator.com', settings=MySettings)
api.register(HotBook)
api.register(Book)

if __name__ == '__main__':
    api.serve()
