---
layout: container
name:  "quay.io/biocontainers/paste-bio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/paste-bio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/paste-bio/container.yaml"
updated_at: "2023-12-11 02:34:18.333269"
latest: "1.4.0--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/paste-bio"
aliases:
 - "scanpy"
 - "sphinx-apidoc"
 - "sphinx-autogen"
 - "sphinx-build"
 - "sphinx-quickstart"
 - "pybabel"
 - "numba"
 - "pycc"
 - "natsort"
 - "mirror_server"
versions:
 - "1.3.0--pyh5e36f6f_0"
 - "1.4.0--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for paste-bio"
config: {"url": "https://biocontainers.pro/tools/paste-bio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for paste-bio", "latest": {"1.4.0--pyh7cba7a3_0": "sha256:ddb129786b1a0b1230081a8986329a17fcf2bc5ff300b803557d6dc7c128c733"}, "tags": {"1.3.0--pyh5e36f6f_0": "sha256:dc6cc2816d30796cd5d882873a092da70055416c537f7521edb1ed51040a8752", "1.4.0--pyh7cba7a3_0": "sha256:ddb129786b1a0b1230081a8986329a17fcf2bc5ff300b803557d6dc7c128c733"}, "docker": "quay.io/biocontainers/paste-bio", "aliases": {"scanpy": "/usr/local/bin/scanpy", "sphinx-apidoc": "/usr/local/bin/sphinx-apidoc", "sphinx-autogen": "/usr/local/bin/sphinx-autogen", "sphinx-build": "/usr/local/bin/sphinx-build", "sphinx-quickstart": "/usr/local/bin/sphinx-quickstart", "pybabel": "/usr/local/bin/pybabel", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "natsort": "/usr/local/bin/natsort", "mirror_server": "/usr/local/bin/mirror_server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/paste-bio.
shpc-registry automated BioContainers addition for paste-bio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/paste-bio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/paste-bio:1.4.0--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/paste-bio/1.4.0--pyh7cba7a3_0
$ module help quay.io/biocontainers/paste-bio/1.4.0--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### paste-bio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### paste-bio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### paste-bio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### paste-bio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### paste-bio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### paste-bio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-apidoc

```bash
$ singularity exec <container> /usr/local/bin/sphinx-apidoc
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-apidoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-autogen

```bash
$ singularity exec <container> /usr/local/bin/sphinx-autogen
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-autogen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-build

```bash
$ singularity exec <container> /usr/local/bin/sphinx-build
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sphinx-quickstart

```bash
$ singularity exec <container> /usr/local/bin/sphinx-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sphinx-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybabel

```bash
$ singularity exec <container> /usr/local/bin/pybabel
$ podman run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numba

```bash
$ singularity exec <container> /usr/local/bin/numba
$ podman run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pycc

```bash
$ singularity exec <container> /usr/local/bin/pycc
$ podman run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pycc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
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