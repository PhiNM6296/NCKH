import scrapy


class LinkPdfSpider(scrapy.Spider):
    name = "link_pdf"
    allowed_domains = ["www.hnx.vn"]
    start_urls = ["https://www.hnx.vn/cophieu-etfs/chi-tiet-chung-khoan-ny-AAV.html?_des_tab=2"]

    def parse(self, response):
        pass
