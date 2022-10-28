class Comment():
    def __init__(self, id, comment):
        self.id = id
        self.comment = comment

    def to_json(self):
        return {
            'ID': self.id,
            "Comentario":self.comment
        }

class FullNotice():
    def __init__(self, id, title, description, comment):
        self.id = id
        self.title = title
        self.description = description
        self.comment = comment

    def to_json(self):
        return {
            'ID': self.id,
            'Títutlo': self.title,
            'Descripción': self.description,
            'Comentario': self.comment
        }
