import pymysql.cursors


class Cursor(object):
    """
    不做连接池处理，如需要连接池，后期可以用openResty或者dba自己的中间件
    """
    def __init__(self, conn):
        self.conn = pymysql.connect(
            host=conn.get('host'),
            user=conn.get('user'),
            password=conn.get('password'),
            db=conn.get('name'),
            port=conn.get('port'),
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.lazy_conn = pymysql.connect(
            host=conn.get('host'),
            user=conn.get('user'),
            password=conn.get('password'),
            db=conn.get('name'),
            port=conn.get('port'),
            charset='utf8',
            cursorclass=pymysql.cursors.SSDictCursor
        )

    def fetch_one(self, sql, *params):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, *params)
                result = cursor.fetchone()
                return result
        finally:
            self.conn.close()

    def fetch_all(self, sql, *params):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, *params)
                result = cursor.fetchall()
                return result
        finally:
            self.conn.close()

    def execute(self, sql, *params):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql, *params)
            self.conn.commit()
            result = cursor.fetchall()
            return result
        finally:
            self.conn.close()

    def lazy_fetch_batch(self, query, batch_size=1):
        try:
            with self.lazy_conn as cursor:
                cursor.execute(query)
                while True:
                    next_rows = cursor.fetchmany(batch_size)
                    if not next_rows:
                        break
                    yield next_rows
        finally:
            self.conn.close()

    def lazy_fetch_one(self, query, size=1):
        try:
            with self.lazy_conn as cursor:
                cursor.execute(query)
                while True:
                    next_rows = cursor.fetchmany(size)
                    if not next_rows:
                        break
                    for row in next_rows:
                        yield row
        finally:
            self.conn.close()
