# -*- coding: utf-8 -*-
import scrapy


class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'
    allowed_domains = ['amazon.in']
    start_urls = ['http://amazon.in/']

    myBaseUrl  ="https://www.amazon.in/OnePlus-Midnight-Black-128GB-Storage/product-reviews/B07DJHY82F/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber="

    start_urls = []

    for i in range(1,101):
        start_urls.append(myBaseUrl + str(i))

    def parse(self, response):
            data = response.css('#cm_cr-review_list')

            # Collecting product star ratings
            star_rating = data.css('.review-rating')

            # Collecting user reviews
            comments = data.css('.review-text')
            count = 0

            # Combining the results
            for review in star_rating:
                yield{'stars': ''.join(review.xpath('.//text()').extract()),
                      'comment': ''.join(comments[count].xpath(".//text()").extract())
                     }
                count=count+1


