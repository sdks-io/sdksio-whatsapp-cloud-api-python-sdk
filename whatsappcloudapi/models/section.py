# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper
from whatsappcloudapi.models.row import Row


class Section(object):

    """Implementation of the 'Section' model.

    TODO: type model description here.

    Attributes:
        title (string): Required if the message has more than one section.
            Title of the section.
        rows (list of Row): Required for List Messages. Contains a list of
            rows. You can have a total of 10 rows across your sections. Each
            row must have a title (Maximum length: 24 characters) and an ID
            (Maximum length: 200 characters). You can add a description
            (Maximum length: 72 characters), but it is optional.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title',
        "rows": 'rows'
    }

    _optionals = [
        'title',
        'rows',
    ]

    def __init__(self,
                 title=APIHelper.SKIP,
                 rows=APIHelper.SKIP):
        """Constructor for the Section class"""

        # Initialize members of the class
        if title is not APIHelper.SKIP:
            self.title = title 
        if rows is not APIHelper.SKIP:
            self.rows = rows 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        rows = None
        if dictionary.get('rows') is not None:
            rows = [Row.from_dictionary(x) for x in dictionary.get('rows')]
        else:
            rows = APIHelper.SKIP
        # Return an object of this model
        return cls(title,
                   rows)