from django.http import HttpResponse
from .models import Book
import datetime

def addBook(request):
    book1 = Book(name="This is a Book", page_number=200, genre="Nonfiction")
    book1.save()
    return HttpResponse("Added book!")


def printAll(request):
    book_str = ""
    allBooks = Book.objects.all()
    for eachBook in allBooks:
        book_str = book_str + str(eachBook) + "<br/>"
    return HttpResponse(book_str)


def recentPub(request):
    eachBook = Book.objects.all()
    for eachElement in eachBook:
        if eachElement.publish_date > datetime.date(2018, 1, 1):
            print(eachElement)
    return HttpResponse("Recently published books are printed in the terminal.")

def changeGenre(request):
    eachBook = Book.objects.all()
    for eachElement in eachBook:
        if eachElement.publish_date >= datetime.date(2018, 1, 1):
            eachElement.genre = "fiction"
            print(eachElement.genre)
    return HttpResponse("Changed genres of books after 2018-01-01. View in terminal")