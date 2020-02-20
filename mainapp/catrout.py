from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from mainapp.__init__ import app

# categories routes fashion,electrical,cosmatics,decorative,books,groceries...


@app.route("/categories/electronics")
def catelec():
    cator="Electronics"
    ti=url_for('static',filename='images/categories/electronics/topimg.jpg')
    img1=url_for('static',filename='images/categories/electronics/img1.jpg')
    img2=url_for('static',filename='images/categories/electronics/img2.jpg')
    img3=url_for('static',filename='images/categories/electronics/img3.jpg')
    img4=url_for('static',filename='images/categories/electronics/img4.jpg')
    img5=url_for('static',filename='images/categories/electronics/img5.jpg')
    img6=url_for('static',filename='images/categories/electronics/img6.jpg')
    img7=url_for('static',filename='images/categories/electronics/img7.jpg')
    img8=url_for('static',filename='images/categories/electronics/img8.jpg')
    img9=url_for('static',filename='images/categories/electronics/img9.jpg')
    img10=url_for('static',filename='images/categories/electronics/img10.jpg')
    img11=url_for('static',filename='images/categories/electronics/img11.jpg')
    img12=url_for('static',filename='images/categories/electronics/img12.jpg')
    title="Electronics"
    cat1=" "
    cat2=" "
    cat3=" "
    lg1="Headphones"
    lg2="Mobile"
    lg3="Storage Devices"
    lg4="Accesories"
    lg5="Television"
    lg6="Laptops"
    lg7="Echo Music"
    lg8="Camera"
    lg9="Iron"
    lg10="Smart Watches"
    lg11="Drones"
    lg12="Smart Plugins"

    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('categories.html',ti=ti,cator=cator,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10
                                            ,img11=img11,img12=img12,cat1=cat1,cat2=cat2,cat3=cat3,lg1=lg1,lg2=lg2,lg3=lg3,lg4=lg4,lg5=lg5,lg6=lg6,lg7=lg7,lg8=lg8,
                                            lg9=lg9,lg10=lg10,lg11=lg11,lg12=lg12,title=title)

@app.route("/categories/fashion")
def catfash():
    cator="Fashion"
    ti=url_for('static',filename='images/categories/fashion/topimg.jpg')
    img1=url_for('static',filename='images/categories/fashion/img1.jpg')
    img2=url_for('static',filename='images/categories/fashion/img2.jpg')
    img3=url_for('static',filename='images/categories/fashion/img3.jpg')
    img4=url_for('static',filename='images/categories/fashion/img4.jpg')
    img5=url_for('static',filename='images/categories/fashion/img5.jpg')
    img6=url_for('static',filename='images/categories/fashion/img6.jpg')
    img7=url_for('static',filename='images/categories/fashion/img7.jpg')
    img8=url_for('static',filename='images/categories/fashion/img8.jpg')
    img9=url_for('static',filename='images/categories/fashion/img9.jpg')
    img10=url_for('static',filename='images/categories/fashion/img10.jpg')
    img11=url_for('static',filename='images/categories/fashion/img11.jpg')
    img12=url_for('static',filename='images/categories/fashion/img12.jpg')
    title="Fashion"
    cat1="Men"
    cat2="Women"
    cat3="Kids"
    lg1="Men"
    lg2="Women"
    lg3="Kids"
    lg4="Topwear"
    lg5="Topwear"
    lg6="Topwear"
    lg7="Bottomwear"
    lg8="Bottomwear"
    lg9="Bottomwear"
    lg10="Footwear"
    lg11="Footwear"
    lg12="Footwear"


    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('categories.html',ti=ti,cator=cator,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10
                                            ,img11=img11,img12=img12,cat1=cat1,cat2=cat2,cat3=cat3,lg1=lg1,lg2=lg2,lg3=lg3,lg4=lg4,lg5=lg5,lg6=lg6,lg7=lg7,lg8=lg8,
                                            lg9=lg9,lg10=lg10,lg11=lg11,lg12=lg12,title=title)

