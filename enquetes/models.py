from django.db import models

# Create your models here.

class Enquete():
    def __init__(self, enquete_id, texto="", data_publicacao=""):
        self.enquete_id = enquete_id
        self.texto = texto
        self.data_publicacao = data_publicacao
