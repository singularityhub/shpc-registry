---
layout: container
name:  "quay.io/biocontainers/advntr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/advntr/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/advntr/container.yaml"
updated_at: "2022-10-27 00:20:04.002952"
latest: "1.4.1--py27h20e14e4_2"
container_url: "https://biocontainers.pro/tools/advntr"
aliases:
 - "adVNTR-Filtering"
 - "advntr"
versions:
 - "1.4.1--py27h20e14e4_2"
description: "shpc-registry automated BioContainers addition for advntr"
config: {"url": "https://biocontainers.pro/tools/advntr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for advntr", "latest": {"1.4.1--py27h20e14e4_2": "sha256:0b569503b0f7a84ffaccd92ad555bdcaf38b9dc30a8d5dd1a2918e124aaec70d"}, "tags": {"1.4.1--py27h20e14e4_2": "sha256:0b569503b0f7a84ffaccd92ad555bdcaf38b9dc30a8d5dd1a2918e124aaec70d"}, "docker": "quay.io/biocontainers/advntr", "aliases": {"adVNTR-Filtering": "/usr/local/bin/adVNTR-Filtering", "advntr": "/usr/local/bin/advntr"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/advntr.
shpc-registry automated BioContainers addition for advntr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/advntr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/advntr:1.4.1--py27h20e14e4_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/advntr/1.4.1--py27h20e14e4_2
$ module help quay.io/biocontainers/advntr/1.4.1--py27h20e14e4_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### advntr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### advntr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### advntr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### advntr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### advntr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### advntr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### adVNTR-Filtering

```bash
$ singularity exec <container> /usr/local/bin/adVNTR-Filtering
$ podman run --it --rm --entrypoint /usr/local/bin/adVNTR-Filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/adVNTR-Filtering   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### advntr

```bash
$ singularity exec <container> /usr/local/bin/advntr
$ podman run --it --rm --entrypoint /usr/local/bin/advntr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/advntr   -v ${PWD} -w ${PWD} <container> -c " $@"
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