@app.route("/categories/books")
def catbooks():
    cator="Books"
    ti=url_for('static',filename='images/categories/books/topimg.jpg')
    img1=url_for('static',filename='images/categories/books/img1.jpg')
    img2=url_for('static',filename='images/categories/books/img2.jpg')
    img3=url_for('static',filename='images/categories/books/img3.jpg')
    img4=url_for('static',filename='images/categories/books/img4.jpg')
    img5=url_for('static',filename='images/categories/books/img5.jpg')
    img6=url_for('static',filename='images/categories/books/img6.jpg')
    img7=url_for('static',filename='images/categories/books/img7.jpg')
    img8=url_for('static',filename='images/categories/books/img8.jpg')
    img9=url_for('static',filename='images/categories/books/img9.jpg')
    img10=url_for('static',filename='images/categories/books/img10.jpg')
    img11=url_for('static',filename='images/categories/books/img11.jpg')
    img12=url_for('static',filename='images/categories/books/img12.jpg')
    title="Books"
    cat1=" "
    cat2=" "
    cat3=" "
    lg1="Fantasy"
    lg2="Adventure"
    lg3="Autobiography"
    lg4="Programming"
    lg5="Romantic"
    lg6="Self Help"
    lg7="History"
    lg8="Science"
    lg9="Cook Books"
    lg10="Horror"
    lg11="Mystery"
    lg12="Satire"

    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('categories.html',ti=ti,cator=cator,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10
                                            ,img11=img11,img12=img12,cat1=cat1,cat2=cat2,cat3=cat3,lg1=lg1,lg2=lg2,lg3=lg3,lg4=lg4,lg5=lg5,lg6=lg6,lg7=lg7,lg8=lg8,
                                            lg9=lg9,lg10=lg10,lg11=lg11,lg12=lg12,title=title)

@app.route("/categories/cosmatics")
def catcosm():
    cator="Cosmatics"
    ti=url_for('static',filename='images/categories/cosmatics/topimg.jpg')
    img1=url_for('static',filename='images/categories/cosmatics/img1.jpg')
    img2=url_for('static',filename='images/categories/cosmatics/img2.jpg')
    img3=url_for('static',filename='images/categories/cosmatics/img3.jpg')
    img4=url_for('static',filename='images/categories/cosmatics/img4.jpg')
    img5=url_for('static',filename='images/categories/cosmatics/img5.jpg')
    img6=url_for('static',filename='images/categories/cosmatics/img6.jpg')
    img7=url_for('static',filename='images/categories/cosmatics/img7.jpg')
    img8=url_for('static',filename='images/categories/cosmatics/img8.jpg')
    img9=url_for('static',filename='images/categories/cosmatics/img9.jpg')
    img10=url_for('static',filename='images/categories/cosmatics/img10.jpg')
    img11=url_for('static',filename='images/categories/cosmatics/img11.jpg')
    img12=url_for('static',filename='images/categories/cosmatics/img12.jpg')
    title="Cosmatics"
    cat1=" "
    cat2=" "
    cat3=" "
    lg1="Headphones"
    lg2="Mobile"
    lg3="Storage Devices"
    lg4="Accesories"
    lg5="Television"
    lg6="Laptops"
    lg7="Echo Music"
    lg8="Camera"
    lg9="Iron"
    lg10="Smart Watches"
    lg11="Drones"
    lg12="Smart Plugins"

    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('categories.html',ti=ti,cator=cator,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10
                                            ,img11=img11,img12=img12,cat1=cat1,cat2=cat2,cat3=cat3,lg1=lg1,lg2=lg2,lg3=lg3,lg4=lg4,lg5=lg5,lg6=lg6,lg7=lg7,lg8=lg8,
                                            lg9=lg9,lg10=lg10,lg11=lg11,lg12=lg12,title=title)

@app.route("/categories/decoratives")
def catdeco():
    cator="Decoratives"
    ti=url_for('static',filename='images/categories/decoratives/topimg.jpg')
    img1=url_for('static',filename='images/categories/decoratives/img1.jpg')
    img2=url_for('static',filename='images/categories/decoratives/img2.jpg')
    img3=url_for('static',filename='images/categories/decoratives/img3.jpg')
    img4=url_for('static',filename='images/categories/decoratives/img4.jpg')
    img5=url_for('static',filename='images/categories/decoratives/img5.jpg')
    img6=url_for('static',filename='images/categories/decoratives/img6.jpg')
    img7=url_for('static',filename='images/categories/decoratives/img7.jpg')
    img8=url_for('static',filename='images/categories/decoratives/img8.jpg')
    img9=url_for('static',filename='images/categories/decoratives/img9.jpg')
    img10=url_for('static',filename='images/categories/decoratives/img10.jpg')
    img11=url_for('static',filename='images/categories/decoratives/img11.jpg')
    img12=url_for('static',filename='images/categories/decoratives/img12.jpg')
    title="Decoratives"
    cat1=" "
    cat2=" "
    cat3=" "
    lg1="Lamps"
    lg2="Figurines"
    lg3="Vases"
    lg4="Clocks"
    lg5="Photo Frames"
    lg6="Mirrors"
    lg7="Statues"
    lg8="Paintings"
    lg9="Wall Decor"
    lg10="Sculptures"
    lg11="Decor Pabbles"
    lg12="Candels"

    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('categories.html',ti=ti,cator=cator,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10
                                            ,img11=img11,img12=img12,cat1=cat1,cat2=cat2,cat3=cat3,lg1=lg1,lg2=lg2,lg3=lg3,lg4=lg4,lg5=lg5,lg6=lg6,lg7=lg7,lg8=lg8,
                                            lg9=lg9,lg10=lg10,lg11=lg11,lg12=lg12,title=title)

