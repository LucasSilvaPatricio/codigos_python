# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----


# ======== função sair =======
def sair():
    session.usuario_sessao = None
    redirect(URL('index'))

# ======== função recado ========
def recado():
    # se não existir sessão ele carrega para index
    if not session.usuario_sessao:
        redirect(URL('index'))

    # carrega os recados de acordo com o usuario logado no momento
    result = db(session.usuario_sessao[0].id == db.recado.id_recado).select(db.recado.ALL, orderby=db.recado.remetente)
    
    #retorna os recados
    return dict(result=result)

# ======== função carrega mural ========
def mural():

    # se não existir sessão ele carrega para index
    if not session.usuario_sessao:
        redirect(URL('index'))

    # carrega todo mural e organiza por titulo
    result = db().select(db.mural_escolar.ALL,orderby=db.mural_escolar.titulo)

    # retorna o mural
    return dict(result=result)

def areaUsuario():
    # status -1 vai dizer que não foi enviado nenhum comentario
    estatus = -1

    # se o request.vars.comentario for definido e for diferente de "" então ele enviara 
    # o comentario e mudara o estatos para 1 indicando que foi enviado com sucesso
    if request.vars.comentario and request.vars.comentario != "":
        db.comentario_anonymou.insert(comentario=request.vars.comentario)
        estatus = 1 
            
    # se sessão não existir ele carrega de volta para index
    if not session.usuario_sessao:
        redirect(URL('index'))

    # busca boletim de acordo com a sessão logada
    boletim = db(db.boletim.id_boletim == session.usuario_sessao[0].id).select(db.boletim.ALL)

    # alguma problema e ele muda o boletim para None
    try:
        media = float(boletim[0].n1)+float(boletim[0].n2)+float(boletim[0].n3)+float(boletim[0].n4)/4
    except Exception:
        media = None


    # mostrar a turma relacionando a serie 
    aluno = db(session.usuario_sessao[0].serie == db.usuario.serie).select(db.usuario.foto,db.usuario.nome)

    # efetua retorno
    return dict(content=session.usuario_sessao,boletim=media,aluno=aluno,envio=estatus)


# ======== função index, responsavel pela tela inicial da aplicação ========
def index():

    # verifica se existe alguma sessão, caso exista ridereciona para a area do usuario
    if session.usuario_sessao:
        redirect(URL('areaUsuario'))

    # cria o formulario de login
    form = FORM(
        LABEL("Usuario: "),
        INPUT(_type="text",_name="usuario",requires=IS_NOT_EMPTY()),
        BR(),
        BR(),
        LABEL("Senha: "),
        INPUT(_type="number",_name="matricula",requires=IS_NOT_EMPTY()),
        BR(),
        BR(),
        INPUT(_type="submit",_value="entrar")
    )

    # verifica se todos os dados do formulario de login foram informados de forma correta.
    if form.process().accepted:
        # em seguida procura por usuario e matricula no banco de dados e caso exista gera uma sessão.
        usuario_sessao = db(db.usuario.nome == request.vars.usuario and db.usuario.matricula == request.vars.matricula).select(db.usuario.ALL)
        
        # verifica se a sessão foi encontrada e encaminha para a pagina area usuario caso tenha sido
        # encontrada a sessão.

        # se sessão não for criada então ele alerta sobre usuario ou matriculas invalidos.
        if usuario_sessao:
            session.usuario_sessao = usuario_sessao
            redirect(URL("areaUsuario"))
        else:
            response.flash = 'Usuario ou matricula invalidos'
            

    return dict(form=form)

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
