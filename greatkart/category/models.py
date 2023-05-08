from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.CharField(max_length=100,unique=True)
    description=models.TextField(max_length=250,blank=True)
    cat_image=models.ImageField(upload_to="Photos/categories")

    class Meta:
        verbose_name='Category'
        verbose_name_plural='categorie'

    def get_url(self):
        return "http://127.0.0.1:8000/store/" + str(self.slug)

    def __str__(self):
        return self.category_name

