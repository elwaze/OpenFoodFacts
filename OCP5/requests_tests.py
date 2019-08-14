#! /usr/bin env python3
# coding: utf-8

import requests


def main():
    # res = requests.get("https://fr.openfoodfacts.org/category/fr:viennoiseries-et-brioches.json")
    # results = res.json()
    #
    # print(results['products'])

    # get categories from the OpenFoodFacts' API
    request_categories = requests.get('https://fr.openfoodfacts.org/categories&json=1')
    categories_json = request_categories.json()
    # print(categories_json)

    data_tags = categories_json.get('tags')
    data_categories = []
    for data in data_tags:
        if data['products'] > 100:
            data_categories.append(data['name'])
    category_number = 0
    categories = []
    while category_number < 50:
        if ":" not in data_categories[category_number] and "-" not in data_categories[category_number]:
            categories.append(data_categories[category_number])
        # self.cursor = self.db.cursor()
        # add_category = ("INSERT INTO Category" "(category)" "VALUES('{}')".format(data_categories[category_number]))
        # self.cursor.execute(add_category)
        # self.db.commit()
        # self.cursor.close()
        category_number += 1

    print(categories)


if __name__ == "__main__":
    main()
