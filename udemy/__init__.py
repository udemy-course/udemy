# Copyright Peng Xiao
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import requests

__title__ = 'python-udemy'
__version__ = '0.0.2'
__author__ = 'penxiao'
__email__ = 'xiaoquwl@gmail.com'


class Udemy(object):
    """udemy api clss
    """
    def __init__(self, url, token, api_version='api-2.0'):
        self._url = '%s/%s' % (url, api_version)
        self._api_version = api_version
        self.headers = {}

        self._set_token(token)

        #: Create a session object for requests
        self.session = requests.Session()

    @property
    def api_version(self):
        """return api version
        """
        return self._api_version

    def _set_token(self, token):
        self.private_token = token if token else None
        if token:
            self.headers["PRIVATE-TOKEN"] = token
        elif "PRIVATE-TOKEN" in self.headers:
            del self.headers["PRIVATE-TOKEN"]
