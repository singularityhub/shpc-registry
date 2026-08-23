---
layout: container
name:  "quay.io/biocontainers/pmotools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pmotools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pmotools/container.yaml"
updated_at: "2026-08-23 03:43:06.623126"
latest: "1.1.0--pyh106432d_0"
container_url: "https://biocontainers.pro/tools/pmotools"
aliases:
 - "cffi-gen-src"
 - "identify-cli"
 - "nodeenv"
 - "pmotools-python"
 - "pre-commit"
 - "virtualenv"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "jsonschema"
 - "numpy-config"
versions:
 - "1.1.0--pyh106432d_0"
description: "singularity registry hpc automated addition for pmotools"
config: {"url": "https://biocontainers.pro/tools/pmotools", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pmotools", "latest": {"1.1.0--pyh106432d_0": "sha256:885fd51c5775b62f1ad5e5d80d2991c453536997d65b7c098e85195686372ecb"}, "tags": {"1.1.0--pyh106432d_0": "sha256:885fd51c5775b62f1ad5e5d80d2991c453536997d65b7c098e85195686372ecb"}, "docker": "quay.io/biocontainers/pmotools", "aliases": {"cffi-gen-src": "/usr/local/bin/cffi-gen-src", "identify-cli": "/usr/local/bin/identify-cli", "nodeenv": "/usr/local/bin/nodeenv", "pmotools-python": "/usr/local/bin/pmotools-python", "pre-commit": "/usr/local/bin/pre-commit", "virtualenv": "/usr/local/bin/virtualenv", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "jsonschema": "/usr/local/bin/jsonschema", "numpy-config": "/usr/local/bin/numpy-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pmotools.
singularity registry hpc automated addition for pmotools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pmotools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pmotools:1.1.0--pyh106432d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pmotools/1.1.0--pyh106432d_0
$ module help quay.io/biocontainers/pmotools/1.1.0--pyh106432d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pmotools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pmotools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pmotools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pmotools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pmotools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pmotools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cffi-gen-src

```bash
$ singularity exec <container> /usr/local/bin/cffi-gen-src
$ podman run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cffi-gen-src   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### identify-cli

```bash
$ singularity exec <container> /usr/local/bin/identify-cli
$ podman run --it --rm --entrypoint /usr/local/bin/identify-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/identify-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nodeenv

```bash
$ singularity exec <container> /usr/local/bin/nodeenv
$ podman run --it --rm --entrypoint /usr/local/bin/nodeenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nodeenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pmotools-python

```bash
$ singularity exec <container> /usr/local/bin/pmotools-python
$ podman run --it --rm --entrypoint /usr/local/bin/pmotools-python   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmotools-python   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pre-commit

```bash
$ singularity exec <container> /usr/local/bin/pre-commit
$ podman run --it --rm --entrypoint /usr/local/bin/pre-commit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pre-commit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### virtualenv

```bash
$ singularity exec <container> /usr/local/bin/virtualenv
$ podman run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/virtualenv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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