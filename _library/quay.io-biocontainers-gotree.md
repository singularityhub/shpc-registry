---
layout: container
name:  "quay.io/biocontainers/gotree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gotree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gotree/container.yaml"
updated_at: "2023-01-11 20:19:37.821399"
latest: "0.4.3--h4b4d50d_2"
container_url: "https://biocontainers.pro/tools/gotree"
aliases:
 - "gotree"
 - "gotree_test.sh"
versions:
 - "0.4.3--h4b4d50d_2"
description: "shpc-registry automated BioContainers addition for gotree"
config: {"url": "https://biocontainers.pro/tools/gotree", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gotree", "latest": {"0.4.3--h4b4d50d_2": "sha256:3b0f023c7c7860e1854fbfcfcd15f176ff02f3e6f2e01da02477edb51e2b4244"}, "tags": {"0.4.3--h4b4d50d_2": "sha256:3b0f023c7c7860e1854fbfcfcd15f176ff02f3e6f2e01da02477edb51e2b4244"}, "docker": "quay.io/biocontainers/gotree", "aliases": {"gotree": "/usr/local/bin/gotree", "gotree_test.sh": "/usr/local/bin/gotree_test.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gotree.
shpc-registry automated BioContainers addition for gotree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gotree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gotree:0.4.3--h4b4d50d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gotree/0.4.3--h4b4d50d_2
$ module help quay.io/biocontainers/gotree/0.4.3--h4b4d50d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gotree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gotree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gotree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gotree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gotree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gotree-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gotree

```bash
$ singularity exec <container> /usr/local/bin/gotree
$ podman run --it --rm --entrypoint /usr/local/bin/gotree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gotree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gotree_test.sh

```bash
$ singularity exec <container> /usr/local/bin/gotree_test.sh
$ podman run --it --rm --entrypoint /usr/local/bin/gotree_test.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gotree_test.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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