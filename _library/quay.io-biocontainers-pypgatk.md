---
layout: container
name:  "quay.io/biocontainers/pypgatk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pypgatk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pypgatk/container.yaml"
updated_at: "2022-10-27 01:10:00.308140"
latest: "0.0.9--py_0"
container_url: "https://biocontainers.pro/tools/pypgatk"
aliases:
 - "epylint"
 - "isort"
 - "isort-identify-imports"
 - "pylint"
 - "pypgatk_cli"
 - "pypgatk_cli.py"
 - "pyreverse"
 - "symilar"
versions:
 - "0.0.9--py_0"
description: "shpc-registry automated BioContainers addition for pypgatk"
config: {"url": "https://biocontainers.pro/tools/pypgatk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pypgatk", "latest": {"0.0.9--py_0": "sha256:4c138a46ab6a268e846074e41a776e1b7d61e27cd4eaa558f48e4ebc21d7cfbc"}, "tags": {"0.0.9--py_0": "sha256:4c138a46ab6a268e846074e41a776e1b7d61e27cd4eaa558f48e4ebc21d7cfbc"}, "docker": "quay.io/biocontainers/pypgatk", "aliases": {"epylint": "/usr/local/bin/epylint", "isort": "/usr/local/bin/isort", "isort-identify-imports": "/usr/local/bin/isort-identify-imports", "pylint": "/usr/local/bin/pylint", "pypgatk_cli": "/usr/local/bin/pypgatk_cli", "pypgatk_cli.py": "/usr/local/bin/pypgatk_cli.py", "pyreverse": "/usr/local/bin/pyreverse", "symilar": "/usr/local/bin/symilar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pypgatk.
shpc-registry automated BioContainers addition for pypgatk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pypgatk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pypgatk:0.0.9--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pypgatk/0.0.9--py_0
$ module help quay.io/biocontainers/pypgatk/0.0.9--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pypgatk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pypgatk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pypgatk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pypgatk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pypgatk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pypgatk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### epylint

```bash
$ singularity exec <container> /usr/local/bin/epylint
$ podman run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/epylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort

```bash
$ singularity exec <container> /usr/local/bin/isort
$ podman run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isort-identify-imports

```bash
$ singularity exec <container> /usr/local/bin/isort-identify-imports
$ podman run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isort-identify-imports   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pylint

```bash
$ singularity exec <container> /usr/local/bin/pylint
$ podman run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pylint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypgatk_cli

```bash
$ singularity exec <container> /usr/local/bin/pypgatk_cli
$ podman run --it --rm --entrypoint /usr/local/bin/pypgatk_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypgatk_cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pypgatk_cli.py

```bash
$ singularity exec <container> /usr/local/bin/pypgatk_cli.py
$ podman run --it --rm --entrypoint /usr/local/bin/pypgatk_cli.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pypgatk_cli.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyreverse

```bash
$ singularity exec <container> /usr/local/bin/pyreverse
$ podman run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyreverse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### symilar

```bash
$ singularity exec <container> /usr/local/bin/symilar
$ podman run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/symilar   -v ${PWD} -w ${PWD} <container> -c " $@"
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