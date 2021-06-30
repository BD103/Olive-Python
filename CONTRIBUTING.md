# Contributing

Olive Python strives to be the most informative guide out there. Here are some tips for developing.

## Development Phase

After cloning the Git, run:

```console
$ poetry lock
$ poetry install
```

I then recommend having two console up. One running `python -m http.server 8000 -d docs` and another rebuilding the page with `make html`.

## Commiting

Always delete the docs folder and rebuild when commiting to the master branch. Sphinx sometimes has small errors when it comes to building, and I'd rather avoid it.
