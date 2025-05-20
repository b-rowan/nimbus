# nimbus

<img src="docs/logo/large.svg" style="width: 100px; height: 100px; display: block;">

An ASIC miner API standard

## Setup

To set up, ensure you have the `poetry` environment manager installed (https://python-poetry.org/).

```commandline
poetry install
```

## Examples

In order to run the examples, you need to install with the `examples` group.

```commandline
poetry install --with examples
poetry run python3 -m nimbus
```

## Docs

In order to run the docs, you need to install with the `docs` group.

```commandline
poetry install --with docs
poetry run mkdocs serve
```
