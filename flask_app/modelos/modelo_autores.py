from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.modelos.modelo_libros import Books

class Authors:
    def __init__( self, id, name, created_at, updated_at ):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
    
    @classmethod
    def agregaAuthor( cls, nuevoAutor ):
        query1 = "ALTER TABLE authors AUTO_INCREMENT = 1;"
        connectToMySQL( "libros_db" ).query_db( query1 )
        query2 = "INSERT INTO authors(name, created_at, updated_at) VALUES(%(name)s, %(created_at)s, %(updated_at)s);"
        resultado = connectToMySQL( "libros_db" ).query_db( query2, nuevoAutor )
        return resultado
    
    @classmethod
    def obtenerListaAutores( cls ):
        query = "SELECT * FROM authors;"
        resultado = connectToMySQL( "libros_db" ).query_db( query )
        authors = []
        for author in resultado:
            authors.append( Authors( author["id"], author["name"], author["created_at"], author["updated_at"]))
        return authors
    
    @classmethod
    def obtenerListaConLibros( cls, encontrarAutor ):
        query = "SELECT name, authors.id, books.id, title, num_of_pages FROM authors JOIN favorites ON favorites.author_id = authors.id JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        resultado = connectToMySQL( "libros_db" ).query_db( query, encontrarAutor )
        return resultado

    @classmethod
    def agregaLibroAuthor( cls, añadirLibro):
        query1 = "ALTER TABLE favorites AUTO_INCREMENT = 1;"
        connectToMySQL( "libros_db" ).query_db( query1 )
        query2 = "INSERT INTO favorites(author_id, book_id) VALUES(%(author_id)s, %(book_id)s);"
        resultado = connectToMySQL( "libros_db" ).query_db( query2, añadirLibro )
        return resultado