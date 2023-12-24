#!/usr/bin/env python3
""" INSERT """


def insert_school(mongo_collection, **kwargs):
    """ Insert new """
    document = mongo_collection.insert_one(kwargs)

    return document.inserted_id


if __name__ == '__main__':
    insert_school()
