import time
import feedparser
import html2text

def main():
    #feeds = {title, published}
    feeds = {}
    flag = 0
    while True:
        with open("rss-links.txt","r") as links_rss:
            for line in links_rss:
                time.sleep(2)
                feeded = feedparser.parse(line)
                title = feeded.entries[0].title
                date_published = feeded.entries[0].published
                #print(feeds.keys())
                if feeded.feed.title not in feeds.keys():
                    feeds[feeded.feed.title] = ""

               # print("###")
               # print(feeds)
               # print(date_published)
               # print(f"{feeds[feeded.feed.title]} == {date_published}")
               # print(feeds[feeded.feed.title] == date_published)
               # print(feeded.feed.title in feeds.keys())
                if feeded.feed.title in feeds.keys() and feeds[feeded.feed.title] == date_published:
                    pass

                elif feeded.feed.title in feeds.keys() :
                    print("###################")
                    print(feeded.feed.title)
                    print(feeded.entries[0].title)
                    print(html2text.html2text(feeded.entries[0].description))
                    feeds[feeded.feed.title] = date_published
                    print("###################")


if __name__ == "__main__":
    main()
