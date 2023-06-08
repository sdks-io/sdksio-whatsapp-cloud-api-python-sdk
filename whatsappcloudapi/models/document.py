# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper


class Document(object):

    """Implementation of the 'Document' model.

    TODO: type model description here.

    Attributes:
        id (string): It is the media object ID. Required when you are not
            using a link.
        link (string): The protocol and URL of the media to be sent. Use only
            with HTTP/HTTPS URLs. Required when you are not using an uploaded
            media ID.
        caption (string): Describes the specified document media.
        filename (string): Describes the filename for the specific document.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "link": 'link',
        "caption": 'caption',
        "filename": 'filename'
    }

    _optionals = [
        'id',
        'link',
        'caption',
        'filename',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 link=APIHelper.SKIP,
                 caption=APIHelper.SKIP,
                 filename=APIHelper.SKIP):
        """Constructor for the Document class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if link is not APIHelper.SKIP:
            self.link = link 
        if caption is not APIHelper.SKIP:
            self.caption = caption 
        if filename is not APIHelper.SKIP:
            self.filename = filename 

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
        caption = dictionary.get("caption") if dictionary.get("caption") else APIHelper.SKIP
        filename = dictionary.get("filename") if dictionary.get("filename") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   link,
                   caption,
                   filename)