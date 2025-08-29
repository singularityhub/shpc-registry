---
layout: container
name:  "quay.io/biocontainers/hcluster_sg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hcluster_sg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hcluster_sg/container.yaml"
updated_at: "2025-08-29 03:09:15.796934"
latest: "0.5.1--h9948957_9"
container_url: "https://biocontainers.pro/tools/hcluster_sg"
aliases:
 - "hcluster_sg"
versions:
 - "0.5.1--h9f5acd7_5"
 - "0.5.1--h4ac6f70_7"
 - "0.5.1--h9948957_8"
 - "0.5.1--h9948957_9"
description: "shpc-registry automated BioContainers addition for hcluster_sg"
config: {"url": "https://biocontainers.pro/tools/hcluster_sg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hcluster_sg", "latest": {"0.5.1--h9948957_9": "sha256:abbfb289248a2c0d057f13799a21cd7937f5e4058113a63811d9794aa3cfd98c"}, "tags": {"0.5.1--h9f5acd7_5": "sha256:8b707c9e5575e0477169838844f44afdff450576b9834c3a475cdce8a1698d15", "0.5.1--h4ac6f70_7": "sha256:8927b0b938e8c3f53add4eef679b426eaafb782fc32b9131eca91ba03b50aad7", "0.5.1--h9948957_8": "sha256:fcd74c83da3b592e943fd82daea751523d953e918edcac8d05b8cd53387a60ef", "0.5.1--h9948957_9": "sha256:abbfb289248a2c0d057f13799a21cd7937f5e4058113a63811d9794aa3cfd98c"}, "docker": "quay.io/biocontainers/hcluster_sg", "aliases": {"hcluster_sg": "/usr/local/bin/hcluster_sg"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hcluster_sg.
shpc-registry automated BioContainers addition for hcluster_sg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hcluster_sg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hcluster_sg:0.5.1--h9948957_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hcluster_sg/0.5.1--h9948957_9
$ module help quay.io/biocontainers/hcluster_sg/0.5.1--h9948957_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hcluster_sg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hcluster_sg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hcluster_sg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hcluster_sg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hcluster_sg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hcluster_sg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hcluster_sg

```bash
$ singularity exec <container> /usr/local/bin/hcluster_sg
$ podman run --it --rm --entrypoint /usr/local/bin/hcluster_sg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hcluster_sg   -v ${PWD} -w ${PWD} <container> -c " $@"
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