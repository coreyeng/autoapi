{% if node.opts['rst-pre-title']|length > 0 -%}
{% for block in node.opts['rst-pre-title'] -%}
{{ block }}

{%- endfor %}
{% endif -%}

{% if orphan -%}
:orphan:

{% endif -%}

=={{ '=' * node.name|length }}==
``{{ node.name }}``
=={{ '=' * node.name|length }}==

.. automodule:: {{ node.name }}

   .. contents::
      :local:
{##}
{%- block modules -%}
{%- if subnodes %}

Submodules
==========

.. toctree::
{% for item in subnodes %}
   {{ item.name }}
{%- endfor %}
{##}
{%- endif -%}
{%- endblock -%}
{##}
.. currentmodule:: {{ node.name }}
{##}
{%- block functions -%}
{%- if node.functions %}

Functions
=========

{% for item, obj in node.functions.items() -%}
- :py:func:`{{ item }}`:
  {{ obj[0]|summary }}

{% endfor -%}

{% for item in node.functions %}
.. autofunction:: {{ item }}
{##}
{%- endfor -%}
{%- endif -%}
{%- endblock -%}

{%- block classes -%}
{%- if node.classes %}

Classes
=======

{% for item, obj in node.classes.items() -%}
- :py:class:`{{ item }}`:
  {{ obj[0]|summary }}

{% endfor -%}

{% for item, obj in node.classes.items() %}
.. autoclass:: {{ item }}
{%- for d in obj[1]['directives'] %}
   :{{ d }}:
{%- endfor %}
{% if inheritance_diagram_available -%}
{% if not node.prebuilt %}
   .. rubric:: Inheritance
   .. inheritance-diagram:: {{ item }}
      :parts: 1
{%- endif -%}
{%- endif -%}

{%- endfor -%}
{%- endif -%}
{%- endblock -%}

{%- block exceptions -%}
{%- if node.exceptions %}

Exceptions
==========

{% for item, obj in node.exceptions.items() -%}
- :py:exc:`{{ item }}`:
  {{ obj[0]|summary }}

{% endfor -%}

{% for item in node.exceptions %}
.. autoexception:: {{ item }}

   .. rubric:: Inheritance
   .. inheritance-diagram:: {{ item }}
      :parts: 1
{##}
{%- endfor -%}
{%- endif -%}
{%- endblock -%}

{%- block variables -%}
{%- if node.variables %}

Variables
=========

{% for item, obj in node.variables.items() -%}
- :py:data:`{{ item }}`
{% endfor -%}

{% for item, obj in node.variables.items() %}
.. autodata:: {{ item }}
{%- for d in obj[1]['directives'] %}
   :{{ d }}:
{%- endfor %}
{% if not node.prebuilt %}
{%- if item is upper %}
   .. code-block:: text

      {{ obj[0]|pprint|indent(6) }}
{%- endif -%}
{%- endif -%}

{%- endfor -%}
{%- endif -%}
{%- endblock -%}
