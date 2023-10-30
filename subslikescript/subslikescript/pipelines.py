import pymongo
import sqlite3

class MongodbPipeline:
    collection_name = 'transcripts'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('<enter mongo db atlas connection string here>')
        self.db = self.client['Business']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
    

class SQLitePipeline:

    def open_spider(self, spider):
        self.client = sqlite3.connect('transcripts.db')
        self.conn = self.client.cursor()

        try:
            self.conn.execute('''
                            CREATE TABLE transcripts(
                                title TEXT,
                                plot TEXT,
                                script TEXT,
                                url TEXT
                            )
                          ''')
            self.client.commit()
        except sqlite3.OperationalError:
            pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.conn.execute('''
                            INSERT INTO transcripts (title, url, plot, script) VALUES (?, ?, ?, ?)
                          ''', (
                              item.get('title'),
                              item.get('url'),
                              item.get('plot'),
                              item.get('script'),
                          ))
        self.client.commit()
        return item

