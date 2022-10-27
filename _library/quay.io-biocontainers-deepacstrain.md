---
layout: container
name:  "quay.io/biocontainers/deepacstrain"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepacstrain/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepacstrain/container.yaml"
updated_at: "2022-10-27 00:51:58.297995"
latest: "0.2.1--py_0"
container_url: "https://biocontainers.pro/tools/deepacstrain"
aliases:
 - "deepac"
 - "deepac-strain"
 - "pyjwt"
versions:
 - "0.2.1--py_0"
description: "shpc-registry automated BioContainers addition for deepacstrain"
config: {"url": "https://biocontainers.pro/tools/deepacstrain", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepacstrain", "latest": {"0.2.1--py_0": "sha256:1f46e7ed53b6bf873c334911e196a7197b34948be6f6a7904d3a337c8b4a929a"}, "tags": {"0.2.1--py_0": "sha256:1f46e7ed53b6bf873c334911e196a7197b34948be6f6a7904d3a337c8b4a929a"}, "docker": "quay.io/biocontainers/deepacstrain", "aliases": {"deepac": "/usr/local/bin/deepac", "deepac-strain": "/usr/local/bin/deepac-strain", "pyjwt": "/usr/local/bin/pyjwt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepacstrain.
shpc-registry automated BioContainers addition for deepacstrain
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepacstrain
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepacstrain:0.2.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepacstrain/0.2.1--py_0
$ module help quay.io/biocontainers/deepacstrain/0.2.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepacstrain-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepacstrain-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepacstrain-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepacstrain-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepacstrain-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepacstrain-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepac

```bash
$ singularity exec <container> /usr/local/bin/deepac
$ podman run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deepac-strain

```bash
$ singularity exec <container> /usr/local/bin/deepac-strain
$ podman run --it --rm --entrypoint /usr/local/bin/deepac-strain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepac-strain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyjwt

```bash
$ singularity exec <container> /usr/local/bin/pyjwt
$ podman run --it --rm --entrypoint /usr/local/bin/pyjwt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyjwt   -v ${PWD} -w ${PWD} <container> -c " $@"
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