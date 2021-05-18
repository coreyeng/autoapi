.. toctree::
   :hidden:

   developer
   autoapi/autoapi
   autoapi/documented

==============
Origen-AutoAPI
==============

.. container:: float-right

   .. image:: _static/images/logo.png

.. note::
   This is a forked version of the original `AutoAPI <https://pypi.org/project/autoapi/>`_, released under the same licensing, with updates specifically for the `Origen project <https://origen-sdk.org/>`_. The original source is available on its `Github <https://github.com/carlos-jenkins/autoapi>`_ project.

.. warning::
   As this is a re-release, many of the configuration values remain the same as the original. It is not advised to use this in parallel to the `original package <https://pypi.python.org/pypi/autoapi/>`_.

Automatic Python API reference documentation generator for Sphinx, inspired by
Doxygen.

``Origen-AutoAPI`` (just ``AutoAPI`` going forward) is a Sphinx_ extension to automatically generate
API reference documentation for Python packages
(:doc:`example <autoapi/documented>`), recursively, without any intervention
from the developer. It will discover all the package modules and their public
objects and document them.

.. contents::
   :local:


Usage
=====

#. Install:

   .. code-block:: sh

      pip install origen_autoapi

   Or if using Virtualenv_ or Tox_ (and you should) add it to your
   *requirements.txt* (or *requirements.dev.txt* if you want to separate
   your package requirements from the development requirements).

#. Add AutoAPI to your extensions:

   In your Sphinx_ ``conf.py`` configuration file add ``origen_autoapi.sphinx``:

   .. code-block:: python

      extensions = [
          'sphinx.ext.autodoc',
          'sphinx.ext.inheritance_diagram',
          'origen_autoapi.sphinx'
      ]

   Make sure to have ``autodoc`` and ``inheritance_diagram`` too because the
   default generation template will use them.

#. Configure AutoAPI with the root modules you want to generate documentation
   for:

   In your project ``conf.py`` file define the ``autoapi_modules`` dictionary
   variable with the module names as keys:

   .. code-block:: python

      autoapi_modules = {'mymodule': None}

   This dictionary maps the module names with the options for generation for
   that module:

   :prune: ``bool [False]``
    The package to document is modeled as a tree, and each submodule is a node
    of that tree.
    A node is considered relevant if it has a public interface that needs to
    be documented or it is required to reach a node that has a public
    interface.
    If ``prune`` is set to ``True``, all branches that aren't relevant will be
    silently ignored. If ``False``, all branches will be generated, even for
    those modules that do not possess a public interface.
   :override: ``bool [True]``
    Regenerate the reference pages even if they exists. AutoAPI by default is
    automatic, but if you prefer to use it like autosummary_generate_ and
    create stub pages for later manual edition set the ``override`` flag to
    ``False`` and commit the generated pages to your version control.
    On the other hand, if fully automatic reference documentation generation
    is preferred put the output folder of this module in your version control
    ignore file.
   :template: ``str ['module']``
    Template name to use. This option can be changed to use different templates
    for different modules. See the section :ref:`different_templates`.
   :output: ``str [module]``
    Output folder to generate the documentation for this module relative to
    the folder where your ``conf.py`` is located. By default the output folder
    is the same as the module key. For example, for ``mymodule`` the following
    could be generated:

    .. code-block:: text

        .
        |-- conf.py
        `-- mymodule
            |-- mymodule.rst
            |-- mymodule.submodule.rst
            `-- mymodule.another.rst
   :orphan: ``bool``
    Inserts the `orphan <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html#orphan>`_ 
    directive to all generated contents from this module.
   :module-members: ``list ['str']``
    Include additional members to document when generating for a ``module``.
    Options are ``undoc-members``, ``special-members``, and ``private-members``
   :class-members: ``list ['str']``
    Include additional members to document. These are inserted as
    `directives <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#directives>`_
    into the resulting ``.rst`` for ``classes``.
   :exclude-members: ``list ['str']``
    Enumerated members to exclude from resulting ``.rst``.

   For example, a custom configuration could be:

   .. code-block:: python

      autoapi_modules = {
         'mymodule': {
            'override': False,
            'output': 'auto'
         }
      }

