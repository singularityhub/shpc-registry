---
layout: container
name:  "quay.io/biocontainers/ms2pip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ms2pip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ms2pip/container.yaml"
updated_at: "2024-07-22 03:24:51.827896"
latest: "4.0.0.dev8--py310h7147d47_0"
container_url: "https://biocontainers.pro/tools/ms2pip"
aliases:
 - "fasta2speclib"
 - "ms2pip"
 - "ms2pip-single-prediction"
 - "xgboost"
 - "pt2to3"
 - "ptdump"
 - "ptrepack"
 - "pttree"
 - "numba"
 - "pycc"
 - "mirror_server"
 - "mirror_server_stop"
 - "jsonschema"
versions:
 - "3.9.0--py39h5371cbf_0"
 - "3.10.0--py39h5371cbf_0"
 - "3.11.0--py39h5371cbf_0"
 - "3.11.0--py310hd6be1da_2"
 - "4.0.0.dev4--py310h7147d47_0"
 - "4.0.0.dev8--py310h7147d47_0"
 - "3.11.0--py38h24c8ff8_2"
 - "3.10.0--py310h79ef01b_0"
 - "3.9.0--py310h79ef01b_0"
description: "shpc-registry automated BioContainers addition for ms2pip"
config: {"url": "https://biocontainers.pro/tools/ms2pip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ms2pip", "latest": {"4.0.0.dev8--py310h7147d47_0": "sha256:7bf2542a085cff5bb3b53afb7c5721a7839e67fdf2c2816b8d886a5184dc7767"}, "tags": {"3.9.0--py39h5371cbf_0": "sha256:fedf933dddebdc976c2e1dfc8d629788992e73ce8be20d9e44ffa99184ec559f", "3.10.0--py39h5371cbf_0": "sha256:ac051375ca0e7793f5b39aa0ba909685c2b4dca66e2cf73262fc91da2bec15a7", "3.11.0--py39h5371cbf_0": "sha256:88e78f7813fe4a77779f8e8c33e9688f0d655674d7a034df5d9ecf3ab2646a13", "3.11.0--py310hd6be1da_2": "sha256:b854effe87e949cd9f9185b9b1fa9558f2612c8b80cd39f8638b5c545a519568", "4.0.0.dev4--py310h7147d47_0": "sha256:c3e98fd2b9f41e1715498d25d60806f252713aff055a6df5f68543ce6eb62e35", "4.0.0.dev8--py310h7147d47_0": "sha256:7bf2542a085cff5bb3b53afb7c5721a7839e67fdf2c2816b8d886a5184dc7767", "3.11.0--py38h24c8ff8_2": "sha256:9c0c12a031ca7c03512ab33eda4d81347d91f3bf1269a509cfdcc85363e93a04", "3.10.0--py310h79ef01b_0": "sha256:bb489d7c1658963e6b633dda74ac8820e61c42f503ce142dd3266d43ff22974d", "3.9.0--py310h79ef01b_0": "sha256:ffc917b654da4d94994e55f751a250871bb5773a0695b82639e83429d36b7cd5"}, "docker": "quay.io/biocontainers/ms2pip", "aliases": {"fasta2speclib": "/usr/local/bin/fasta2speclib", "ms2pip": "/usr/local/bin/ms2pip", "ms2pip-single-prediction": "/usr/local/bin/ms2pip-single-prediction", "xgboost": "/usr/local/bin/xgboost", "pt2to3": "/usr/local/bin/pt2to3", "ptdump": "/usr/local/bin/ptdump", "ptrepack": "/usr/local/bin/ptrepack", "pttree": "/usr/local/bin/pttree", "numba": "/usr/local/bin/numba", "pycc": "/usr/local/bin/pycc", "mirror_server": "/usr/local/bin/mirror_server", "mirror_server_stop": "/usr/local/bin/mirror_server_stop", "jsonschema": "/usr/local/bin/jsonschema"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ms2pip.
shpc-registry automated BioContainers addition for ms2pip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ms2pip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ms2pip:4.0.0.dev8--py310h7147d47_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ms2pip/4.0.0.dev8--py310h7147d47_0
$ module help quay.io/biocontainers/ms2pip/4.0.0.dev8--py310h7147d47_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ms2pip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ms2pip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ms2pip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ms2pip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ms2pip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ms2pip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasta2speclib

```bash
$ singularity exec <container> /usr/local/bin/fasta2speclib
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2speclib   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2speclib   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ms2pip

```bash
$ singularity exec <container> /usr/local/bin/ms2pip
$ podman run --it --rm --entrypoint /usr/local/bin/ms2pip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ms2pip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ms2pip-single-prediction

```bash
$ singularity exec <container> /usr/local/bin/ms2pip-single-prediction
$ podman run --it --rm --entrypoint /usr/local/bin/ms2pip-single-prediction   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ms2pip-single-prediction   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xgboost

```bash
$ singularity exec <container> /usr/local/bin/xgboost
$ podman run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgboost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pt2to3

```bash
$ singularity exec <container> /usr/local/bin/pt2to3
$ podman run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pt2to3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptdump

```bash
$ singularity exec <container> /usr/local/bin/ptdump
$ podman run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ptrepack

```bash
$ singularity exec <container> /usr/local/bin/ptrepack
$ podman run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ptrepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pttree

```bash
$ singularity exec <container> /usr/local/bin/pttree
$ podman run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pttree   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### mirror_server

```bash
$ singularity exec <container> /usr/local/bin/mirror_server
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirror_server_stop

```bash
$ singularity exec <container> /usr/local/bin/mirror_server_stop
$ podman run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirror_server_stop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jsonschema

```bash
$ singularity exec <container> /usr/local/bin/jsonschema
$ podman run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jsonschema   -v ${PWD} -w ${PWD} <container> -c " $@"
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