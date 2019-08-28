#! /usr/bin env python3
# coding: utf-8

import requests

from OFF_models import Product


def valid_result(url, name, nutriscore, categ, stores, country):
    """
    Tests that all the needed values are in the product description
    :param url: url of the OFF product page
    :param name: name of the product
    :param nutriscore: nutriscore of the product, used to sort the products
    :param categ: at least one category to compare similar peoducts
    :param stores: at least one store where we can buy the product
    :param country: we just want products for France
    :return: if all the params are OK -> True; else -> False

    """

    if url != "" and url is not None:
        if name != "" and name is not None:
            if nutriscore != "" and nutriscore is not None:
                if categ != "" and categ is not None:
                    if stores != "" and stores is not None:
                        if country.lower() == "france":
                            return True
    return False


def main():

    # get categories from the OpenFoodFacts' API
    request_categories = requests.get('https://fr.openfoodfacts.org/categories&json=1')
    categories_json = request_categories.json()
    data_tags = categories_json.get('tags')

    # make some sorting
    data_categories = []
    for data in data_tags:
        # for a useful category, we want at least 500 products
        if data['products'] > 100:
            data_categories.append((data['name'], data['url'], data['products']))
    category_number = 0
    category_tested = 0
    categories = []
    # we want 20 ctegories
    while category_number < 10:
        # we keep only categories with a clean name
        if ":" not in data_categories[category_tested][0] and "-" not in data_categories[category_tested][0]:
            categories.append(data_categories[category_tested])
            category_number += 1
        category_tested += 1

    # get products from OFF
    products = []
    prod_nb = 0
    pnb = 0
    prod = []
    for category in categories:
        pages_count = 1
        needed_pages = category[2]/20
        if needed_pages > 5:
            needed_pages = 5
        while pages_count < needed_pages:
            # we request pages one by one
            # request_products = requests.get(category[1] + '/' + str(pages_count) + '.json')
            request_products = requests.get(category[1] + '&json=' + str(pages_count))
            products_json = request_products.json()
            prod.append(products_json.get('products'))
            pages_count += 1

        # make some sorting
        for i in (range(0, len(prod)-1)):
            for p in prod[i]:
                url = p.get('url')
                name = p.get('product_name_fr')
                nutriscore = p.get('nutrition_grades')
                categ = p.get('categories')
                stores = p.get('stores')
                country = p.get('countries')
                pnb += 1
                if valid_result(url, name, nutriscore, categ, stores, country):
                    #insert directement dans la bdd à revoir +++
                    options = {"name": name, "link": url, "nutriscore": nutriscore, "categories": categ, "stores": stores}
                    product = Product(**options)
                    product.insert_into_db()
                    # products.append()
                    prod_nb += 1
    print(products)
    print(prod_nb)
    print(pnb)


if __name__ == "__main__":
    main()
