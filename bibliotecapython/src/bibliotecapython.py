#variable creq que estatica almacenada en ele egmento de datos
static_var=0

bss_var=None

from enum import enum
class Genre(enum):
    FICTION=1
    NON_FICTION=2
    SCIENCE=3
    HISTORY=4
    FANTASY=5
    BIOGRAPHY=6
    OTHER=7

class book:
    def __init__(self,id,title, author, publication_year,genre,quantity):
        self.id=book
        self.title=title
        self.author=author
        self.publication_year=publication_year
        self.genre=genre
        self.quantity=quantity
        self.next=None


class Member: 
    def __init__(self,member_id,name):
        self.id=member_id
        self.name=name
        self.issuedcount=0
        self.issued_books=[]
        self.next=None

#def genrrToString

def genreToString(genre):
    match genre:
        case Genre.FICTION:
            return "Ficcion"
        case Genre.NON_FICTION:
            return "No ficcion"
        case Genre.SCIENCE:
            return "Ciencia"
        case Genre.HISTORY:
            return "Historia"
        case Genre.FANTASY:
            return "Fantasia"
        case Genre.BIOGRAPHY:
            return "Biografia"
        case Genre.OTHER:
            return "otro"
        case _:
            return "Desconocido"


#def addbook(library, count):
    



