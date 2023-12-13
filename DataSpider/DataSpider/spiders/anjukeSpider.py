import re
import time

import scrapy

from ..items import NewHouseItem
from ..items import ErShouHouseItem
from ..items import RentHouseItem


class AnjukespiderSpider(scrapy.Spider):
    name = 'anjukeSpider'
    # allowed_domains = ['wh.fang.anjuke.com']
    # 新房url
    # start_urls = ['https://wh.fang.anjuke.com']
    # 二手房url
    #start_urls = ['https://wuhan.anjuke.com/sale/']
    #租房url
    start_urls=['https://wh.zu.anjuke.com/?from=navigation']

    # 新房页面
    # def parse(self, response):
    #     all_msg = response.xpath('''//div[@class="key-list imglazyload"]/div''')
    #     flag = 0
    #     for i in all_msg:
    #         newhouse = NewHouseItem()
    #         newhouse["community"] = i.xpath('.//span[@class="items-name"]/text()').extract_first()  # 小区名称
    #         try:
    #             area=i.xpath('.//span[@class="list-map"]/text()').extract()[0].replace("\xa0","")
    #             newhouse["city_area"]=re.findall(r'\[(.*?)\]',area)[0]
    #         except:
    #             pass
    #         try:
    #             newhouse["address"] = i.xpath('.//span[@class="list-map"]/text()').extract()[0].replace("\xa0","")  # 小区地址
    #         except:
    #             pass
    #         try:
    #             list1 = i.xpath('.//a[@class="huxing"]/span/text()').extract()[:-1]  # 小区户型
    #             newhouse["house_type"] = "".join(list1)
    #         except:
    #             pass
    #         time.sleep(0.5)
    #         try:
    #             newhouse["house_square"] = i.xpath('.//a[@class="huxing"]/span/text()').extract()[-1].replace('建筑面积：', '')  # 小区建筑面积
    #         except:
    #             pass
    #         try:
    #             newhouse["average_price"] = i.xpath('.//p[contains(@class,"price")]/span/text()').extract_first()   # 小区均价
    #         except:
    #             pass
    #         yield newhouse
    #
    #         # print(newhouse)
    #         # break
    #
    #     for i in range(2, 101):
    #         time.sleep(1)
    #         next_pag_url = f'https://wh.fang.anjuke.com/loupan/all/p{i}/?'
    #         yield scrapy.Request(url=next_pag_url, callback=self.parse)
    #     pass

    # 二手房页面
    # def parse(self, response):
    #     all_msg = response.xpath("//div[@class='property']")
    #     for i in all_msg:
    #         ershouhouse = ErShouHouseItem()
    #         ershouhouse["introduce"] = i.xpath(".//h3/@title").extract_first().replace(" ","")
    #         ershouhouse["house_address"] = i.xpath(
    #             'string(.//div[@class="property-content-info property-content-info-comm"])').extract_first()
    #         ershouhouse["house_floor"] = i.xpath(".//p[@class='property-content-info-text'][3]/text()").extract_first().replace("\n","").replace(" ","")
    #         ershouhouse["house_square"] = i.xpath(".//p[@class='property-content-info-text'][1]/text()").extract_first().replace("\n","").replace(" ","").replace("㎡","")
    #         ershouhouse["ershou_type"] = i.xpath(
    #             'string(.//p[@class="property-content-info-text property-content-info-attribute"])').extract_first().strip().replace(" ","")
    #         ershouhouse["built_time"] = i.xpath(".//p[@class='property-content-info-text'][4]/text()").extract_first().replace("\n","").replace(" ","")
    #         time.sleep(0.5)
    #         ershouhouse["house_orientations"] = i.xpath(
    #             ".//p[@class='property-content-info-text'][2]/text()").extract_first()
    #         ershouhouse["single_price"] = i.xpath(".//p[@class='property-price-average']/text()").extract_first().replace("元/㎡","")
    #         ershouhouse["total_price"]=i.xpath(".//p[@class='property-price-total']/span[1]/text()").extract_first()
    #         yield ershouhouse
    #         # print(ershouhouse)
    #         # break
    #     for i in range(2, 21):
    #         time.sleep(2)
    #         next_pag_url = f'https://wuhan.anjuke.com/sale/p{i}/?'
    #         yield scrapy.Request(url=next_pag_url, callback=self.parse)
    #     pass

    # 租房页面
    def parse(self, response):
        all_msg=response.xpath("//div[@class='list-content']")
        for i in all_msg:
            renthouse=RentHouseItem()
            renthouse["rent_introduce"]=i.xpath(".//div[@class='zu-info']/h3/a/b/text()").extract_first()
            renthouse["rent_address"]=i.xpath("string(.//div[@class='zu-info']/address)").extract_first().strip('\xa0\xa0\n').replace(" ","").replace("\xa0\xa0\n","").replace("\n","")
            renthouse["rent_style"]=i.xpath(".//div[@class='zu-info']/p[1]").xpath('string(.)').extract_first().replace("\n","").replace(" ","").split("|")[0]
            renthouse["month_price"]=i.xpath("div[@class='zu-itemmod']/div[@class='zu-side']/p/strong/b[@class='strongbox']/text()").extract_first().replace(" ","").replace("\n","")
            time.sleep(0.5)
            renthouse["rent_orientations"]=i.xpath(".//div[@class='zu-info']/p[2]/span[2]/text()").extract_first()
            renthouse["rent_square"]=i.xpath(".//div[@class='zu-info']/p[1]/b[3]/text()").extract_first()
            #print(renthouse)
            yield renthouse

        for i in range(2, 20):
            time.sleep(2)
            next_pag_url = f'https://wh.zu.anjuke.com/fangyuan/p{i}/?'
            yield scrapy.Request(url=next_pag_url, callback=self.parse)
        pass
