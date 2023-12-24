#!/usr/bin/env python3
""" Update """


def update_topics(mongo_collection, name, topics):
    """ Update """
    mongo_collection.update_one({'name': name}, {'$set': {'topics': topics}})


if __name__ == '__main__':
    update_topics()
