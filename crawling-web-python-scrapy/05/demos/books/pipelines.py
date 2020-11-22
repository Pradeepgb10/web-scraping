#3 - item pipelines
#4 - drop unwanted items

#4
from scrapy.exceptions import DropItem

class BooksPrice(object):
    def process_item(self, item, spider):
        price = item['price'].replace('£', '')
        if float(price) > 50:
            item['price'] = 'Expensive'
        else:
            item['price'] = price
        return item

class CheckAsViable(object):
    def process_item(self, item, spider):
        if item['price'] != 'Expensive':
            print('\r\n Book found ->')
            print('title: ' + item['title'])
            print('price: ' + item['price'])
            print('imageurl: ' + item['imageurl'])
            print('bookurl: ' + item['bookurl'])
        #4
        else:
            raise DropItem()
        return item