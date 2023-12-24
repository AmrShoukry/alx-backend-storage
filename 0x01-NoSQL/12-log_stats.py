#!/usr/bin/env python3
""" LOGS """
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    documents = nginx_collection.find()

    x = 0
    get = 0
    post = 0
    put = 0
    patch = 0
    delete = 0
    checked = 0

    for document in documents:
        x += 1
        if (document['method'] == 'GET'):
            get += 1
            if (document['path'] == '/status'):
                checked += 1
        elif (document['method'] == 'POST'):
            post += 1
        elif (document['method'] == 'PUT'):
            put += 1
        elif (document['method'] == 'PATCH'):
            patch += 1
        elif (document['method'] == 'DELETE'):
            delete += 1

    print(f'{x} logs:')
    print('Methods:')
    print(f'\tmethod GET: {get}')
    print(f'\tmethod POST: {post}')
    print(f'\tmethod PUT: {put}')
    print(f'\tmethod PATCH: {patch}')
    print(f'\tmethod DELETE: {delete}')
    print(f'{checked} status check')
