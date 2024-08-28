from icrawler.builtin import GoogleImageCrawler
import sys
import os
def crawl_images(keyword, max_num, storage_dir):
    if not os.path.exists(storage_dir):
        os.makedirs(storage_dir)
    crawler = GoogleImageCrawler(storage={'root_dir': storage_dir})
    crawler.crawl(keyword=keyword, max_num=max_num)
if len(sys.argv) < 4:
    print("Usage: python script_name.py <keyword> <number> <outputfile>")
    sys.exit(1)
name=sys.argv[1]
number=int(sys.argv[2])
outputfile=sys.argv[3]
crawl_images(name,number, storage_dir=os.path.join(outputfile))

