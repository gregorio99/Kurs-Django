from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy


class Author(models.Model):
    first_name = models.CharField(_("first name"), max_length=20)
    last_name = models.CharField(_("last name"), max_length=50)

    def __str__(self):
        return _("{first_name} {last_name}").format(
            first_name=self.first_name, last_name=self.last_name)

    class Meta:
        # tytaj nie mozna tak zrobic: = _("last_name", "first_name")
        ordering = ("last_name", "first_name")
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Coś w rodzaju rękopisu.
    """
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    category = models.ManyToManyField(BookCategory)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('shelf:book-detail', kwargs={'pk': self.id})


class BookEdition(models.Model):
    """
    Wydanie określonej książki
    """
    book = models.ForeignKey(Book, related_name='editions')
    publisher = models.ForeignKey(Publisher)
    date = models.DateField()
    isbn = models.CharField(max_length=17, blank=True)

    def __str__(self):
        return "{book.title}, {publisher.name}".format(
            book=self.book, publisher=self.publisher)


COVER_TYPES = (
    ('soft', 'soft'),
    ('hard', 'hard'),
    # (wartość_w_bazie, wartość_wyświetlana)
)


class BookItem(models.Model):
    """
    Konkretny egzemplarz
    """
    edition = models.ForeignKey(BookEdition)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition,
                                           cover=self.get_cover_type_display())
