# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from whatsappcloudapi.api_helper import APIHelper
from whatsappcloudapi.models.address import Address
from whatsappcloudapi.models.email_object import EmailObject
from whatsappcloudapi.models.name import Name
from whatsappcloudapi.models.org import Org
from whatsappcloudapi.models.phone_object import PhoneObject
from whatsappcloudapi.models.url_object import UrlObject


class Contact(object):

    """Implementation of the 'Contact' model.

    TODO: type model description here.

    Attributes:
        addresses (list of Address): Full contact address(es)
        birthday (string): TODO: type description here.
        emails (list of EmailObject): Contact email address(es)
        name (Name): Full contact name
        org (Org): Contact organization information
        phones (list of PhoneObject): Contact phone number(s)
        urls (list of UrlObject): Contact URL(s)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "addresses": 'addresses',
        "birthday": 'birthday',
        "emails": 'emails',
        "org": 'org',
        "phones": 'phones',
        "urls": 'urls'
    }

    _optionals = [
        'addresses',
        'birthday',
        'emails',
        'org',
        'phones',
        'urls',
    ]

    def __init__(self,
                 name=None,
                 addresses=APIHelper.SKIP,
                 birthday='YYYY-MM-DD formatted string.',
                 emails=APIHelper.SKIP,
                 org=APIHelper.SKIP,
                 phones=APIHelper.SKIP,
                 urls=APIHelper.SKIP):
        """Constructor for the Contact class"""

        # Initialize members of the class
        if addresses is not APIHelper.SKIP:
            self.addresses = addresses 
        self.birthday = birthday 
        if emails is not APIHelper.SKIP:
            self.emails = emails 
        self.name = name 
        if org is not APIHelper.SKIP:
            self.org = org 
        if phones is not APIHelper.SKIP:
            self.phones = phones 
        if urls is not APIHelper.SKIP:
            self.urls = urls 

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

        name = Name.from_dictionary(dictionary.get('name')) if dictionary.get('name') else None
        addresses = None
        if dictionary.get('addresses') is not None:
            addresses = [Address.from_dictionary(x) for x in dictionary.get('addresses')]
        else:
            addresses = APIHelper.SKIP
        birthday = dictionary.get("birthday") if dictionary.get("birthday") else 'YYYY-MM-DD formatted string.'
        emails = None
        if dictionary.get('emails') is not None:
            emails = [EmailObject.from_dictionary(x) for x in dictionary.get('emails')]
        else:
            emails = APIHelper.SKIP
        org = Org.from_dictionary(dictionary.get('org')) if 'org' in dictionary.keys() else APIHelper.SKIP
        phones = None
        if dictionary.get('phones') is not None:
            phones = [PhoneObject.from_dictionary(x) for x in dictionary.get('phones')]
        else:
            phones = APIHelper.SKIP
        urls = None
        if dictionary.get('urls') is not None:
            urls = [UrlObject.from_dictionary(x) for x in dictionary.get('urls')]
        else:
            urls = APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   addresses,
                   birthday,
                   emails,
                   org,
                   phones,
                   urls)
