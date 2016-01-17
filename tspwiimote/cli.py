#!/usr/bin/env python
#
# Copyright 2016 BMC Software, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from tspwiimote import Driver
import argparse


class CLI(object):

  def __init__(self):
    self._email = None
    self._api_token = None
    self._product_name = "TrueSight Pulse"
    self._description = "command line tool for integrating {0} and WiiMote/Raspberry Pi".format(self._product_name)

  def _parse_arguments(self):
    parser = argparse.ArgumentParser(description=self._product_name)
    parser.add_argument('-e', '--email', dest='email', action='store', metavar="e_mail",
                                 help='e-mail that has access to the {0} account'.format(self.product_name))
    parser.add_argument('-t', '--api-token', dest='api_token', action='store', metavar="api_token",
                                 help='API token for given e-mail that has access to the {0} account'.format(
                                     self.product_name))
    args = self.parser.parse_args()
    self._email = args.email
    self._api_token = args.api_token

  def execute():
    try:
        self._parse_arguments()
        d = Driver(email=self._email, api_token=self._api_token)
        d.run() 
    except RuntimeError:
        exit(1)

def main():
   cli = CLI()
   cli.execute()

if __name__ == "__main__":
    main() 
