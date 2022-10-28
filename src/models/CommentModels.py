from .entities.comentario import Comment, FullNotice
from database.db import get_connection

class CommentModels():
    @classmethod
    def add_comment(self, id, comment):
        try: 
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO comentarios ("ID", "Comentario")
                                VALUES (%s, %s) """, (id, comment))
                
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as e:
            raise Exception(e)


    @classmethod
    def get_fullnews(self):
        try: 
            connection = get_connection()
            full_notice = []
            with connection.cursor() as cursor:
                cursor.execute(""" SELECT "noticias"."ID", "noticias"."Título", "noticias"."Descripción", "comentarios"."Comentario"  
                                    FROM noticias LEFT JOIN comentarios ON  "noticias"."ID" = "comentarios"."ID"  """)

                result_set = cursor.fetchall()
                for row in result_set:
                    notice = FullNotice(row[0], row[1], row[2], row[3])
                    full_notice.append(notice.to_json())
                
            connection.close()
            return full_notice
        except Exception as e:
            raise Exception(e)