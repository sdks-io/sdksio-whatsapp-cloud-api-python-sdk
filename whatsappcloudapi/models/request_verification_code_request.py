# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class RequestVerificationCodeRequest(object):

    """Implementation of the 'RequestVerificationCodeRequest' model.

    TODO: type model description here.

    Attributes:
        code_method (RequestVerificationCodeMethodEnum): Chosen method for
            verification.
        locale (string): Your locale. For example: "en_US".

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code_method": 'code_method',
        "locale": 'locale'
    }

    def __init__(self,
                 code_method=None,
                 locale=None):
        """Constructor for the RequestVerificationCodeRequest class"""

        # Initialize members of the class
        self.code_method = code_method 
        self.locale = locale 

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

        code_method = dictionary.get("code_method") if dictionary.get("code_method") else None
        locale = dictionary.get("locale") if dictionary.get("locale") else None
        # Return an object of this model
        return cls(code_method,
                   locale)