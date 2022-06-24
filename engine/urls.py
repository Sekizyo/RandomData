from django.urls import path, include

import engine.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", engine.views.index, name="index"),
    path("addresses/", engine.views.addresses, name="addresses"),
    path("books/", engine.views.books, name="books"),
    path("cars/", engine.views.cars, name="cars"),
    path("creditcards/", engine.views.creditCards, name="creditCards"),
    path("datetime/<str:arg>", engine.views.dateTime, name="dateTime"),
    path("persons/", engine.views.persons, name="persons"),
    path("places/", engine.views.places, name="places"),
    path("products/", engine.views.products, name="products"),
    path("texts/", engine.views.texts, name="texts"),
    path("users/", engine.views.users, name="users")
]
