# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Main of the instance validator. This script takes a YAML building
configuration file as an argument and validates it for coherence with the
Digital Buildings ontology.

This is done by first ensuring the file syntax is valid YAML, then by
parsing the ontology and comparing it with the file contents.

This tool allows clients to independently validate their configuration files.
It saves time and provides more accuracy than manual error checks."""

from __future__ import print_function

import instance_parser
import argparse
import sys

# TODO add input and return type checks in all functions

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
      description='Validate a YAML building configuration file')
  parser.add_argument('-i', '--input',
                      dest='filename',
                      required=True,
                      help='Filepath to YAML building configuration',
                      metavar='FILE')
  arg = parser.parse_args()

  # SYNTAX VALIDATION
  print('\nValidator starting ...\n')
  filename = arg.filename

  # throws errors for syntax
  raw_parse = instance_parser.parse_yaml(filename)

  if raw_parse is None:
    print('\nSyntax Error.')
    sys.exit(0)

  parsed = dict(raw_parse)

  print('Passed syntax checks!')
