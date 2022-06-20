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
    path("", engine.views.index)
    path("/addresses", engine.views.addresses)
    path("/books", engine.views.books)
    path("/creditcards", engine.views.creditCards)
    path("/dateTime", engine.views.dateTime)
    path("/persons", engine.views.persons)
    path("/places", engine.views.places)
    path("/products", engine.views.products)
    path("/texts", engine.views.texts)
    path("/users", engine.views.users)
]
