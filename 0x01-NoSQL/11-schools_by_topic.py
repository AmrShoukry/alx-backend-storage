#!/usr/bin/env python3
""" Update """


def schools_by_topic(mongo_collection, topic):
    """ Update """
    return list(mongo_collection.find({'topics': topic}))


if __name__ == '__main__':
    schools_by_topic()
