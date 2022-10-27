---
layout: container
name:  "quay.io/biocontainers/deepsignal-plant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepsignal-plant/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepsignal-plant/container.yaml"
updated_at: "2022-10-27 00:41:52.317556"
latest: "0.1.6--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/deepsignal-plant"
aliases:
 - ".scikit-learn-post-link.sh"
 - "deepsignal_plant"
versions:
 - "0.1.6--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for deepsignal-plant"
config: {"url": "https://biocontainers.pro/tools/deepsignal-plant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepsignal-plant", "latest": {"0.1.6--pyhdfd78af_0": "sha256:739f5d3c829bea63657e237b390c1f09a3bc67f78dbb59d0f2df4aff3a4f0ba5"}, "tags": {"0.1.6--pyhdfd78af_0": "sha256:739f5d3c829bea63657e237b390c1f09a3bc67f78dbb59d0f2df4aff3a4f0ba5"}, "docker": "quay.io/biocontainers/deepsignal-plant", "aliases": {".scikit-learn-post-link.sh": "/usr/local/bin/.scikit-learn-post-link.sh", "deepsignal_plant": "/usr/local/bin/deepsignal_plant"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepsignal-plant.
shpc-registry automated BioContainers addition for deepsignal-plant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepsignal-plant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepsignal-plant:0.1.6--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepsignal-plant/0.1.6--pyhdfd78af_0
$ module help quay.io/biocontainers/deepsignal-plant/0.1.6--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepsignal-plant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepsignal-plant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepsignal-plant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepsignal-plant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepsignal-plant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepsignal-plant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .scikit-learn-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.scikit-learn-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.scikit-learn-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.scikit-learn-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deepsignal_plant

```bash
$ singularity exec <container> /usr/local/bin/deepsignal_plant
$ podman run --it --rm --entrypoint /usr/local/bin/deepsignal_plant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepsignal_plant   -v ${PWD} -w ${PWD} <container> -c " $@"
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