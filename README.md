# ss-downloader

Install poetry & Python 3.8+

```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

## how to use

```
source load-env.sh
poetry run python list.py
poetry run python download.py
```

## how this was done

```
poetry-new init
poetry add ssgetpy
```

```
poetry install
```