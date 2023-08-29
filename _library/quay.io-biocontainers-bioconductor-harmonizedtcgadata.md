---
layout: container
name:  "quay.io/biocontainers/bioconductor-harmonizedtcgadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-harmonizedtcgadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-harmonizedtcgadata/container.yaml"
updated_at: "2023-08-29 03:51:38.495380"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-harmonizedtcgadata"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_1"
 - "1.14.0--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.0--r40_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-harmonizedtcgadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-harmonizedtcgadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-harmonizedtcgadata", "latest": {"1.22.0--r43hdfd78af_0": "sha256:20d143cebbe314b2bea8c8efdc00ee4ab6f51549a5f6eb18d5fc303cf35e56e9"}, "tags": {"1.8.0--r36_0": "sha256:b74adf29f129752959f2a20b62e7d17c7f836be131b2932deb2e45678501dfa5", "1.20.0--r42hdfd78af_0": "sha256:3cf91349914dc00e0bb1a7f427c11d85bfdb96413854cd3deadfa46f0695701d", "1.16.0--r41hdfd78af_1": "sha256:35fd3a772f26afc54a75db122f47443bcdf7c088022c2e3b92793c685656923c", "1.14.0--r41hdfd78af_0": "sha256:c10fb228fe58f6ac7d20739fc6e5a1db795f565298ae7f5b682be6fe9d81a9e6", "1.12.0--r40hdfd78af_1": "sha256:8331b98a148d651f762c7f8b3c81b944ac937317b5462b19e568591c710aeaac", "1.10.0--r40_0": "sha256:9a01116c7fc83c175a44318d6fe11ae9f32e77dc56acb542ab1bf6f181e8d380", "1.22.0--r43hdfd78af_0": "sha256:20d143cebbe314b2bea8c8efdc00ee4ab6f51549a5f6eb18d5fc303cf35e56e9"}, "docker": "quay.io/biocontainers/bioconductor-harmonizedtcgadata", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-harmonizedtcgadata.
shpc-registry automated BioContainers addition for bioconductor-harmonizedtcgadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-harmonizedtcgadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-harmonizedtcgadata:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-harmonizedtcgadata/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-harmonizedtcgadata/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-harmonizedtcgadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harmonizedtcgadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-harmonizedtcgadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-harmonizedtcgadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-harmonizedtcgadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-harmonizedtcgadata-inspect-deffile:

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