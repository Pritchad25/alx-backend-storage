#!/usr/bin/env python3
"""Module for using PyMongo."""


def list_all(mongo_collection):
    """Lists all documents in a collection."""

    docList = []

    docs = mongo_collection.find()
    for doc in docs:
        docList.append(doc)

    return docList
