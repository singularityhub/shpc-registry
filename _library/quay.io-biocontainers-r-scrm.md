---
layout: container
name:  "quay.io/biocontainers/r-scrm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-scrm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-scrm/container.yaml"
updated_at: "2025-07-17 04:11:23.447015"
latest: "1.7.2_4--r351h29659fb_1"
container_url: "https://biocontainers.pro/tools/r-scrm"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.7.2_4--r351h29659fb_1"
description: "shpc-registry automated BioContainers addition for r-scrm"
config: {"url": "https://biocontainers.pro/tools/r-scrm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-scrm", "latest": {"1.7.2_4--r351h29659fb_1": "sha256:f679cd355d7210adf823d2045d4eeb5bdbef368bf2bbb291de4eddbc6876cd8a"}, "tags": {"1.7.2_4--r351h29659fb_1": "sha256:f679cd355d7210adf823d2045d4eeb5bdbef368bf2bbb291de4eddbc6876cd8a"}, "docker": "quay.io/biocontainers/r-scrm", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-scrm.
shpc-registry automated BioContainers addition for r-scrm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-scrm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-scrm:1.7.2_4--r351h29659fb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-scrm/1.7.2_4--r351h29659fb_1
$ module help quay.io/biocontainers/r-scrm/1.7.2_4--r351h29659fb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-scrm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-scrm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-scrm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-scrm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-scrm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-scrm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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