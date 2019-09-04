#! /usr/bin env python3
# coding: utf-8

from OFF_repositories import ProductRepository
from OFF_repositories import CategoryRepository
from OFF_repositories import StoreRepository
from OFF_repositories import UserRepository
from database import db


class Product:
    objects = ProductRepository(db)

    def __init__(
            self,
            link=None,
            name=None,
            nutriscore=None,
            other_categories=None,
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
        return 'INSERT INTO product (link, name, nutriscore, category_name) VALUES ({}, {}, {}, {});'.format(
            self.link, self.name, self.nutriscore, self.category)

    @property
    def select_sql_query_product(self):
        return 'SELECT * FROM product WHERE category_name = {}'.format(self.category)

    def insert_into_db(self):
        self.objects.insert_by_model(self)


class Category:
    objects = CategoryRepository(db)

    def __init__(
            self,
            name=None,
            products=None
    ):
        self.name = name
        self.products = products    # collection / liste (si ordonné)

    @property
    def insert_sql_query(self):
        return 'INSERT INTO category (name) VALUES ({})'.format(self.name)

    def insert_into_db(self):
        self.objects.insert_by_model(self)


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


if __name__ == "__main__":
    pass
    # ex pr recup tous les prod de la bdd :
    # products = Product.objects.get_products()
    # pr recup prod d'1 cat :
    # catprod = Product.objects.get_products_by_category(category_name)
# enreg unn nouveau prod :
#new_prod_categories = Categorie.object.get_by_name(category_name) ?
# new_product = Product.object.insert(link, name, nutriscore, stores, new_prod_categories)
