# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class Audio(object):

    """Implementation of the 'Audio' model.

    TODO: type model description here.

    Attributes:
        id (string): The media object ID. Required when you are not using a
            link.
        link (string): The protocol and URL of the media to be sent. Use only
            with HTTP/HTTPS URLs. Required when you are not using an uploaded
            media ID.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "link": 'link'
    }

    _optionals = [
        'id',
        'link',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 link=APIHelper.SKIP):
        """Constructor for the Audio class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if link is not APIHelper.SKIP:
            self.link = link 

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

        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        link = dictionary.get("link") if dictionary.get("link") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   link)
