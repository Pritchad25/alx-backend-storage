#!/usr/bin/env python3
""" The Module for using PyMongo."""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based
    on the name."""
    name_field = {"name": name}
    value_field = {"$set": {"topics": topics}}
    mongo_collection.update_many(name_field, value_field)
