---
layout: container
name:  "quay.io/biocontainers/deepmased"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepmased/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepmased/container.yaml"
updated_at: "2022-10-27 01:02:45.287516"
latest: "0.3.1--pyh5ca1d4c_0"
container_url: "https://biocontainers.pro/tools/deepmased"
aliases:
 - "DeepMAsED"
versions:
 - "0.3.1--pyh5ca1d4c_0"
description: "shpc-registry automated BioContainers addition for deepmased"
config: {"url": "https://biocontainers.pro/tools/deepmased", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepmased", "latest": {"0.3.1--pyh5ca1d4c_0": "sha256:b609a61f557d37c8a33be24736fe01692c7ac79d0cafec60f98425b9dcd4ef7c"}, "tags": {"0.3.1--pyh5ca1d4c_0": "sha256:b609a61f557d37c8a33be24736fe01692c7ac79d0cafec60f98425b9dcd4ef7c"}, "docker": "quay.io/biocontainers/deepmased", "aliases": {"DeepMAsED": "/usr/local/bin/DeepMAsED"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepmased.
shpc-registry automated BioContainers addition for deepmased
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepmased
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepmased:0.3.1--pyh5ca1d4c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepmased/0.3.1--pyh5ca1d4c_0
$ module help quay.io/biocontainers/deepmased/0.3.1--pyh5ca1d4c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepmased-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepmased-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepmased-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepmased-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepmased-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepmased-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### DeepMAsED

```bash
$ singularity exec <container> /usr/local/bin/DeepMAsED
$ podman run --it --rm --entrypoint /usr/local/bin/DeepMAsED   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/DeepMAsED   -v ${PWD} -w ${PWD} <container> -c " $@"
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