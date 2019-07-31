#! /usr/bin env python3
# coding: utf-8

import requests


def main():
    res = requests.get("https://fr.openfoodfacts.org/category/fr:viennoiseries-et-brioches.json")
    results = res.json()

    print(results['products'])


if __name__ == "__main__":
    main()
