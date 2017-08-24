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

import unittest

from udemy import Udemy
from udemy.cli import main


class TestCLI(unittest.TestCase):

    def test_instance(self):
        myudemy = main()
        self.assertEqual(isinstance(myudemy, Udemy), True)


if __name__ == '__main__':
    unittest.main()
