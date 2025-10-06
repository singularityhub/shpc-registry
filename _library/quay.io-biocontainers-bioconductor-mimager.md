---
layout: container
name:  "quay.io/biocontainers/bioconductor-mimager"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mimager/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mimager/container.yaml"
updated_at: "2025-10-06 03:42:04.970515"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mimager"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mimager"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mimager", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mimager", "latest": {"1.30.0--r44hdfd78af_0": "sha256:4ed7182c9311f9022e90506792019ef012cad0b751c661b88be0b4ff42163962"}, "tags": {"1.8.0--r36_1": "sha256:3827c21fffe6fda5af54efc53567e21a15ecf30b67869551eb1668006c75039c", "1.22.0--r42hdfd78af_0": "sha256:04229fe8084bc75a9e8720c79c916a652df5122583d36eda5b136101cbfac867", "1.18.0--r41hdfd78af_0": "sha256:2f4e19a44e6c24a2a393a0f2788342d77779b62ad7181f40c18ea5192dc77735", "1.16.0--r41hdfd78af_0": "sha256:42ce940470fe14262e92462e96680e41546305db14270005daf4f5c7a9465997", "1.14.0--r40hdfd78af_1": "sha256:7dbf86e987b2ddeb7d789a80f9ae8daf1e88bd766046981150097c50c3498c41", "1.12.0--r40_0": "sha256:ea71a7f9fe9804b2158b25e916321c57294b421a67f2a9fe8bedf8549a1cb9c6", "1.24.0--r43hdfd78af_0": "sha256:928905b85f17608c626d8fabe3703ef87ab608e7d9ffe6f87795e7245d746ff8", "1.26.0--r43hdfd78af_0": "sha256:bd54ea439be0daf79ccd9df57b84c74f3f660a31ab6a3adb68ab079a9665b19b", "1.30.0--r44hdfd78af_0": "sha256:4ed7182c9311f9022e90506792019ef012cad0b751c661b88be0b4ff42163962"}, "docker": "quay.io/biocontainers/bioconductor-mimager", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mimager.
shpc-registry automated BioContainers addition for bioconductor-mimager
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mimager
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mimager:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mimager/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mimager/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mimager-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mimager-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mimager-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mimager-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mimager-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mimager-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
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