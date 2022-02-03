from flask import render_template, request, session, redirect, url_for, flash
from flask_app import app
from flask_app.modelos.modelo_autores import Authors
from flask_app.modelos.modelo_libros import Books
from datetime import datetime


@app.route( '/authors', methods=["GET"] )
def despliegaAutores():
    listaAutores = Authors.obtenerListaAutores()
    return render_template( "authors.html", listaAutores=listaAutores)


@app.route( '/author/<idAutor>', methods=["GET"] )
def mostrarAutor( idAutor ):
    encontrarAutor = {
        "id" : idAutor
    }
    listaAutorLibros = Authors.obtenerListaConLibros(encontrarAutor)
    listaLibros = Books.obtenerListaLibros()
    return render_template( "author_show.html", listaAutorLibros=listaAutorLibros, listaLibros=listaLibros, var=idAutor)


@app.route( '/author/new', methods=["POST"] )
def crearAutor_P():
    nuevoAutor = {
        "name" : request.form["name"],
        "created_at" : datetime.today(),
        "updated_at" : datetime.today()
    }
    Authors.agregaAuthor( nuevoAutor )
    return redirect( '/authors' )


@app.route( '/author/<idAutor>/add', methods=["POST"] )
def añadirLibro_P(idAutor):
    añadirLibro = {
        "author_id" : idAutor,
        "book_id" : request.form["book_id"]
    }
    Authors.agregaLibroAuthor( añadirLibro )
    return redirect(url_for('mostrarAutor', idAutor=idAutor ))