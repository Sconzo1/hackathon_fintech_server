from abc import ABC

import knox.auth
from drf_spectacular.authentication import OpenApiAuthenticationExtension


class KnoxTokenScheme(OpenApiAuthenticationExtension, ABC):
    name = "knox auth"
    target_class = knox.auth.TokenAuthentication
    match_subclasses = True
    priority = 1

    def get_security_definition(self, auto_schema):
        return {
            'type': 'http',
            'scheme': 'bearer',
        }
