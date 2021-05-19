# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2020 KuraLabs S.R.L
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Test suite for module autoapi.apinode.

See http://pythontesting.net/framework/pytest/pytest-introduction/#fixtures
"""

import pytest  # noqa

from origen_autoapi import APINode


def test_autotree():
    """
    Check that the APINode tree is consistent with a known package.
    """
    tree = APINode('origen_autoapi')

    assert tree.is_root()
    assert tree.depth() == 1
    assert len(tree.directory) == 3
    assert tree.is_relevant()
    assert tree.has_public_api()
    assert tree.get_module('origen_autoapi.apinode') is not None
    assert not tree.get_module('origen_autoapi.apinode').is_relevant()
    assert tree.tree()
    assert tree.tree(fullname=False)
    assert repr(tree)
    assert str(tree)

    depth = 1
    for node, leaves in tree.walk():
        assert not node.is_leaf()
        assert node.depth() == depth
        for leaf in leaves:
            assert leaf.is_leaf()
            assert leaf.depth() == depth + 1
        depth += 1
