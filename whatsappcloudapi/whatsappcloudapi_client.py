# -*- coding: utf-8 -*-

"""
whatsappcloudapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from whatsappcloudapi.configuration import Configuration
from whatsappcloudapi.controllers.base_controller import BaseController
from whatsappcloudapi.configuration import Environment
from whatsappcloudapi.http.auth.o_auth_2 import OAuth2
from whatsappcloudapi.controllers.messages_controller import MessagesController
from whatsappcloudapi.controllers.registration_controller\
    import RegistrationController
from whatsappcloudapi.controllers.business_profiles_controller\
    import BusinessProfilesController
from whatsappcloudapi.controllers.media_controller import MediaController
from whatsappcloudapi.controllers.phone_numbers_controller\
    import PhoneNumbersController
from whatsappcloudapi.controllers.two_step_verification_controller\
    import TwoStepVerificationController


class WhatsappcloudapiClient(object):

    @LazyProperty
    def messages(self):
        return MessagesController(self.global_configuration)

    @LazyProperty
    def registration(self):
        return RegistrationController(self.global_configuration)

    @LazyProperty
    def business_profiles(self):
        return BusinessProfilesController(self.global_configuration)

    @LazyProperty
    def media(self):
        return MediaController(self.global_configuration)

    @LazyProperty
    def phone_numbers(self):
        return PhoneNumbersController(self.global_configuration)

    @LazyProperty
    def two_step_verification(self):
        return TwoStepVerificationController(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'],
                 environment=Environment.PRODUCTION, version='v13.0',
                 access_token='', config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         version=version,
                                         access_token=access_token)
        else:
            self.config = config

        self.global_configuration = GlobalConfiguration(self.config)\
            .global_errors(BaseController.global_errors())\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseController.user_agent(), BaseController.user_agent_parameters())
        self.initialize_auth_managers(self.global_configuration)

        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

    def initialize_auth_managers(self, global_config):
        http_client_config = global_config.get_http_client_configuration()
        self.auth_managers = { key: None for key in ['global']}
        self.auth_managers['global'] = OAuth2(http_client_config.access_token)
        return self.auth_managers
