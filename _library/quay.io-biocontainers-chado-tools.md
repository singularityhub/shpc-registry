---
layout: container
name:  "quay.io/biocontainers/chado-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chado-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/chado-tools/container.yaml"
updated_at: "2024-02-18 03:02:25.250606"
latest: "0.2.15--py_0"
container_url: "https://biocontainers.pro/tools/chado-tools"
aliases:
 - "chado"
 - "pronto"
 - "gffutils-cli"
 - "activate-global-python-argcomplete"
 - "pybabel"
 - "python-argcomplete-check-easy-install-script"
 - "python-argcomplete-tcsh"
 - "register-python-argcomplete"
 - "faidx"
 - "pg_config"
 - "2to3-3.6"
 - "idle3.6"
versions:
 - "0.2.8--py_0"
 - "0.2.15--py_0"
description: "shpc-registry automated BioContainers addition for chado-tools"
config: {"url": "https://biocontainers.pro/tools/chado-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chado-tools", "latest": {"0.2.15--py_0": "sha256:05ddf1c7f51f5b2f0f180e69766714b5d66178dd6f044be4dfab2306100b8983"}, "tags": {"0.2.8--py_0": "sha256:1d061eabf655fde26f2043d18f1274271252d8d67f1613db0ec7cd2fd122d9da", "0.2.15--py_0": "sha256:05ddf1c7f51f5b2f0f180e69766714b5d66178dd6f044be4dfab2306100b8983"}, "docker": "quay.io/biocontainers/chado-tools", "aliases": {"chado": "/usr/local/bin/chado", "pronto": "/usr/local/bin/pronto", "gffutils-cli": "/usr/local/bin/gffutils-cli", "activate-global-python-argcomplete": "/usr/local/bin/activate-global-python-argcomplete", "pybabel": "/usr/local/bin/pybabel", "python-argcomplete-check-easy-install-script": "/usr/local/bin/python-argcomplete-check-easy-install-script", "python-argcomplete-tcsh": "/usr/local/bin/python-argcomplete-tcsh", "register-python-argcomplete": "/usr/local/bin/register-python-argcomplete", "faidx": "/usr/local/bin/faidx", "pg_config": "/usr/local/bin/pg_config", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chado-tools.
shpc-registry automated BioContainers addition for chado-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chado-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chado-tools:0.2.15--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chado-tools/0.2.15--py_0
$ module help quay.io/biocontainers/chado-tools/0.2.15--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chado-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chado-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chado-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chado-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chado-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chado-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chado

```bash
$ singularity exec <container> /usr/local/bin/chado
$ podman run --it --rm --entrypoint /usr/local/bin/chado   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chado   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pronto

```bash
$ singularity exec <container> /usr/local/bin/pronto
$ podman run --it --rm --entrypoint /usr/local/bin/pronto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pronto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffutils-cli

```bash
$ singularity exec <container> /usr/local/bin/gffutils-cli
$ podman run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffutils-cli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### activate-global-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/activate-global-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/activate-global-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-check-easy-install-script

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-check-easy-install-script
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-check-easy-install-script   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python-argcomplete-tcsh

```bash
$ singularity exec <container> /usr/local/bin/python-argcomplete-tcsh
$ podman run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python-argcomplete-tcsh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### register-python-argcomplete

```bash
$ singularity exec <container> /usr/local/bin/register-python-argcomplete
$ podman run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/register-python-argcomplete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faidx

```bash
$ singularity exec <container> /usr/local/bin/faidx
$ podman run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faidx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_config

```bash
$ singularity exec <container> /usr/local/bin/pg_config
$ podman run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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