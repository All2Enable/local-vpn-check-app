from django.db import models

#for future use, when there will be many servers
class Server(models.Model):
    name = models.CharField(max_length=30)

    def __srt__(self):
        return self.name
