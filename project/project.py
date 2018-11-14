from flask import Flask, render_template, url_for, redirect, request, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Categories, Base, CategoryItem, User

app = Flask(__name__)

engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# 1 homepage 
@app.route('/')
@app.route('/catalog')
def showCatalog():
    categories = session.query(Categories).all()
    items = session.query(CategoryItem).order_by(CategoryItem.id.desc()).limit(10)
    return render_template('publiccatalog.html', categories=categories,items=items)
   
# 2 Show catalog 
@app.route('/catalog/<int:categories_id>')
def showCategories(categories_id):    
    #categories side bar
    allcategories = session.query(Categories).all() 
    #categories items
    categories = session.query(Categories).filter_by(id=categories_id).one()
    items = session.query(CategoryItem).filter_by(categories_id=categories.id)
    return render_template('category.html', categories=categories, items=items,allcategories=allcategories)

# 3 show items
@app.route('/catalog/<int:categories_id>/<int:items_id>')
def showItem(categories_id,items_id):
    categories = session.query(Categories).filter_by(id=categories_id).one()
    items = session.query(CategoryItem).filter_by(id=items_id).one()
    return render_template('publicitem.html', categories=categories,items=items)

# 4 Create new item
@app.route('/catalog/new', methods=['GET', 'POST'])
def newItem():
    if request.method =='POST':
        newItem = CategoryItem(name = request.form['name'],
                               description = request.form['description'],
                               categories_id = request.form['categories_id'])
        session.add(newItem)
        session.commit()
        flash("New item created!")
        return redirect(url_for('showCatalog'))
    else:
        return render_template('newitem.html')
                                   
# 5 Edit the item
@app.route('/catalog/<int:categories_id>/<int:items_id>/edit',methods=['GET','POST'])
def editItem(categories_id,items_id):
    editedItem = session.query(CategoryItem).filter_by(id=items_id).one()
    if request.method == 'POST':
        if request.form['name'] =="":
            editedItem.name = editedItem.name
        else:
            editedItem.name = request.form['name']

        if request.form['description'] =="":
            editedItem.description = editedItem.description
        else:
            editedItem.description = request.form['description']

        if request.form['categories_id'] == "":
            editedItem.categories_id = editedItem.categories_id
        else:
            editedItem.categories_id = request.form['categories_id']
        
        session.add(editedItem)
        session.commit()
        flash("item edited!")
        return redirect(url_for('showItem',categories_id=categories_id,items_id=items_id))
    else:
        return render_template('edititem.html',categories_id=categories_id,items_id=items_id, item=editedItem)

# 6 Delete item
@app.route('/catalog/<int:categories_id>/<int:items_id>/delete',methods=['GET', 'POST'])
def deleteItem(categories_id, items_id):
    itemToDelete = session.query(CategoryItem).filter_by(id=items_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("item deleted!")
        return redirect(url_for('showCategories', categories_id=categories_id))
    else:
        return render_template('deleteitem.html', categories_id=categories_id,
                               items_id=items_id, item=itemToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)