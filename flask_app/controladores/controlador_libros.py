from flask import render_template, request, session, redirect, url_for, flash
from flask_app import app
from flask_app.modelos.modelo_libros import Books
from datetime import datetime
from flask_app.modelos.modelo_autores import Authors


@app.route( '/books', methods=["GET"] )
def mostrarlibros():
    listaLibros = Books.obtenerListaLibros()
    return render_template("books.html", listaLibros=listaLibros)

@app.route( '/book/new', methods=["POST"] )
def crearLibro_P():
    nuevoBook = {
        "title" : request.form["title"],
        "num_of_pages" : request.form["num_of_pages"],
        "created_at" : datetime.today(),
        "updated_at" : datetime.today()
    }
    Books.agregaBooks( nuevoBook )
    return redirect( '/books' )

@app.route( '/book/<idBook>', methods=["GET"] )
def mostrarlibro_P(idBook):
    encontrarLibro = {
        "id" : idBook
    }
    listaAutoresFavorito = Books.obtenerListaAutoresFavorito(encontrarLibro)
    print("-----", listaAutoresFavorito)
    listaAutores = Authors.obtenerListaAutores()
    return render_template("book_show.html", listaAutoresFavorito=listaAutoresFavorito, listaAutores=listaAutores, var = idBook)

@app.route( '/book/<idBook>/add', methods=["POST"] )
def añadirLibroFavorito_P(idBook):
    añadirLibro = {
        "author_id" : request.form["autor_id"],
        "book_id" : idBook
        
    }
    Books.agregaAutorFavorito( añadirLibro )
    return redirect(url_for('mostrarlibro_P', idBook=idBook ))