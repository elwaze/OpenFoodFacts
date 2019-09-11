#! /usr/bin env python3
# coding: utf-8

from clint.textui import colored, puts, prompt, indent

from purbeurre_models import Product, Category, Store, User
import off_requestor


def main():

    puts(colored.magenta("BONJOUR !"))

    # loads the OFF API data to database
    off_requestor.main()

    # asks for user identification. Registers in db if new user.
    user_id = puts(colored.magenta(prompt.query("Veuillez renseigner votre adresse e-mail afin d'être identifié : ")))
    user = User({"name": user_id})
    user.insert_into_db()
    puts(colored.green("Rentrez le numéro de la catégorie choisie pour accéder aux produits : "))
    categories = []
    # getting categories from the database
    # comment j'appelle get_categories() ?
    for i in range(len(categories)):
        with indent(4):
            puts(colored.blue(str(i + 1) + ' : ' + categories[i]))
    category_number = prompt.query("")
    category = Category({"name": categories[category_number - 1]})

    puts(colored.green("Rentrez le numéro du produit choisi pour accéder à un substitut : "))
    # getting products from the database
    products = []
    # products = get_products_by_category(category) non c'est pas ca, a retravailler
    for i in range(len(products)):
        with indent(4):
            puts(colored.blue(str(i + 1) + ' : ' + products[i]))
    product_number = prompt.query("")
    product = Product({"link": products[product_number - 1]})
    # substitute = get_better_product(product.score)
    puts(colored.green("Nous vous proposons de consommer " + substitute.name + " à la place de " + product.name))
    puts(colored.green("Plus d'infos : "))
    with indent(4):
        puts(colored.green("Nutriscore : " + substitute.nutriscore))
        puts(colored.green("Magasins où l'acheter : " + substitute.stores))
        puts(colored.green("Lien vers le descriptif OpenFoodFacts : " + substitute.link))
    favorite = puts(colored.blue(prompt.query("voulez-vous enregistrer ce produit dans vos favoris ? ")))


if __name__ == "__main__":
    main()


