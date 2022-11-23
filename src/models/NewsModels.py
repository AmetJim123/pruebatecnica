from .entities.noticia import Noticia
from database.db import get_connection

class NewsModels():

    @classmethod
    def add_news(self, news):
        try:
            connection=get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO noticias("ID", "Título", "Descripción")
                                VALUES(%s, %s, %s)""", (news.id, news.title, news.description))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)

    @classmethod
    def get_news(self):

        try: 
            connection = get_connection()
            all_news = []

            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM noticias""")

                result_set = cursor.fetchall()

                for row in result_set:
                    news = Noticia(row[0], row[1], row[2])
                    all_news.append(news.to_json())

            connection.close()
            return all_news
        except Exception as e:
            raise Exception(e)


    @classmethod
    def get_new(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""SELECT * FROM noticias 
                                WHERE "ID"=%s """,
                                (id,))
            
                row = cursor.fetchone()
                news = None
                if row != None:
                    news = Noticia(row[0], row[1], row[2])
                    news = news.to_json()
                
            connection.close()
            return news
        except Exception as e:
            raise Exception(e)
    

    @classmethod
    def update_news(self, news):
        try:
            connection  = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE noticias SET "Título"= %s, "Descripción"= %s
                WHERE "ID"=%s """, (news.title, news.description, news.id))

                affected_rows = cursor.rowcount
                connection.commit()
            
            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)


    @classmethod
    def delete_news(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""DELETE FROM noticias WHERE "ID"=%s """, (id,))

                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)