from django.db import models

class Klass(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

class Mehmonhona(models.Model):
    name = models.CharField(max_length=100)
    star = models.IntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Travel(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    period = models.DateTimeField(auto_now_add=True)
    price = models.PositiveIntegerField()
    klass = models.ForeignKey(Klass,on_delete=models.CASCADE,related_name='klass')
    mehmonhona = models.ForeignKey(Mehmonhona,on_delete=models.CASCADE,related_name='mehmonhona')

    def __str__(self):
        return self.name
    