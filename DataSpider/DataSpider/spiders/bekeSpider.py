import copy
import time

import scrapy
from ..items import NewHouseItem
from ..items import RentHouseItem
from ..items import ErShouHouseItem
class BekespiderSpider(scrapy.Spider):
    name = 'bekeSpider'
    allowed_domains = ['wh.fang.ke.com']
    #新房url
    start_urls = ['https://wh.fang.ke.com/loupan/']

    #二手房url
    #start_urls=['https://wh.ke.com/ershoufang/']

    #租房url
    start_urls=['https://wh.zu.ke.com/zufang/']
    page=2

    #新房
    # def parse(self, response):
    #     houseList = response.xpath('//div[@class="resblock-list-container clearfix"]/ul[2]/li')
    #     n_url = "https://wh.fang.ke.com/loupan/pg{}/".format(self.page)
    #     for i in houseList:
    #         bknewhouse=NewHouseItem()
    #         # bknewhouse["community"]=i.xpath(".//div[@class='resblock-desc-wrapper']/div[@class='resblock-name']/a/text()").extract_first()
    #         # bknewhouse["city_area"]=i.xpath(".//div[@class='resblock-desc-wrapper']/a[1]/text()").extract()[1].split("/")[0]
    #         # bknewhouse["address"]=i.xpath(".//div[@class='resblock-desc-wrapper']/a[1]/text()").extract()[1].split("/")[2].strip("\n\t\t")
    #         house_type=i.xpath(".//div[@class='houseInfo']/a[2]").xpath('string(.)').extract()
    #         print(house_type)
    #         # bknewhouse["house_square"]=i.xpath(".//div[@class='resblock-desc-wrapper']/a[2]/span[@class='area']/text()").extract_first()
    #         # bknewhouse["average_price"]=i.xpath(".//div[@class='resblock-desc-wrapper']/div[@class='resblock-price']/div[@class='main-price']/span[1]/text()").extract_first()
    #         #yield bknewhouse
    #     if self.page < 21:
    #         time.sleep(2)
    #         yield scrapy.Request(url=n_url, dont_filter=True, callback=self.parse)
    #         self.page += 1
    #     pass

    #二手房(over)
    # def parse(self, response):
    #     all_msg=response.xpath("//li[@class='clear']/div[@class='info clear']")
    #     n_url = "https://wh.fang.ke.com/ershoufang/pg{}/".format(self.page)
    #     #print(all_msg)
    #     for i in all_msg:
    #         bkershouhouse=ErShouHouseItem()
    #         bkershouhouse["introduce"]=i.xpath("div[@class='title']/a/text()").extract_first()
    #         bkershouhouse["house_address"]=i.xpath("div[@class='address']/div[@class='flood']/div[@class='positionInfo']/a/text()").extract_first()
    #         bkershouhouse["total_price"] = i.xpath(
    #             "div[@class='address']/div[@class='priceInfo']/div[@class='totalPrice totalPrice2']/span[1]/text()").extract_first().strip()
    #         bkershouhouse["single_price"] = i.xpath(
    #             "div[@class='address']/div[@class='priceInfo']/div[@class='unitPrice']/span[1]/text()").extract_first().strip().replace("元/平","").replace(",","")
    #
    #         #处理span标签
    #         str1=i.xpath("div[@class='address']/div[@class='houseInfo']").xpath('string(.)').extract()[0].strip('\n').replace(" ","")
    #         list1 = str1.split('|')
    #         list2=[str(i).replace('\n','') for i in list1]
    #         #print(list2)
    #         conut=len(list2)
    #         if conut==5:
    #             bkershouhouse["built_time"]=list2[1]
    #             bkershouhouse["house_floor"]=list2[0]
    #         else:
    #             bkershouhouse["built_time"]=''
    #             bkershouhouse["house_floor"] = list2[1]
    #         bkershouhouse["house_orientations"] = list2[-1]
    #         bkershouhouse["house_square"]=list2[-2].replace("平米","")
    #         bkershouhouse["ershou_type"]=list2[-3]
    #
    #         yield bkershouhouse
    #     if self.page < 3:
    #         time.sleep(5)
    #         yield scrapy.Request(url=n_url, dont_filter=True, callback=self.parse)
    #         self.page += 1
    #     pass



    #租房(完成）
    def parse(self, response):
        print(response.url)
        node_list = response.xpath('//div[@class="content__list--item--main"]')
        print(len(node_list))
        item = RentHouseItem()
        for node in node_list:
            item["rent_introduce"] = node.xpath("./p[1]/a/text()").extract_first().strip()
            item["month_price"] = node.xpath(
                './span[@class="content__list--item-price"]/em/text()').extract_first().strip()
            infolist=node.xpath("./p[2]").xpath('string(.)').extract()[0].strip("\n").replace(" ","")
            time.sleep(0.5)
            list1=infolist.split("/")
            list2 = [str(i).replace('\n', '') for i in list1]

            #print(list2)
            count=len(list2)
            if count==6:
                item["rent_square"]=list2[-4].replace("㎡","")
                item["rent_orientations"]=list2[-3]
                item["rent_address"] = list2[1].split("-")[-1]
                item["rent_style"]=list2[-2]
            elif count==5:
                item["rent_square"]=list2[-4].replace("㎡","")
                item["rent_orientations"]=list2[-3]
                item["rent_address"]=list2[0].split("-")[-1]
                item["rent_style"] = list2[-2]
            elif count==4:
                item["rent_square"]=list2[-3].replace("㎡","")
                item["rent_orientations"]=''
                item["rent_address"]=''
                item["rent_style"] = list2[-1]
            else:
                item["rent_square"]=''
                item["rent_orientations"]=''
                item["rent_address"]=''
                item["rent_style"]=''
        yield item
    #
    #     #逻辑是先获取下一页的地址，判断是否有，有的话则请求下一页
        if self.page < 20:
            time.sleep(2)
            next_url = 'https://jn.zu.ke.com/zufang/pg{}/#contentList'.format(self.page)
            self.page += 1
            yield scrapy.Request(next_url,dont_filter=True ,callback=self.parse)






