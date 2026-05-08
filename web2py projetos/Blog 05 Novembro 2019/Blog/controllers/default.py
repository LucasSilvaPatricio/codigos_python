# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----

def post():
    
    # id do post por padrão é o do primeiro post
    id_post = 1 

    # se for feito um request mas de um id invalido então ele carrega pro post padrão
    if request.args(0):
        id_post = request.args(0,cast=int)
        if db(db.post.id == id_post).count() <= 0:
            id_post = 1
            
    # se não for passado id ele carrega pro id padrão    

    post=db(db.post.id == id_post).select(db.post.ALL)

    form=FORM(
            LABEL("Nome: "),
            INPUT(_type="text",_name="nome",requires=IS_NOT_EMPTY()),BR(),
            LABEL("E-mail: "),
            INPUT(_type="email",_name="email"),BR(),
            LABEL("Comentario: "),BR(),
            TEXTAREA(_name="comentario",requires=IS_NOT_EMPTY()),BR(),
            INPUT(_type="submit",name="enviar",_value="enviar")
    )

    print(id_post)
    if form.process().accepted:
        db.comentario.insert(id_comentario = id_post)
        db.comentario.insert(nome = form.vars.nome)
        db.comentario.insert(email=form.vars.email)
        db.comentario.insert(conteudo=form.vars.comentario)

    return dict(post=post,form=form)

def index():

    numero_de_paginas = db(db.post).count()
    numero_de_paginacao = 5

    # começa da pagina 0 e vai até o numero de paginas a ser apresentadas
    minimo = 0
    maximo = numero_de_paginacao

    # adiciona o minimo e maximo passado na url
    if request.args(0) and request.args(1):
        minimo = request.args(0,cast=int)
        maximo = request.args(1,cast=int)

    # seleciona um limite de post que está sendo especificado por minimo e maximo
    posts = db().select(db.post.ALL,orderby=db.post.title,limitby=(minimo,maximo))

    # se a pagina for maior ou igual a numero de paginas então ele volta para
    # a posição inicial, minimo = 0 e maximo = numero_de_paginacao
    if maximo >= numero_de_paginas:
        minimo = 0
        maximo = numero_de_paginacao
    else:
        minimo = minimo + numero_de_paginacao
        maximo = maximo + numero_de_paginacao
        if maximo > numero_de_paginas:
            maximo = maximo - (maximo - numero_de_paginas)

    return dict(posts=posts,limite=(minimo,maximo))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki()

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
