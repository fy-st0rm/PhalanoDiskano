from inc      import *
from model    import *
from response import *
from utils    import *

def category():
    response = request.get_json()
    if not verify_key(["titles"], response):
        return Response(FAILED, "`titles` are the required payload fields.", []).as_json()

    titles = response['titles']

    for title in titles:
        cat = Category(title=title)
        pdb.session.add(cat)
        pdb.session.commit()
    return Response(SUCESS, "Sucessfully Added Category.", []).as_json()

def category_get():
    res = {
        "categories": {}
    }
    catQuery = Category.query.all()

    for cat in catQuery:
       res["categories"].update({cat.title: cat.id})
    return Response(SUCESS, "", [res]).as_json()

def category_edit():
    response = request.get_json()
    if not verify_key(["title","id"], response):
        return Response(FAILED, " `id` `title` are the required payload fields.", []).as_json()
    
    newTitle = response["title"]
    catId = response["id"]

    catQuery = Category.query.filter_by(id=catId).first()

    if catQuery == None:
        return Response(NOT_FOUND, f"Category with {catId} doesnt exists.",[]).as_json()
    
    catQuery.title = newTitle
    pdb.session.add(catQuery)
    pdb.session.commit()
    return Response(SUCESS, "Sucessfully updated post.",[]).as_json()
