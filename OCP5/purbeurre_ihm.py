#! /usr/bin env python3
# coding: utf-8

from clint.textui import colored, puts, prompt, indent

from purbeurre_models import Product, Category, Store, User
import off_requestor
import database


def user_choice():
    puts(colored.blue("Voulez-vous : "))
    with indent(4):
        puts(colored.blue("1 : Retrouver vos aliments substitués"))
        puts(colored.blue("2 : Rechercher un nouvel aliment"))

    response = int(prompt.query(" "))
    choice_list = [1, 2]
    if response not in choice_list:
        puts(colored.red("Attention : vous devez obligatoirement rentrer 1 ou 2 pour continuer."))
        user_choice()
    return response


def category_selection():
    puts(colored.green("Rentrez le numéro de la catégorie choisie pour accéder aux produits : "))
    # getting categories from the database
    categories = []
    for element in Category.objects.get_categories():
        categories.append(element['name'])
    for i in range(len(categories)):
        with indent(4):
            puts(colored.blue(str(i + 1) + ' : ' + categories[i]))
    category_number = int(prompt.query(" "))
    try:
        category_number = category_number - 1
    except TypeError:
        puts(colored.red("Attention : vous devez rentrer un nombre de la liste de catégories"))
        category_selection()
    else:
        if category_number in range(len(categories)):
            return categories[category_number]
        else:
            puts(colored.red("Attention : vous devez rentrer un nombre de la liste de catégories"))
            category_selection()


def product_selection(category=None, user=0):
    puts(colored.green("Rentrez le numéro du produit choisi pour accéder à un substitut : "))
    products = []
    # if user_id = 0, searching by category
    if user == 0:
        prods = Product.objects.get_products_by_category(category)
        for element in prods:
            products.append((element['name'], element['link']))
    # else, searching in the registred products of the user
    else:
        prods = Product.objects.get_products_by_user(user)
        for element in prods:
            product = Product.objects.get_product_name(element)
            products.append((product, element))
    for i in range(len(products)):
        with indent(4):
            puts(colored.blue(str(i + 1) + ' : ' + products[i][0]))
    product_number = int(prompt.query(" "))
    try:
        product_number = product_number - 1
    except TypeError:
        puts(colored.red("Attention : vous devez rentrer un nombre de la liste de produits"))
        product = product_selection(category=category, user=user)
    else:
        return products[product_number]


def substitute_proposal(substitute, product):
    puts(colored.green("Nous vous proposons de consommer " + substitute.name + " à la place de " + product.name))
    puts(colored.green("Plus d'infos : "))
    with indent(4):
        puts(colored.green("Nutriscore : " + str(substitute.nutriscore)))
        # puts(colored.green("Magasins où l'acheter : " + ', '.join(map(str, substitute.stores))))
        puts(colored.green("Lien vers le descriptif OpenFoodFacts : " + substitute.link))


def main():

    puts(colored.magenta("BONJOUR !"))
    # asks for user identification. Registers in db if new user.
    user_id = prompt.query("Veuillez renseigner votre adresse e-mail afin d'être identifié : ")
    user = User(user_id)
    user.insert_into_db()

    # starting while loop to run the app or quit
    while_quit = 0
    while while_quit == 0:

        # asks if the user wants to see it's favorites or to search new products
        choice = user_choice()

        if choice == 2:
            # runs the requests to OFF
            # loads the OFF API data to database
            off_requestor.off_requestor()
            # asks the user to choose a category among the categories registered
            category = category_selection()
            category = Category(name=category)
            # asks the user to choose a product among the products registered in this category
            product = product_selection(category=category)
            product = Product(link=product[1], name=product[0])
            #
            substitute = Product.objects.get_better_products_by_category(category)
            substitute = substitute[0]
            substitute = Product(link=substitute["link"], name=substitute["name"], nutriscore=substitute["nutriscore"])
            substitute.stores = Store.objects.get_stores_by_product(substitute)
            substitute_proposal(substitute, product)

            save_product = [{'selector': 'yes', 'prompt': 'oui', 'return': 1},
                            {'selector': 'no', 'prompt': 'non', 'return': 0}]
            favorite = prompt.options("voulez-vous enregistrer ce produit dans vos favoris ? ", save_product)
            if favorite:
                user.insert_sql_query_prod_user_relation(good_product=substitute, bad_product=product)

        else:
            product = product_selection(user=user)
            product = Product(link=product)
            substitute = database.db.query('SELECT good_product_link FROM products_users_relation WHERE bad_product_link = "{}";'.format(product))
            substitute = Product(link=substitute)
            # substitute.stores, substitute.nutriscore, substitute.name =
            substitute_proposal(substitute, product)

        # going out of while loop.
        quit_options = [{'selector': 'yes', 'prompt': 'yes', 'return': 0},
                        {'selector': 'no', 'prompt': 'no', 'return': 1}]
        while_quit = prompt.options("Souhaitez-vous continuer ?", quit_options)


if __name__ == "__main__":
    main()
