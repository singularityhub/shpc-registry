---
layout: container
name:  "quay.io/biocontainers/jarvis3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/jarvis3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/jarvis3/container.yaml"
updated_at: "2025-01-18 03:14:36.361869"
latest: "3.7--h7b50bb2_3"
container_url: "https://biocontainers.pro/tools/jarvis3"
aliases:
 - "JARVIS3"
 - "JARVIS3.sh"
 - "JARVIS3.sh.bak"
 - "XScoreC"
 - "XScoreD"
versions:
 - "3.7--h031d066_1"
 - "3.7--h031d066_2"
 - "3.7--h7b50bb2_3"
description: "singularity registry hpc automated addition for jarvis3"
config: {"url": "https://biocontainers.pro/tools/jarvis3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for jarvis3", "latest": {"3.7--h7b50bb2_3": "sha256:cfd9eae1a261d94bcff77f8e8e7761fd8eaf326490feec9688826d705365b9e8"}, "tags": {"3.7--h031d066_1": "sha256:599b15086e057612cc1cf3d0278d93692df3131130e73b8f4b964d0d1093a982", "3.7--h031d066_2": "sha256:531cccca30b664bcdeba2cd7154b75e5687a63aa0fedd68174a42b3fa9a9cab1", "3.7--h7b50bb2_3": "sha256:cfd9eae1a261d94bcff77f8e8e7761fd8eaf326490feec9688826d705365b9e8"}, "docker": "quay.io/biocontainers/jarvis3", "aliases": {"JARVIS3": "/usr/local/bin/JARVIS3", "JARVIS3.sh": "/usr/local/bin/JARVIS3.sh", "JARVIS3.sh.bak": "/usr/local/bin/JARVIS3.sh.bak", "XScoreC": "/usr/local/bin/XScoreC", "XScoreD": "/usr/local/bin/XScoreD"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/jarvis3.
singularity registry hpc automated addition for jarvis3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/jarvis3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/jarvis3:3.7--h7b50bb2_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/jarvis3/3.7--h7b50bb2_3
$ module help quay.io/biocontainers/jarvis3/3.7--h7b50bb2_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jarvis3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jarvis3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jarvis3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jarvis3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jarvis3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jarvis3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### JARVIS3

```bash
$ singularity exec <container> /usr/local/bin/JARVIS3
$ podman run --it --rm --entrypoint /usr/local/bin/JARVIS3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JARVIS3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JARVIS3.sh

```bash
$ singularity exec <container> /usr/local/bin/JARVIS3.sh
$ podman run --it --rm --entrypoint /usr/local/bin/JARVIS3.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JARVIS3.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### JARVIS3.sh.bak

```bash
$ singularity exec <container> /usr/local/bin/JARVIS3.sh.bak
$ podman run --it --rm --entrypoint /usr/local/bin/JARVIS3.sh.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/JARVIS3.sh.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### XScoreC

```bash
$ singularity exec <container> /usr/local/bin/XScoreC
$ podman run --it --rm --entrypoint /usr/local/bin/XScoreC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/XScoreC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### XScoreD

```bash
$ singularity exec <container> /usr/local/bin/XScoreD
$ podman run --it --rm --entrypoint /usr/local/bin/XScoreD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/XScoreD   -v ${PWD} -w ${PWD} <container> -c " $@"
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