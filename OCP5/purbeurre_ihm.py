#! /usr/bin env python3
# coding: utf-8

from clint.textui import colored, puts, prompt, indent

from purbeurre_models import Product, Category, Store, User
import off_requestor


def user_choice():
    puts(colored.blue("Voulez-vous : "))
    with indent(4):
        puts(colored.blue("1 : Retrouver vos aliments substitués"))
        puts(colored.blue("2 : Rechercher un nouvel aliment"))
    choice = prompt.query("")
    if (choice != 1) and (choice != 2):
        puts(colored.red("Attention : vous devez obligatoirement rentrer 1 ou 2 pour continuer."))
        user_choice()
    return choice


def category_selection():
    puts(colored.green("Rentrez le numéro de la catégorie choisie pour accéder aux produits : "))
    categories = []
    # getting categories from the database
    # comment j'appelle get_categories() ?
    for i in range(len(categories)):
        with indent(4):
            puts(colored.blue(str(i + 1) + ' : ' + categories[i]))
    category_number = prompt.query("")
    try:
        category_number = category_number - 1
    except TypeError:
        puts(colored.red("Attention : vous devez rentrer un nombre de la liste de catégories"))
        category = category_selection()
    else:
        return categories[category_number]


def product_selection(category, user_id=0):
    puts(colored.green("Rentrez le numéro du produit choisi pour accéder à un substitut : "))
    products = []
    # products = get_products_by_category(category) non c'est pas ca, a retravailler.
    # si user_id = 0 chercher dans la categorie, sinon rechercher dans les favoris de l'user_id
    for i in range(len(products)):
        with indent(4):
            puts(colored.blue(str(i + 1) + ' : ' + products[i]))
    product_number = prompt.query("")
    try:
        product_number = product_number - 1
    except TypeError:
        puts(colored.red("Attention : vous devez rentrer un nombre de la liste de produits"))
        product = product_selection(category)
    else:
        return products[product_number]


def main():

    puts(colored.magenta("BONJOUR !"))
    # asks for user identification. Registers in db if new user.
    user_id = puts(colored.magenta(prompt.query("Veuillez renseigner votre adresse e-mail afin d'être identifié : ")))
    user = User({"name": user_id})
    user.insert_into_db()
    # asks if the user wants to see it's favorites or to search new products
    choice = user_choice()

    if choice == 2:
        # runs the requests to OFF
        # loads the OFF API data to database
        off_requestor.off_requestor()
        # asks the user to choose a category among the categories registered
        category = category_selection()
        category = Category({"name": category})
        # asks the user to choose a product among the products registered in this category
        product = product_selection(category=category)
        # attention, là im me faut le link et pas le name !!!
        product = Product({"link": product})

        substitute = product.get_better_product(product.score)
        puts(colored.green("Nous vous proposons de consommer " + substitute.name + " à la place de " + product.name))
        puts(colored.green("Plus d'infos : "))
        with indent(4):
            puts(colored.green("Nutriscore : " + substitute.nutriscore))
            puts(colored.green("Magasins où l'acheter : " + substitute.stores))
            puts(colored.green("Lien vers le descriptif OpenFoodFacts : " + substitute.link))
        favorite = puts(colored.blue(prompt.query("voulez-vous enregistrer ce produit dans vos favoris ? ")))
        # gérer l'enregistrement

    else:
        product = product_selection(user_id=user_id)
        # attention, là im me faut le link et pas le name !!!
        product = Product({"link": product})
        # attention, quand on est dans les favoris, y'a le substitué et le substituant...

    end_of_while = user_id = puts(colored.magenta(prompt.query("Souhaitez-vous continuer ? ")))



if __name__ == "__main__":
    main()


