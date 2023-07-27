import feedparser

def extract_rss_items(rss_url):
    feed = feedparser.parse(rss_url)
    items = []
    for entry in feed.entries:
        item = {
            'title': entry.title,
            'link': entry.link,
            'published_date': entry.published,
            'description': entry.description,
        }
        items.append(item)
    return items

rss_url = "https://vnexpress.net/rss/tin-moi-nhat.rss"
rss_items = extract_rss_items(rss_url)

for index, item in enumerate(rss_items, start=1):
    print(f"Item {index}:")
    print(f"Title: {item['title']}")
    print(f"Link: {item['link']}")
    print(f"Published Date: {item['published_date']}")
    print(f"Description: {item['description']}")
    print("=" * 50)