#. Configure Auxillary AutoAPI Settings

   Other options available in your Sphinx's ``conf.py``:

   .. code-block:: python

      # Output directory to place generated contents.
      # Can be absolute or relative to your Sphinx's ``conf.py``.
      autoapi_output_dir = '...'

   AutoAPI also supports a listener to post-process an ``APINode``.
   Each node will be given to this method in turn:

   .. code-block:: python

      def setup(app):
         def postprocess_node(app, node):
            ...
      
         app.connect('autoapi-process-node', postprocess_node)

#. Reference your documentation in your Sphinx project:

   Add in one of your reST source files a reference to the documentation.

   .. code-block:: rest

      .. toctree::
         :hidden:

         mymodule/mymodule

   And, optionally, you can link to it like this:

   .. code-block:: rest

      See the :doc:`reference documentation <mymodule/mymodule>`.

#. Prepare your codebase:

   Now in your modules, put all the elements you want to document in the
   ``__all__`` or the ``__api__`` listings. See the section
   :ref:`documenting_the_code`.


.. _documenting_the_code:

Documenting the code
====================

The strict minimum:

- List all public objects in your ``__all__`` (preferred) or ``__api__``.
- Put at least a docstring with a brief in your module, in all your public
  classes, methods, functions and variables.

Even better:

- Use the autodoc_ syntax in your docstrings (or use other that autodoc
  supports).

Use the following example as a guide. Check corresponding
:doc:`documentation <autoapi/documented>` produced by AutoAPI.

.. literalinclude:: documented.py


Customizing
===========

AutoAPI provides several ways to customize the output generated by the tool.
AutoAPI uses the Jinja2_ template engine for page generation.


Overriding the default template
-------------------------------

The `default template`_ used by ``autoapi`` can be customized to meet your
needs. To do so, copy the default template and put it in your
``templates_path`` (usually ``_templates``) folder under:

.. code-block:: text

   <templates_path>/autoapi/module.rst

The next run Sphinx_ will use it for all your modules documentation generation.


.. _different_templates:

Using different templates
-------------------------

Instead of providing a single template for all your modules you can also setup
different templates for different modules. For example, for you module
``mymod`` you choose to use the template ``mymodtemplate``. In your ``conf.py``
the following is setup:

.. code-block:: python

   # autoapi configuration
   autoapi_modules = {
       'mymod': {'template': 'mymodtemplate'}
   }

Now you need to place your template in:

.. code-block:: text

   <templates_path>/autoapi/mymodtemplate.rst

And AutoAPI will use it for documenting ``mymod`` only.


Improvements
============

This is a list of possible improvements, its doesn't mean they are good idea
or that they should be implemented.

- Automatically hook the auto-generated files to the index document
  ``toctree``.
- Extend the ``__api__`` key to support a dictionary so each element that
  requires documentation can provide attributes individually
  (like show special members).
- Generate an optional module index page with a different template
  (called index.rst at the module generation folder).


Contributing
============

- :doc:`Developer Guide. <developer>`
- :doc:`Internal Documentation Reference. <autoapi/autoapi>`


Development
===========

- `Project GitHub`_.
- `Project PyPI`_.

License
=======

.. code-block:: text

   Copyright (C) 2015-2021 KuraLabs S.R.L, Origen-SDK

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing,
   software distributed under the License is distributed on an
   "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
   KIND, either express or implied.  See the License for the
   specific language governing permissions and limitations
   under the License.


.. _Sphinx: http://sphinx-doc.org/
.. _Virtualenv: https://virtualenv.pypa.io/
.. _autodoc: http://sphinx-doc.org/ext/autodoc.html
.. _autosummary_generate: http://sphinx-doc.org/latest/ext/autosummary.html#generating-stub-pages-automatically
.. _Tox: https://tox.readthedocs.org/
.. _default template: https://raw.githubusercontent.com/carlos-jenkins/autoapi/master/lib/autoapi/templates/autoapi/module.rst
.. _Project GitHub: https://github.com/coreyeng/autoapi
.. _Project PyPI: https://pypi.python.org/pypi/origen_autoapi/
.. _Original Source GitHub: https://github.com/carlos-jenkins/autoapi
.. _Original PyPI: https://pypi.python.org/pypi/autoapi/
.. _Jinja2: http://jinja.pocoo.org/
