---
layout: container
name:  "quay.io/biocontainers/selene-sdk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/selene-sdk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/selene-sdk/container.yaml"
updated_at: "2022-10-27 00:48:29.797553"
latest: "0.5.0--py37h77a2a36_1"
container_url: "https://biocontainers.pro/tools/selene-sdk"
aliases:
 - ".scikit-learn-post-link.sh"
 - "selene_sdk"
versions:
 - "0.5.0--py37h77a2a36_1"
description: "shpc-registry automated BioContainers addition for selene-sdk"
config: {"url": "https://biocontainers.pro/tools/selene-sdk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for selene-sdk", "latest": {"0.5.0--py37h77a2a36_1": "sha256:58d61ec06edb3441f7d9b2b5dcc0f819a096b134468c6b5b4eda1cae22392d0e"}, "tags": {"0.5.0--py37h77a2a36_1": "sha256:58d61ec06edb3441f7d9b2b5dcc0f819a096b134468c6b5b4eda1cae22392d0e"}, "docker": "quay.io/biocontainers/selene-sdk", "aliases": {".scikit-learn-post-link.sh": "/usr/local/bin/.scikit-learn-post-link.sh", "selene_sdk": "/usr/local/bin/selene_sdk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/selene-sdk.
shpc-registry automated BioContainers addition for selene-sdk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/selene-sdk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/selene-sdk:0.5.0--py37h77a2a36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/selene-sdk/0.5.0--py37h77a2a36_1
$ module help quay.io/biocontainers/selene-sdk/0.5.0--py37h77a2a36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### selene-sdk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### selene-sdk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### selene-sdk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### selene-sdk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### selene-sdk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### selene-sdk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .scikit-learn-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.scikit-learn-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.scikit-learn-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.scikit-learn-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### selene_sdk

```bash
$ singularity exec <container> /usr/local/bin/selene_sdk
$ podman run --it --rm --entrypoint /usr/local/bin/selene_sdk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/selene_sdk   -v ${PWD} -w ${PWD} <container> -c " $@"
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