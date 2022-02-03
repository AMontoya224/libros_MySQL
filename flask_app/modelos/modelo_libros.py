from flask_app.config.mysqlconnection import connectToMySQL

class Books:
    def __init__( self, id, title, num_of_pages, created_at, updated_at ):
        self.id = id
        self.title = title
        self.num_of_pages = num_of_pages
        self.created_at = created_at
        self.updated_at = updated_at
    
    @classmethod
    def agregaBooks( cls, nuevoLibro ):
        query1 = "ALTER TABLE books AUTO_INCREMENT = 1;"
        connectToMySQL( "libros_db" ).query_db( query1 )
        query2 = "INSERT INTO books(title, num_of_pages, created_at, updated_at) VALUES(%(title)s, %(num_of_pages)s, %(created_at)s, %(updated_at)s);"
        resultado = connectToMySQL( "libros_db" ).query_db( query2, nuevoLibro )
        return resultado

    @classmethod
    def obtenerListaLibros( cls ):
        query = "SELECT * FROM books;"
        resultado = connectToMySQL( "libros_db" ).query_db( query )
        books = []
        for book in resultado:
            books.append( Books( book["id"], book["title"], book["num_of_pages"], book["created_at"], book["updated_at"]))
        return books

    @classmethod
    def obtenerListaAutoresFavorito( cls, encontrarLibro, ):
        query = "SELECT authors.id, name, title, books.id FROM authors JOIN favorites ON favorites.author_id = authors.id JOIN books ON books.id = favorites.book_id WHERE books.id = %(id)s;"
        resultado = connectToMySQL( "libros_db" ).query_db( query, encontrarLibro )
        return resultado

    @classmethod
    def agregaAutorFavorito( cls, añadirLibro ):
        query1 = "ALTER TABLE books AUTO_INCREMENT = 1;"
        connectToMySQL( "libros_db" ).query_db( query1 )
        query2 = "INSERT INTO favorites(author_id, book_id) VALUES(%(author_id)s, %(book_id)s);"
        resultado = connectToMySQL( "libros_db" ).query_db( query2, añadirLibro )
        return resultado
        