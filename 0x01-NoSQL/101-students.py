#!/usr/bin/env python3
""" Top students """

def top_students(mongo_collection):
    """ Top students """
    top = mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ])
    return top
