# A Python Polylith repo

This is a repository with a `Python` setup of the Polylith Architecture.
Here you will find code being shared between different kind of projects, and the developer tooling setup.

## Docs
The official Polylith documentation:
[high-level documentation](https://polylith.gitbook.io/polylith)

A Python implementation of the Polylith tool:
[python-polylith](https://github.com/DavidVujic/python-polylith)

## Developer experience

### pytest
Have a look at the `pyproject.toml` configuration file, to make `pytest` work really well with this type of architecture.

``` toml
[tool.pytest.ini_options]
consider_namespace_packages = true
```

#### The "loose" theme
This repository is setup with the `loose` theme, a Python exclusive addition to the architecture.
The theme is about the folder structure of components:

`components/<namespace>/<name>`, and a separate `tests` top folder.

Currently, there is poor support in pytest for the original Polylith component structure:

`components/<name>/<src or test>/<namespace>/<name>/`

With the original Polylith structure, refer to python-polylith-example-theme-tdd#1.
Otherwise, you will have to explicitly add each component path to the `pythonpath`.
There is a similar [feature request](https://github.com/python/mypy/issues/9965) in the mypy repo about adding regex support to the `mypy_path` property.
Hopefully it will be implemented in the future. :pray:


### Tests

Run tests with:

```bash
uv run poe test
```

### Deployment

The `example_` projects contain examples for packaging and deploying APIs and handlers with docker,
AWS Lambdas and GCP functions.

#### Kubernetes
The _"My FastAPI project"_ includes an example setup for deploying into a __Kubernetes__ cluser,
by using _kustomize_ to configure the deployments.

Have a look at the [project-specific](./projects/my_fastapi_project/kubernetes) and the [shared](./../../_kubernetes) configurations.

The configuration is structured as:
- basic setup for all types of deployments
    - with overlays for different environments (development, staging, production)
- service-specific setup, with overlays
    - APIs
    - handlers
- project-specific setup, with overlays
