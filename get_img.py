from icrawler.builtin import BingImageCrawler
crawler = BingImageCrawler(storage={"root_dir": "images"})
crawler.crawl(keyword="fasion", max_num=20)