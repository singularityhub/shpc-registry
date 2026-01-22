---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowtime"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowtime/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowtime/container.yaml"
updated_at: "2026-01-22 04:05:21.393212"
latest: "1.30.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowtime"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.22.0--r42hdfd78af_0"
 - "1.17.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.30.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowtime"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowtime", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowtime", "latest": {"1.30.0--r44hdfd78af_0": "sha256:67d6427e0305095ca00e7c3569c35e2770c0da0924c8be00e03c90e71baec411"}, "tags": {"1.8.0--r36_1": "sha256:10353a9f7267122f3286f7f062884d99775b9ac766bc019367548a8313b1d8df", "1.22.0--r42hdfd78af_0": "sha256:e700a0d13024cf75fc0a270b966ae2a4c4bf054c65c0dfedc4a08cf0c5b06e53", "1.17.0--r41hdfd78af_0": "sha256:dab6100d76e2ad5c247432c1db9dad5e83ca8550337906bba2ba5a0f37f3280e", "1.16.0--r41hdfd78af_0": "sha256:f2921bcf5647ceebf8a900f6492851f7270885111adfeb8ced64938cbf48cd24", "1.14.0--r40hdfd78af_1": "sha256:be4fe7e2c6d700dea4fe7b0e01a667baa0a089ec9561dfa0c02f645870fb0be7", "1.12.0--r40_0": "sha256:46453210c88c580844abbc4ab8ebe3e9f1d2034eb3930631911ef8ac344a8398", "1.24.0--r43hdfd78af_0": "sha256:c92ec18e2d3d489cbdcee747bb418cf3058b8cb9184906491c6710175f73cf83", "1.26.0--r43hdfd78af_0": "sha256:dea9ce52237f0e6e03678ce6f80e00504bc6749621decbddf885f05d56cf6d6b", "1.30.0--r44hdfd78af_0": "sha256:67d6427e0305095ca00e7c3569c35e2770c0da0924c8be00e03c90e71baec411"}, "docker": "quay.io/biocontainers/bioconductor-flowtime", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowtime.
shpc-registry automated BioContainers addition for bioconductor-flowtime
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowtime
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowtime:1.30.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowtime/1.30.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowtime/1.30.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowtime-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowtime-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowtime-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowtime-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowtime-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowtime-inspect-deffile:

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