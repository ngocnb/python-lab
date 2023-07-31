import mysql.connector
from db_config import DB_CONFIG

class Post:
    def __init__(self):
        self.connection = self._connect_to_database()
        self.cursor = self.connection.cursor()

    def _connect_to_database(self):
        return mysql.connector.connect(**DB_CONFIG)

    def _close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection.is_connected():
            self.connection.close()

    def _execute_query(self, query, values=None):
        if values:
            self.cursor.execute(query, values)
        else:
            self.cursor.execute(query)

    def item_exists(self, link):
        query = "SELECT COUNT(*) FROM posts WHERE link = %s"
        self.cursor.execute(query, (link,))
        count = self.cursor.fetchone()[0]
        return count > 0

    def insert_item(self, item):
        link = item['link']
        if not self.item_exists(link):
            content = item.get('content', '')
            query = "INSERT INTO posts (title, link, published_date, description, content) " \
                    "VALUES (%s, %s, %s, %s, %s)"
            values = (item['title'], link, item['published_date'], item['description'], content)
            self._execute_query(query, values)

    def update_is_hot(self, link):
        query = "UPDATE posts SET is_hot = 1 WHERE link = %s"
        self._execute_query(query, (link,))

    def commit(self):
        self.connection.commit()

    def close(self):
        self._close_connection()