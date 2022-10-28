class Noticia():
    def __init__(self, id, title =None, description=None):
        self.id = id
        self.title = title
        self.description = description

    def to_json(self):
        return {
            'ID':self.id,
            'Título':self.title,
            'Descripción':self.description
        }