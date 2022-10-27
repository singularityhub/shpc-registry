---
layout: container
name:  "quay.io/biocontainers/grafimo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/grafimo/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/grafimo/container.yaml"
updated_at: "2022-10-27 00:25:56.345311"
latest: "1.1.6--py39h5371cbf_0"
container_url: "https://biocontainers.pro/tools/grafimo"
aliases:
 - "grafimo"
 - "vg"
versions:
 - "1.1.6--py39h5371cbf_0"
description: "shpc-registry automated BioContainers addition for grafimo"
config: {"url": "https://biocontainers.pro/tools/grafimo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for grafimo", "latest": {"1.1.6--py39h5371cbf_0": "sha256:c1aac609e9056ed7b9aa3428234568a6068547f82568f5822aebfece8c2e47dd"}, "tags": {"1.1.6--py39h5371cbf_0": "sha256:c1aac609e9056ed7b9aa3428234568a6068547f82568f5822aebfece8c2e47dd"}, "docker": "quay.io/biocontainers/grafimo", "aliases": {"grafimo": "/usr/local/bin/grafimo", "vg": "/usr/local/bin/vg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/grafimo.
shpc-registry automated BioContainers addition for grafimo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/grafimo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/grafimo:1.1.6--py39h5371cbf_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/grafimo/1.1.6--py39h5371cbf_0
$ module help quay.io/biocontainers/grafimo/1.1.6--py39h5371cbf_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### grafimo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### grafimo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### grafimo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### grafimo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### grafimo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### grafimo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### grafimo

```bash
$ singularity exec <container> /usr/local/bin/grafimo
$ podman run --it --rm --entrypoint /usr/local/bin/grafimo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grafimo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vg

```bash
$ singularity exec <container> /usr/local/bin/vg
$ podman run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vg   -v ${PWD} -w ${PWD} <container> -c " $@"
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