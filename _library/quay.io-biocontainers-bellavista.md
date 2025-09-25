---
layout: container
name:  "quay.io/biocontainers/bellavista"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bellavista/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bellavista/container.yaml"
updated_at: "2025-09-25 03:34:35.126002"
latest: "0.0.2--pyhdfd78af_1"
container_url: "https://biocontainers.pro/tools/bellavista"
aliases:
 - "bellavista"
 - "debugpy"
 - "debugpy-adapter"
 - "napari"
 - "npe2"
 - "numpydoc"
 - "ome_zarr"
 - "pax11publish"
 - "pint-convert"
 - "protoc-29.3.0"
 - "protoc-gen-upb"
 - "protoc-gen-upb-29.3.0"
 - "protoc-gen-upb_minitable"
 - "protoc-gen-upb_minitable-29.3.0"
 - "protoc-gen-upbdefs"
 - "protoc-gen-upbdefs-29.3.0"
 - "pyproject-build"
 - "python-build"
 - "qtpy"
 - "ldapadd"
 - "ldapcompare"
 - "ldapdelete"
 - "ldapexop"
 - "ldapmodify"
 - "ldapmodrdn"
 - "ldappasswd"
 - "ldapsearch"
 - "ldapurl"
 - "ldapvc"
 - "ldapwhoami"
 - "typer"
 - "dotenv"
 - "checksum-profile"
 - "elastishadow"
 - "jupyter-qtconsole"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
 - "rst2pseudoxml"
 - "rst2s5"
 - "rst2xetex"
versions:
 - "0.0.2--pyhdfd78af_1"
