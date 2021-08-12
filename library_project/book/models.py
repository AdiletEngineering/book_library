from django.db import models


class City(models.Model):
    name = models.CharField("name of city", max_length=50)

    def __str__(self):
        return self.name


class Reader(models.Model):
    name = models.CharField("name of reader", max_length=50)
    last_name = models.CharField("last name of reader", max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, related_name='addresses')
    reader = models.ForeignKey(to=Reader, on_delete=models.DO_NOTHING, related_name='addresses')
    street = models.CharField('name of street', max_length=100)
    house = models.CharField('number of house', max_length=10)
    apartment = models.CharField('number of apartment', max_length=10, default=None)

    def __str__(self):
        return f'{self.street}, {self.house}'


class Card(models.Model):
    reader = models.ForeignKey(to=Reader, on_delete=models.DO_NOTHING, related_name='cards')
    card_number = models.IntegerField('Номер читательского билета')
    password = models.CharField("card password", max_length=4)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Operation(models.Model):
    reader = models.ForeignKey(to=Reader, on_delete=models.DO_NOTHING, related_name='operations')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    close_date = models.DateTimeField()


class Genre(models.Model):
    name = models.CharField("name of genre", max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField("name of author", max_length=100)
    last_name = models.CharField("last name of author", max_length=100)

    def __str__(self):
        return f'{self.name}, {self.last_name}'


class Book(models.Model):
    operations = models.ManyToManyField(to=Operation, related_name='books')
    authors = models.ManyToManyField(to=Author, related_name='books')
    genres = models.ManyToManyField(to=Genre, related_name='books')
    name = models.CharField("name of book", max_length=50)
    publish_date = models.DateField("date of publishing")

    def __str__(self):
        return self.name


class Price(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.DO_NOTHING, related_name='prices')
    value = models.FloatField("Цена")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.price} soms, {self.book}'
