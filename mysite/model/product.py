from django.db import models

class Product(models.Model):

    @property
    def name(self):
        return self.name

    @name.setter
    def setName(self, name):
        self.name = name