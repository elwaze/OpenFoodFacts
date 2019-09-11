#! /usr/bin env python3
# coding: utf-8

from purbeurre_repositories import ProductRepository
from purbeurre_repositories import CategoryRepository
from purbeurre_repositories import StoreRepository
from purbeurre_repositories import UserRepository
from database import db


class Product:
    objects = ProductRepository(db)

    def __init__(
            self,
            link=None,
            name=None,
            nutriscore=None,
            category=None,
            stores=None,
            users=None
    ):
        self.link = link
        self.name = name
        self.nutriscore = nutriscore
        self.category = category
        self.stores = stores    # collection / liste (si ordonné)
        self.users = users  # collection / liste (si ordonné)

    @property
    def insert_sql_query_product(self):
        return 'INSERT IGNORE INTO product (link, name, nutriscore, category_name) VALUES ("{}", "{}", "{}", "{}");'.format(
            self.link, self.name, self.nutriscore, self.category)

    @property
    def insert_sql_query_stores(self):
        return 'INSERT IGNORE INTO store (name) VALUES ("{}");'.format(self.stores)

    @property
    def insert_sql_query_prod_store_relation(self):
        return 'INSERT INTO products_stores_relation (product_link, store_idstore) VALUES ("{}", "{}");'.format(
            self.link, ##idstore???##)

    def insert_into_db(self):
        self.objects.insert_by_model(self)
        print('Product {} inserted'.format(self.__dict__))


class Category:
    objects = CategoryRepository(db)

    def __init__(
            self,
            name=None
    ):
        self.name = name

    @property
    def insert_sql_query(self):
        return 'INSERT INTO category (name) VALUES ("{}")'.format(self.name)

    @property
    def select_sql_query_prod(self):
        return 'SELECT * FROM product WHERE category_name = "{}";'.format(self.name)

    def insert_into_db(self):
        self.objects.insert_by_model(self)
        print('Category {} inserted'.format(self.__dict__))


class Store:
    objects = StoreRepository(db)

    def __init__(
            self,
            name=None,
            products=None
    ):
        self.name = name
        self.products = products    # collection / liste (si ordonné)
        self.idstore = None


class User:
    objects = UserRepository(db)

    def __init__(
            self,
            name=None,
            products=None
    ):
        self.name = name
        self.products = products

    @property
    def insert_sql_query(self):
        return 'INSERT IGNORE INTO user (name) VALUES ("{}");'.format(self.name)

    def insert_into_db(self):
        self.objects.insert_by_model(self)



if __name__ == "__main__":
    pass
    # ex pr recup tous les prod de la bdd :
    # products = Product.objects.get_products()
    # pr recup prod d'1 cat :
    # catprod = Product.objects.get_products_by_category(category_name)
# enreg unn nouveau prod :
#new_prod_categories = Categorie.object.get_by_name(category_name) ?
# new_product = Product.object.insert(link, name, nutriscore, stores, new_prod_categories)
