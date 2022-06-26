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
    path("address/", engine.views.address, name="addresse"),
    path("book/", engine.views.book, name="book"),
    path("car/", engine.views.car, name="car"),
    path("creditcard/", engine.views.creditCard, name="creditCard"),
    path("datetime/<str:arg>", engine.views.dateTime, name="dateTime"),
    path("person/", engine.views.person, name="person"),
    path("place/", engine.views.place, name="place"),
    path("product/", engine.views.product, name="product"),
    path("text/", engine.views.text, name="text"),
    path("user/", engine.views.user, name="user")
]