@app.route("/categories/home and kitchen")
def catgroc():
    cator="Grocery"
    ti=url_for('static',filename='images/categories/grocery/topimg.jpg')
    img1=url_for('static',filename='images/categories/grocery/img1.jpg')
    img2=url_for('static',filename='images/categories/grocery/img2.jpg')
    img3=url_for('static',filename='images/categories/grocery/img3.jpg')
    img4=url_for('static',filename='images/categories/grocery/img4.jpg')
    img5=url_for('static',filename='images/categories/grocery/img5.jpg')
    img6=url_for('static',filename='images/categories/grocery/img6.jpg')
    img7=url_for('static',filename='images/categories/grocery/img7.jpg')
    img8=url_for('static',filename='images/categories/grocery/img8.jpg')
    img9=url_for('static',filename='images/categories/grocery/img9.jpg')
    img10=url_for('static',filename='images/categories/grocery/img10.jpg')
    img11=url_for('static',filename='images/categories/grocery/img11.jpg')
    img12=url_for('static',filename='images/categories/grocery/img12.jpg')
    title="Grocery"
    cat1=" "
    cat2=" "
    cat3=" "
    lg1="Headphones"
    lg2="Mobile"
    lg3="Storage Devices"
    lg4="Accesories"
    lg5="Television"
    lg6="Laptops"
    lg7="Echo Music"
    lg8="Camera"
    lg9="Iron"
    lg10="Smart Watches"
    lg11="Drones"
    lg12="Smart Plugins"

    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('categories.html',ti=ti,cator=cator,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10
                                            ,img11=img11,img12=img12,cat1=cat1,cat2=cat2,cat3=cat3,lg1=lg1,lg2=lg2,lg3=lg3,lg4=lg4,lg5=lg5,lg6=lg6,lg7=lg7,lg8=lg8,
                                            lg9=lg9,lg10=lg10,lg11=lg11,lg12=lg12,title=title)


@app.route("/categories/scraper1")
def page3():
    cator="Decoratives"
    ti=url_for('static',filename='images/categories/decoratives/topimg.jpg')
    img1=url_for('static',filename='images/categories/decoratives/img1.jpg')
    img2=url_for('static',filename='images/categories/decoratives/img2.jpg')
    img3=url_for('static',filename='images/categories/decoratives/img3.jpg')
    img4=url_for('static',filename='images/categories/decoratives/img4.jpg')
    img5=url_for('static',filename='images/categories/decoratives/img5.jpg')
    img6=url_for('static',filename='images/categories/decoratives/img6.jpg')
    img7=url_for('static',filename='images/categories/decoratives/img7.jpg')
    img8=url_for('static',filename='images/categories/decoratives/img8.jpg')
    img9=url_for('static',filename='images/categories/decoratives/img9.jpg')
    img10=url_for('static',filename='images/categories/decoratives/img10.jpg')
    img11=url_for('static',filename='images/categories/decoratives/img11.jpg')
    img12=url_for('static',filename='images/categories/decoratives/img12.jpg')
    title="Decoratives"
    cat1=" "
    cat2=" "
    cat3=" "
    lg1="Buy Now"
    lg2="Figurines"
    lg3="Vases"
    lg4="Clocks"
    lg5="Photo Frames"
    lg6="Mirrors"
    lg7="Statues"
    lg8="Paintings"
    lg9="Wall Decor"
    lg10="Sculptures"
    lg11="Decor Pabbles"
    lg12="Candels"
    
    if not current_user.is_authenticated:
        return redirect(url_for("login"))
    return render_template('page3.html',ti=ti,cator=cator,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7,img8=img8,img9=img9,img10=img10
                                            ,img11=img11,img12=img12,cat1=cat1,cat2=cat2,cat3=cat3,lg1=lg1,lg2=lg2,lg3=lg3,lg4=lg4,lg5=lg5,lg6=lg6,lg7=lg7,lg8=lg8,
                                            lg9=lg9,lg10=lg10,lg11=lg11,lg12=lg12,title=title)



