#!/usr/bin/env python3
""" ALL """


def list_all(mongo_collection):
    """ List all """
    documents = mongo_collection.find()

    if not documents:
        return []

    return documents


if __name__ == '__main__':
    list_all()
