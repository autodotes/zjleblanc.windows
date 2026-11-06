#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2012, Michael DeHaan <michael.dehaan@gmail.com>, and others
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: smb_info
short_description: Gather information regarding server message block shares
description:
  - Gets list of server message block shares on a Windows hosts
  - Gets access details for each share
version_added: "1.0.1"
author:
  - Zach LeBlanc (@zjleblanc)
options:
  name:
    description:
      - Optional name filter to isolate specific shares
    type: str
    required: false
    default: "*"
seealso:
  - module: ansible.windows.win_share
'''

EXAMPLES = r'''
- name: Get info for all server message block shares
  zjleblanc.windows.smb_info:

- name: Get info for shares starting with Net
  zjleblanc.windows.smb_info:
    name: Net*
'''

RETURN = r'''
info:
  description: Object containing entries for each server message block share identified with metadata and access details
  returned: success
  type: dict
changed:
  description: Always false. This module only reads share information.
  returned: always
  type: bool
'''
