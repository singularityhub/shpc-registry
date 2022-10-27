---
layout: container
name:  "quay.io/biocontainers/ms2pip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ms2pip/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ms2pip/container.yaml"
updated_at: "2022-10-27 00:50:04.384125"
latest: "3.9.0--py39h5371cbf_0"
container_url: "https://biocontainers.pro/tools/ms2pip"
aliases:
 - "fasta2speclib"
 - "ms2pip"
 - "ms2pip-single-prediction"
versions:
 - "3.9.0--py39h5371cbf_0"
description: "shpc-registry automated BioContainers addition for ms2pip"
config: {"url": "https://biocontainers.pro/tools/ms2pip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ms2pip", "latest": {"3.9.0--py39h5371cbf_0": "sha256:fedf933dddebdc976c2e1dfc8d629788992e73ce8be20d9e44ffa99184ec559f"}, "tags": {"3.9.0--py39h5371cbf_0": "sha256:fedf933dddebdc976c2e1dfc8d629788992e73ce8be20d9e44ffa99184ec559f"}, "docker": "quay.io/biocontainers/ms2pip", "aliases": {"fasta2speclib": "/usr/local/bin/fasta2speclib", "ms2pip": "/usr/local/bin/ms2pip", "ms2pip-single-prediction": "/usr/local/bin/ms2pip-single-prediction"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ms2pip.
shpc-registry automated BioContainers addition for ms2pip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ms2pip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ms2pip:3.9.0--py39h5371cbf_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ms2pip/3.9.0--py39h5371cbf_0
$ module help quay.io/biocontainers/ms2pip/3.9.0--py39h5371cbf_0
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