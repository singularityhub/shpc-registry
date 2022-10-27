---
layout: container
name:  "quay.io/biocontainers/chiron"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/chiron/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/chiron/container.yaml"
updated_at: "2022-10-27 00:40:58.484733"
latest: "0.6.1.1--py_0"
container_url: "https://biocontainers.pro/tools/chiron"
aliases:
 - "chiron"
versions:
 - "0.6.1.1--py_0"
description: "shpc-registry automated BioContainers addition for chiron"
config: {"url": "https://biocontainers.pro/tools/chiron", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for chiron", "latest": {"0.6.1.1--py_0": "sha256:84bb15be72fb143b4465ff240b488ff43f398b756ad436324a26a1f79a186072"}, "tags": {"0.6.1.1--py_0": "sha256:84bb15be72fb143b4465ff240b488ff43f398b756ad436324a26a1f79a186072"}, "docker": "quay.io/biocontainers/chiron", "aliases": {"chiron": "/usr/local/bin/chiron"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/chiron.
shpc-registry automated BioContainers addition for chiron
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/chiron
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/chiron:0.6.1.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/chiron/0.6.1.1--py_0
$ module help quay.io/biocontainers/chiron/0.6.1.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### chiron-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### chiron-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### chiron-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### chiron-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### chiron-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### chiron-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### chiron

```bash
$ singularity exec <container> /usr/local/bin/chiron
$ podman run --it --rm --entrypoint /usr/local/bin/chiron   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chiron   -v ${PWD} -w ${PWD} <container> -c " $@"
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