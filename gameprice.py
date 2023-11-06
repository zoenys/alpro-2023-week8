import scrapy

class GamePrice(scrapy.Spider):
    name = "gameprice"
    start_urls = ['https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/1']

    def parse(self, response):
        for item in response.css('div.psw-product-tile.psw-interactive-root'):
            title = item.css('span.psw-t-body.psw-c-t-1.psw-t-truncate-2.psw-m-b-2::text').get()
            price = item.css('span.psw-m-r-3::text').get().replace('\xa0', '')

            yield {
                'title': title,
                'price': price,
            }

        current_page = int(response.url.split('/')[-1])
        next_page = f'https://store.playstation.com/en-id/category/05a2d027-cedc-4ac0-abeb-8fc26fec7180/{current_page + 1}'
        
        # Check if the next button exists
        next_button = response.css(f'button[name=""][value="{current_page + 1}"]:disabled')
        if len(next_button) == 0:
            yield response.follow(next_page, callback=self.parse)


