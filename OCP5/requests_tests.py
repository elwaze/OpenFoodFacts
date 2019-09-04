#! /usr/bin env python3
# coding: utf-8

import requests

from OFF_models import Product, Category, Store, User
#
# def main():
#
#     # get categories from the OpenFoodFacts' API
#     request_categories = requests.get('https://fr.openfoodfacts.org/categories&json=1')
#     categories_json = request_categories.json()
#     data_tags = categories_json.get('tags')
#
#     # make some sorting
#     data_categories = []
#     for data in data_tags:
#         # for a useful category, we want at least 500 products
#         if data['products'] > 100:
#             data_categories.append((data['name'], data['url'], data['products']))
#     category_number = 0
#     category_tested = 0
#     categories = []
#     # we want 20 ctegories
#     while category_number < 10:
#         # we keep only categories with a clean name
#         if ":" not in data_categories[category_tested][0] and "-" not in data_categories[category_tested][0]:
#             categories.append(data_categories[category_tested])
#             category_number += 1
#         category_tested += 1
#
#     # get products from OFF
#     products = []
#     prod_nb = 0
#     pnb = 0
#     prod = []
#     for category in categories:
#         pages_count = 1
#         needed_pages = category[2]/20
#         if needed_pages > 5:
#             needed_pages = 5
#         while pages_count < needed_pages:
#             # we request pages one by one
#             # request_products = requests.get(category[1] + '/' + str(pages_count) + '.json')
#             request_products = requests.get(category[1] + '&json=' + str(pages_count))
#             products_json = request_products.json()
#             prod.append(products_json.get('products'))
#             pages_count += 1
#
#         # make some sorting
#         for i in (range(0, len(prod)-1)):
#             for p in prod[i]:
#                 url = p.get('url')
#                 name = p.get('product_name_fr')
#                 nutriscore = p.get('nutrition_grades')
#                 categ = p.get('categories')
#                 stores = p.get('stores')
#                 country = p.get('countries')
#                 pnb += 1
#                 if all([url, name, nutriscore, categ, stores, country.lower().strip() == "france"]):
#                 # if valid_result(url, name, nutriscore, categ, stores, country):
#                     #insert directement dans la bdd à revoir +++
#                     options = {"name": name, "link": url, "nutriscore": nutriscore, "categories": categ, "stores": stores}
#                     product = Product(**options)
#                     product.insert_into_db()
#                     prod_nb += 1
#     print(prod_nb)
#     print(pnb)


def sort_and_register_products(products):
    for i in (range(0, len(products) - 1)):
        for product in products[i]:
            url = product.get('url')
            name = product.get('product_name_fr')
            nutriscore = product.get('nutrition_grades')
            categ = product.get('categories')
            stores = product.get('stores')
            country = product.get('countries')
            if all([url, name, nutriscore, categ, stores, country.lower().strip() == "france"]):
                # insert directement dans la bdd à revoir +++
                options = {"name": name, "link": url, "nutriscore": nutriscore, "categories": categ, "stores": stores}
                product = Product(**options)
                product.insert_into_db()


def get_products(category):
    products = []
    pages_count = 1
    needed_pages = category[2] / 20
    # if we take too many pages, it's too long for demo
    if needed_pages > 3:
        needed_pages = 3
    while pages_count < needed_pages:
        # we request pages one by one
        request_products = requests.get(category[1] + '&json=' + str(pages_count))
        products_json = request_products.json()
        products.append(products_json.get('products'))
        pages_count += 1
        sort_and_register_products(products)


def get_categories(data_tags):
    data_categories = []
    for data in data_tags:
        # for a useful category, we want at least 500 products
        if data['products'] > 100:
            data_categories.append((data['name'], data['url'], data['products']))
    category_selected = 0
    category_tested = 0
    categories = []
    # we want 5 categories
    while category_selected < 5:
        # we keep only categories with a clean name
        category = data_categories[category_tested]
        if ":" not in category[0] and "-" not in category[0]:
            category_selected += 1
            options = {"name": category[0], "products": category[2]}
            category_registered = Category(**options)
            category_registered.insert_into_db()
            # get products for this category
            get_products(category)
        category_tested += 1


def main():
    # get categories from the OpenFoodFacts' API
    request_categories = requests.get('https://fr.openfoodfacts.org/categories&json=1')
    categories_json = request_categories.json()
    data_tags = categories_json.get('tags')
    # make some sorting and get products
    get_categories(data_tags)


if __name__ == "__main__":
    main()
