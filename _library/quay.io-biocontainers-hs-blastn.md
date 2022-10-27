---
layout: container
name:  "quay.io/biocontainers/hs-blastn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hs-blastn/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hs-blastn/container.yaml"
updated_at: "2022-10-27 00:24:12.155920"
latest: "0.0.5--h9f5acd7_4"
container_url: "https://biocontainers.pro/tools/hs-blastn"
aliases:
 - "hs-blastn"
versions:
 - "0.0.5--h9f5acd7_4"
description: "shpc-registry automated BioContainers addition for hs-blastn"
config: {"url": "https://biocontainers.pro/tools/hs-blastn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hs-blastn", "latest": {"0.0.5--h9f5acd7_4": "sha256:86d0eb8c71eb209d57b38cc24312448321830088227a89f0b5a943b4823cbba7"}, "tags": {"0.0.5--h9f5acd7_4": "sha256:86d0eb8c71eb209d57b38cc24312448321830088227a89f0b5a943b4823cbba7"}, "docker": "quay.io/biocontainers/hs-blastn", "aliases": {"hs-blastn": "/usr/local/bin/hs-blastn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hs-blastn.
shpc-registry automated BioContainers addition for hs-blastn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hs-blastn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hs-blastn:0.0.5--h9f5acd7_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hs-blastn/0.0.5--h9f5acd7_4
$ module help quay.io/biocontainers/hs-blastn/0.0.5--h9f5acd7_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hs-blastn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hs-blastn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hs-blastn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hs-blastn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hs-blastn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hs-blastn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hs-blastn

```bash
$ singularity exec <container> /usr/local/bin/hs-blastn
$ podman run --it --rm --entrypoint /usr/local/bin/hs-blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hs-blastn   -v ${PWD} -w ${PWD} <container> -c " $@"
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