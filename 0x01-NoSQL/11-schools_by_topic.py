#!/usr/bin/env python3
"""The Module for using PyMongo."""


def schools_by_topic(mongo_collection, topic):
    """returns the list of schools having a specific topic."""
    return [item for item in mongo_collection.find({"topics": topic})]
