from django.db import models
from django.template.defaultfilters import slugify

#  Book.objects.all()
#  Book.objects.first()
#  Book.objects.last()
#  Book.objects.get(title='Pan Tadeusz')
#  Book.objects.filter(title='Pan Tadeusz')
#  Book.objects.filter(title__iexact='pan tadeusz')
#  Book.objects.filter(title__istartswith='pan')
#  Book.objects.filter(year__lt=1950)
#


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    pages = models.SmallIntegerField()
    slug = models.SlugField(null=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.slug:
            self.slug = slugify(self.title)

        return super().save(
            force_insert=force_insert, force_update=force_update, using=force_update, update_fields=update_fields
        )
