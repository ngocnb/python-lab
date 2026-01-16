import feedparser
from bs4 import BeautifulSoup
from models.post import PostModel  # Importing from models.post

class VnExpress:
    def __init__(self, rss_url):
        self.rss_url = rss_url
    
    def extract_items(self):
        feed = feedparser.parse(self.rss_url)
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

    def get_content(self, url):
        response = feedparser.parse(url)
        content = ""
        if 'entries' in response and len(response.entries) > 0:
            description = response.entries[0].description
            soup = BeautifulSoup(description, 'html.parser')
            content_tag = soup.find('article', class_='fck_detail')
            if content_tag:
                content = content_tag.get_text(separator="\n")
        return content

    def check_and_process_hot_news(self):
        try:
            model = PostModel()  # Using PostModel from models.post
            items = self.extract_items()

            for item in items:
                link = item['link']
                if not model.item_exists(link):
                    item["content"] = self.get_content(link)
                    model.insert_item(item)

                model.update_is_hot(link)

            model.commit()
            model.close()
            print("Data has been successfully checked and processed in MySQL database.")
        except Exception as e:
            print(f"Error: {e}")

    def save(self):
        try:
            model = PostModel()  # Using PostModel from models.post
            items = self.extract_items()

            for item in items:
                item["content"] = self.get_content(link)
                model.insert_item(item)

            model.commit()
            model.close()
            print("Data has been successfully saved to MySQL database.")
        except Exception as e:
            print(f"Error: {e}")
