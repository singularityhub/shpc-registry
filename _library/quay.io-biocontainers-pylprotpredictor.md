---
layout: container
name:  "quay.io/biocontainers/pylprotpredictor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pylprotpredictor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pylprotpredictor/container.yaml"
updated_at: "2024-07-28 02:45:53.316748"
latest: "1.0.2--pyh864c0ab_1"
container_url: "https://biocontainers.pro/tools/pylprotpredictor"
aliases:
 - "PylProtPredictor"
 - "codecov"
 - "flake8"
 - "pycodestyle"
 - "pyflakes"
 - "pylprotpredictor"
 - "coverage"
 - "diamond"
 - "py.test"
 - "pytest"
 - "prodigal"
 - "f2py3.8"
 - "chardetect"
 - "2to3-3.8"
 - "idle3.8"
 - "pydoc3.8"
versions:
 - "1.0.2--pyh864c0ab_1"
description: "shpc-registry automated BioContainers addition for pylprotpredictor"
config: {"url": "https://biocontainers.pro/tools/pylprotpredictor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pylprotpredictor", "latest": {"1.0.2--pyh864c0ab_1": "sha256:6053728952de731cdf0d5387138df229303ecf6597b2820e011a69fd69a2fc78"}, "tags": {"1.0.2--pyh864c0ab_1": "sha256:6053728952de731cdf0d5387138df229303ecf6597b2820e011a69fd69a2fc78"}, "docker": "quay.io/biocontainers/pylprotpredictor", "aliases": {"PylProtPredictor": "/usr/local/bin/PylProtPredictor", "codecov": "/usr/local/bin/codecov", "flake8": "/usr/local/bin/flake8", "pycodestyle": "/usr/local/bin/pycodestyle", "pyflakes": "/usr/local/bin/pyflakes", "pylprotpredictor": "/usr/local/bin/pylprotpredictor", "coverage": "/usr/local/bin/coverage", "diamond": "/usr/local/bin/diamond", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "prodigal": "/usr/local/bin/prodigal", "f2py3.8": "/usr/local/bin/f2py3.8", "chardetect": "/usr/local/bin/chardetect", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8", "pydoc3.8": "/usr/local/bin/pydoc3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pylprotpredictor.
shpc-registry automated BioContainers addition for pylprotpredictor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pylprotpredictor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pylprotpredictor:1.0.2--pyh864c0ab_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pylprotpredictor/1.0.2--pyh864c0ab_1
$ module help quay.io/biocontainers/pylprotpredictor/1.0.2--pyh864c0ab_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pylprotpredictor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pylprotpredictor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pylprotpredictor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pylprotpredictor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pylprotpredictor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pylprotpredictor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### PylProtPredictor

```bash
$ singularity exec <container> /usr/local/bin/PylProtPredictor
$ podman run --it --rm --entrypoint /usr/local/bin/PylProtPredictor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PylProtPredictor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### codecov

```bash
$ singularity exec <container> /usr/local/bin/codecov
$ podman run --it --rm --entrypoint /usr/local/bin/codecov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/codecov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flake8

```bash
$ singularity exec <container> /usr/local/bin/flake8
$ podman run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flake8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycodestyle

```bash
$ singularity exec <container> /usr/local/bin/pycodestyle
$ podman run --it --rm --entrypoint /usr/local/bin/pycodestyle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycodestyle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyflakes

```bash
$ singularity exec <container> /usr/local/bin/pyflakes
$ podman run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyflakes   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylprotpredictor

```bash
$ singularity exec <container> /usr/local/bin/pylprotpredictor
$ podman run --it --rm --entrypoint /usr/local/bin/pylprotpredictor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylprotpredictor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverage

```bash
$ singularity exec <container> /usr/local/bin/coverage
$ podman run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diamond

```bash
$ singularity exec <container> /usr/local/bin/diamond
$ podman run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diamond   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prodigal

```bash
$ singularity exec <container> /usr/local/bin/prodigal
$ podman run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prodigal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### f2py3.8

```bash
$ singularity exec <container> /usr/local/bin/f2py3.8
$ podman run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/f2py3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chardetect

```bash
$ singularity exec <container> /usr/local/bin/chardetect
$ podman run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chardetect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.8

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.8
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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