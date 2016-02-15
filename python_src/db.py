#!/usr/bin/env python
""" Controls actions on the database """

import settings
from db_patches import db_patches_list


def query(query_string, safe_mode=True):
    """ Given a query string returns a cursor object """
    valid_query = validate_query(query_string, safe_mode)
    if valid_query:
        cursor = settings.connection.cursor()
        return cursor.execute(query_string)
    else:
        raise Exception(
            'SQL verbs that alter schema are not allowed in safe mode')


def validate_query(query_string, safe_mode):
    """On safe mode, reject schema alterations """
    verbs_not_allowed = ['create, alter, grant']
    if safe_mode:
        if any(verb in query_string.lower() for verb in verbs_not_allowed):
            return False

    return True


def validate_patches():
    """ Ensure that the required db patches have been applied
    and applies those requireds
    """
    for patch in db_patches_list():
        print ("##### validating patch %s ####" % (patch.name))
        is_valid = query(patch.validation, safe_mode=False)
        if is_valid:
            print ('Validation OK')
        else:
            print ('Not valid - Applying patch ...')
            query(patch.sql, safe_mode=False)


validate_patches()
