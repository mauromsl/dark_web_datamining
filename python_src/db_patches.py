#!/usr/bin/env python
"""
contains all the patches that have been applied to
the database in order to keep schemas consistent across environments
"""


class DBPatch():
    def __init__(self, name, sql, validation, *args, **kwargs):
        """ Encapsulates the patches to be applied """
        self.name = name
        self.sql = sql
        self.validation = validation

patches = []

sql = """
    ALTER TABLE `dark_web`.`tblProduct`
    ADD COLUMN `USD` DECIMAL(15,2) UNSIGNED NULL COMMENT '' AFTER `product_picture`,
    ADD COLUMN `GBP` DECIMAL(15,2) UNSIGNED NULL COMMENT '' AFTER `USD`;
    """

validation = """
    SELECT *
    FROM information_schema.COLUMNS
    WHERE
        TABLE_SCHEMA = 'dark_web'
        AND TABLE_NAME = 'tblProducts'
        AND COLUMN_NAME = 'GBP';
        """
additional_currencies_patch = DBPatch(
    name='additional_currencies_patch',
    sql=sql,
    validation=validation
)

patches.append(additional_currencies_patch)


def db_patches_list():
    """ Returns a list containing all the patches required by the project """
    return patches
