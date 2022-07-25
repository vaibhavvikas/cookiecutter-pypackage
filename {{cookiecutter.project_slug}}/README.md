{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
## {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

## Features

* TODO

## Credits

This package was created with Cookiecutter_ and the `vaibhavvikas/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`vaibhavvikas/cookiecutter-pypackage`: https://github.com/vaibhavvikas/cookiecutter-pypackage
