import time
import feedparser
import html2text

# if the word is identified, the entire message will be printed red

alerting_words = []
def init_alerting_words(filename_path):
    with open(filename_path, "r")as f:
        for line in f:
            line_no_newline = line.replace("\n", "")
            alerting_words.append(line_no_newline)
color = {
        "RED":'\033[31m',
        "GREEN":'\033[32m',
        'WHITE':'\033[37m'
        }

def pre_print(text, list_of_words):
    returned = text
    for word in list_of_words:
        if word in text:
            return f"{color['RED']}{text}{color['WHITE']}"
    return text

def main():
    feeds = {}
    #assuming the file exists, RTFM
    init_alerting_words("trigger_words.txt")
    print(alerting_words)
    while True:
        with open("rss-links.txt","r") as links_rss:
            for line in links_rss:
                time.sleep(2)
                feeded = feedparser.parse(line)
                title = feeded.entries[0].title
                date_published = feeded.entries[0].published
                if feeded.feed.title not in feeds.keys():
                    feeds[feeded.feed.title] = ""
                if feeded.feed.title in feeds.keys() and feeds[feeded.feed.title] == html2text.html2text(feeded.entries[0].description):
                    time.sleep(10)
                    pass

                elif feeded.feed.title in feeds.keys() :
                    print(feeded.feed.title)
                    print(date_published)
                    print(feeded.entries[0].title)
                    not_functional_var = html2text.html2text(feeded.entries[0].description)
                    print(pre_print(not_functional_var,alerting_words))
                    feeds[feeded.feed.title] = html2text.html2text(feeded.entries[0].description)
                    print("###################")



if __name__ == "__main__":
    main()