description: "singularity registry hpc automated addition for bellavista"
config: {"url": "https://biocontainers.pro/tools/bellavista", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bellavista", "latest": {"0.0.2--pyhdfd78af_1": "sha256:ff29407f9f29cd991d85499d42403de1b06369391ffa8be3edb9ddd17d979f3a"}, "tags": {"0.0.2--pyhdfd78af_1": "sha256:ff29407f9f29cd991d85499d42403de1b06369391ffa8be3edb9ddd17d979f3a"}, "docker": "quay.io/biocontainers/bellavista", "aliases": {"bellavista": "/usr/local/bin/bellavista", "debugpy": "/usr/local/bin/debugpy", "debugpy-adapter": "/usr/local/bin/debugpy-adapter", "napari": "/usr/local/bin/napari", "npe2": "/usr/local/bin/npe2", "numpydoc": "/usr/local/bin/numpydoc", "ome_zarr": "/usr/local/bin/ome_zarr", "pax11publish": "/usr/local/bin/pax11publish", "pint-convert": "/usr/local/bin/pint-convert", "protoc-29.3.0": "/usr/local/bin/protoc-29.3.0", "protoc-gen-upb": "/usr/local/bin/protoc-gen-upb", "protoc-gen-upb-29.3.0": "/usr/local/bin/protoc-gen-upb-29.3.0", "protoc-gen-upb_minitable": "/usr/local/bin/protoc-gen-upb_minitable", "protoc-gen-upb_minitable-29.3.0": "/usr/local/bin/protoc-gen-upb_minitable-29.3.0", "protoc-gen-upbdefs": "/usr/local/bin/protoc-gen-upbdefs", "protoc-gen-upbdefs-29.3.0": "/usr/local/bin/protoc-gen-upbdefs-29.3.0", "pyproject-build": "/usr/local/bin/pyproject-build", "python-build": "/usr/local/bin/python-build", "qtpy": "/usr/local/bin/qtpy", "ldapadd": "/usr/local/bin/ldapadd", "ldapcompare": "/usr/local/bin/ldapcompare", "ldapdelete": "/usr/local/bin/ldapdelete", "ldapexop": "/usr/local/bin/ldapexop", "ldapmodify": "/usr/local/bin/ldapmodify", "ldapmodrdn": "/usr/local/bin/ldapmodrdn", "ldappasswd": "/usr/local/bin/ldappasswd", "ldapsearch": "/usr/local/bin/ldapsearch", "ldapurl": "/usr/local/bin/ldapurl", "ldapvc": "/usr/local/bin/ldapvc", "ldapwhoami": "/usr/local/bin/ldapwhoami", "typer": "/usr/local/bin/typer", "dotenv": "/usr/local/bin/dotenv", "checksum-profile": "/usr/local/bin/checksum-profile", "elastishadow": "/usr/local/bin/elastishadow", "jupyter-qtconsole": "/usr/local/bin/jupyter-qtconsole", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt", "rst2pseudoxml": "/usr/local/bin/rst2pseudoxml", "rst2s5": "/usr/local/bin/rst2s5", "rst2xetex": "/usr/local/bin/rst2xetex"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bellavista.
singularity registry hpc automated addition for bellavista
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bellavista
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bellavista:0.0.2--pyhdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bellavista/0.0.2--pyhdfd78af_1
$ module help quay.io/biocontainers/bellavista/0.0.2--pyhdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bellavista-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bellavista-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bellavista-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bellavista-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bellavista-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bellavista-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bellavista

```bash
$ singularity exec <container> /usr/local/bin/bellavista
$ podman run --it --rm --entrypoint /usr/local/bin/bellavista   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bellavista   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy

```bash
$ singularity exec <container> /usr/local/bin/debugpy
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debugpy-adapter

```bash
$ singularity exec <container> /usr/local/bin/debugpy-adapter
$ podman run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debugpy-adapter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### napari

```bash
$ singularity exec <container> /usr/local/bin/napari
$ podman run --it --rm --entrypoint /usr/local/bin/napari   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/napari   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npe2

```bash
$ singularity exec <container> /usr/local/bin/npe2
$ podman run --it --rm --entrypoint /usr/local/bin/npe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npe2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpydoc

```bash
$ singularity exec <container> /usr/local/bin/numpydoc
$ podman run --it --rm --entrypoint /usr/local/bin/numpydoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpydoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ome_zarr

```bash
$ singularity exec <container> /usr/local/bin/ome_zarr
$ podman run --it --rm --entrypoint /usr/local/bin/ome_zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ome_zarr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pax11publish

```bash
$ singularity exec <container> /usr/local/bin/pax11publish
$ podman run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pax11publish   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pint-convert

```bash
$ singularity exec <container> /usr/local/bin/pint-convert
$ podman run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pint-convert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upb_minitable-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upb_minitable-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upb_minitable-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-gen-upbdefs-29.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-gen-upbdefs-29.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-gen-upbdefs-29.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyproject-build

```bash
$ singularity exec <container> /usr/local/bin/pyproject-build
$ podman run --it --rm --entrypoint /usr/local/bin/pyproject-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyproject-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-build

```bash
$ singularity exec <container> /usr/local/bin/python-build
$ podman run --it --rm --entrypoint /usr/local/bin/python-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qtpy

```bash
$ singularity exec <container> /usr/local/bin/qtpy
$ podman run --it --rm --entrypoint /usr/local/bin/qtpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qtpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapadd

```bash
$ singularity exec <container> /usr/local/bin/ldapadd
$ podman run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapadd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapcompare

```bash
$ singularity exec <container> /usr/local/bin/ldapcompare
$ podman run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapdelete

```bash
$ singularity exec <container> /usr/local/bin/ldapdelete
$ podman run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapdelete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapexop

```bash
$ singularity exec <container> /usr/local/bin/ldapexop
$ podman run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapexop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodify

```bash
$ singularity exec <container> /usr/local/bin/ldapmodify
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapmodrdn

```bash
$ singularity exec <container> /usr/local/bin/ldapmodrdn
$ podman run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapmodrdn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldappasswd

```bash
$ singularity exec <container> /usr/local/bin/ldappasswd
$ podman run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldappasswd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapsearch

```bash
$ singularity exec <container> /usr/local/bin/ldapsearch
$ podman run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapurl

```bash
$ singularity exec <container> /usr/local/bin/ldapurl
$ podman run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapurl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapvc

```bash
$ singularity exec <container> /usr/local/bin/ldapvc
$ podman run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapvc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ldapwhoami

```bash
$ singularity exec <container> /usr/local/bin/ldapwhoami
$ podman run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ldapwhoami   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dotenv

```bash
$ singularity exec <container> /usr/local/bin/dotenv
$ podman run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dotenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checksum-profile

```bash
$ singularity exec <container> /usr/local/bin/checksum-profile
$ podman run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checksum-profile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### elastishadow

```bash
$ singularity exec <container> /usr/local/bin/elastishadow
$ podman run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/elastishadow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jupyter-qtconsole

```bash
$ singularity exec <container> /usr/local/bin/jupyter-qtconsole
$ podman run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jupyter-qtconsole   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html

```bash
$ singularity exec <container> /usr/local/bin/rst2html
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html4

```bash
$ singularity exec <container> /usr/local/bin/rst2html4
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2html5

```bash
$ singularity exec <container> /usr/local/bin/rst2html5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2html5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2latex

```bash
$ singularity exec <container> /usr/local/bin/rst2latex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2latex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2man

```bash
$ singularity exec <container> /usr/local/bin/rst2man
$ podman run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2man   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2odt

```bash
$ singularity exec <container> /usr/local/bin/rst2odt
$ podman run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2odt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2pseudoxml

```bash
$ singularity exec <container> /usr/local/bin/rst2pseudoxml
$ podman run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2pseudoxml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2s5

```bash
$ singularity exec <container> /usr/local/bin/rst2s5
$ podman run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2s5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rst2xetex

```bash
$ singularity exec <container> /usr/local/bin/rst2xetex
$ podman run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rst2xetex   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)