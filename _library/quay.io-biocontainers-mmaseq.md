---
layout: container
name:  "quay.io/biocontainers/mmaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmaseq/container.yaml"
updated_at: "2026-06-27 06:14:54.714972"
latest: "1.0.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/mmaseq"
aliases:
 - "menuinst"
 - "mmacreate"
 - "mmadeploy"
 - "mmaseq"
 - "pyproject-build"
 - "python-build"
 - "unearth"
 - "jsondiff"
 - "jsonpatch"
 - "distro"
 - "phc"
 - "idna"
 - "jsonpointer"
 - "mamba-package"
 - "conda2solv"
 - "dumpsolv"
 - "installcheck"
 - "mergesolv"
 - "repo2solv"
 - "testsolv"
 - "archspec"
 - "eido"
 - "cph"
 - "bsdunzip"
 - "httpx"
 - "typer"
 - "rst2html"
 - "rst2html4"
 - "rst2html5"
 - "rst2latex"
 - "rst2man"
 - "rst2odt"
versions:
 - "1.0.0--pyh106432d_0"
description: "singularity registry hpc automated addition for mmaseq"
config: {"url": "https://biocontainers.pro/tools/mmaseq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mmaseq", "latest": {"1.0.0--pyh106432d_0": "sha256:9ef44e316d8b4b99441848c446dcf850914226fa3169a3be0ff47fc6ca3a7216"}, "tags": {"1.0.0--pyh106432d_0": "sha256:9ef44e316d8b4b99441848c446dcf850914226fa3169a3be0ff47fc6ca3a7216"}, "docker": "quay.io/biocontainers/mmaseq", "aliases": {"menuinst": "/usr/local/bin/menuinst", "mmacreate": "/usr/local/bin/mmacreate", "mmadeploy": "/usr/local/bin/mmadeploy", "mmaseq": "/usr/local/bin/mmaseq", "pyproject-build": "/usr/local/bin/pyproject-build", "python-build": "/usr/local/bin/python-build", "unearth": "/usr/local/bin/unearth", "jsondiff": "/usr/local/bin/jsondiff", "jsonpatch": "/usr/local/bin/jsonpatch", "distro": "/usr/local/bin/distro", "phc": "/usr/local/bin/phc", "idna": "/usr/local/bin/idna", "jsonpointer": "/usr/local/bin/jsonpointer", "mamba-package": "/usr/local/bin/mamba-package", "conda2solv": "/usr/local/bin/conda2solv", "dumpsolv": "/usr/local/bin/dumpsolv", "installcheck": "/usr/local/bin/installcheck", "mergesolv": "/usr/local/bin/mergesolv", "repo2solv": "/usr/local/bin/repo2solv", "testsolv": "/usr/local/bin/testsolv", "archspec": "/usr/local/bin/archspec", "eido": "/usr/local/bin/eido", "cph": "/usr/local/bin/cph", "bsdunzip": "/usr/local/bin/bsdunzip", "httpx": "/usr/local/bin/httpx", "typer": "/usr/local/bin/typer", "rst2html": "/usr/local/bin/rst2html", "rst2html4": "/usr/local/bin/rst2html4", "rst2html5": "/usr/local/bin/rst2html5", "rst2latex": "/usr/local/bin/rst2latex", "rst2man": "/usr/local/bin/rst2man", "rst2odt": "/usr/local/bin/rst2odt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmaseq.
singularity registry hpc automated addition for mmaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmaseq:1.0.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmaseq/1.0.0--pyh106432d_0
$ module help quay.io/biocontainers/mmaseq/1.0.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### menuinst

```bash
$ singularity exec <container> /usr/local/bin/menuinst
$ podman run --it --rm --entrypoint /usr/local/bin/menuinst   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/menuinst   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmacreate

```bash
$ singularity exec <container> /usr/local/bin/mmacreate
$ podman run --it --rm --entrypoint /usr/local/bin/mmacreate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmacreate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmadeploy

```bash
$ singularity exec <container> /usr/local/bin/mmadeploy
$ podman run --it --rm --entrypoint /usr/local/bin/mmadeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmadeploy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mmaseq

```bash
$ singularity exec <container> /usr/local/bin/mmaseq
$ podman run --it --rm --entrypoint /usr/local/bin/mmaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmaseq   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### unearth

```bash
$ singularity exec <container> /usr/local/bin/unearth
$ podman run --it --rm --entrypoint /usr/local/bin/unearth   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unearth   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsondiff

```bash
$ singularity exec <container> /usr/local/bin/jsondiff
$ podman run --it --rm --entrypoint /usr/local/bin/jsondiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsondiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpatch

```bash
$ singularity exec <container> /usr/local/bin/jsonpatch
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distro

```bash
$ singularity exec <container> /usr/local/bin/distro
$ podman run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phc

```bash
$ singularity exec <container> /usr/local/bin/phc
$ podman run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idna

```bash
$ singularity exec <container> /usr/local/bin/idna
$ podman run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonpointer

```bash
$ singularity exec <container> /usr/local/bin/jsonpointer
$ podman run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonpointer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda2solv

```bash
$ singularity exec <container> /usr/local/bin/conda2solv
$ podman run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsolv

```bash
$ singularity exec <container> /usr/local/bin/dumpsolv
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installcheck

```bash
$ singularity exec <container> /usr/local/bin/installcheck
$ podman run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergesolv

```bash
$ singularity exec <container> /usr/local/bin/mergesolv
$ podman run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repo2solv

```bash
$ singularity exec <container> /usr/local/bin/repo2solv
$ podman run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testsolv

```bash
$ singularity exec <container> /usr/local/bin/testsolv
$ podman run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archspec

```bash
$ singularity exec <container> /usr/local/bin/archspec
$ podman run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archspec   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eido

```bash
$ singularity exec <container> /usr/local/bin/eido
$ podman run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eido   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cph

```bash
$ singularity exec <container> /usr/local/bin/cph
$ podman run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### httpx

```bash
$ singularity exec <container> /usr/local/bin/httpx
$ podman run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/httpx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### typer

```bash
$ singularity exec <container> /usr/local/bin/typer
$ podman run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/typer   -v ${PWD} -w ${PWD} <container> -c " $@"
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