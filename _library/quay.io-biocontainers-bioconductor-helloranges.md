---
layout: container
name:  "quay.io/biocontainers/bioconductor-helloranges"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-helloranges/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-helloranges/container.yaml"
updated_at: "2024-02-29 02:36:21.727715"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-helloranges"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-helloranges"
config: {"url": "https://biocontainers.pro/tools/bioconductor-helloranges", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-helloranges", "latest": {"1.28.0--r43hdfd78af_0": "sha256:f294897f3d4c28ed7643c63c63daeb2090f26bb9fdec0ddee486419dd8c8ab52"}, "tags": {"1.8.0--r351_0": "sha256:189ed97f8eff30a1265686dcc923cdcc01a2bf523dec06021990637ef155d2d4", "1.24.0--r42hdfd78af_0": "sha256:192af8b544e2b7cb6e1a07f8958b7220091e28405d315ff3d587ae97f0024c03", "1.20.0--r41hdfd78af_0": "sha256:5508a03897455c0746bd2b3d63d02580e32a1f6513f077a53eb3eba5d7e04516", "1.18.0--r41hdfd78af_0": "sha256:77bbb138ba8891dd7e45e4838d3437432baf950a3379eb8132acc1f2e298c92f", "1.16.0--r40hdfd78af_1": "sha256:02e861b74d6bf2a8f2ba2b0979964fb58d96785e9fa2315e9cba01f4bec5c864", "1.14.0--r40_0": "sha256:f6f8944536b1e927386d423c3b2f2a99a3da413dca75414f4db7066cb0928f48", "1.26.0--r43hdfd78af_0": "sha256:2372c280772a5687c03170665637aa68db15e4af98c04dd001ce4bd3e8574a40", "1.28.0--r43hdfd78af_0": "sha256:f294897f3d4c28ed7643c63c63daeb2090f26bb9fdec0ddee486419dd8c8ab52"}, "docker": "quay.io/biocontainers/bioconductor-helloranges", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-helloranges.
shpc-registry automated BioContainers addition for bioconductor-helloranges
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-helloranges
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-helloranges:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-helloranges/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-helloranges/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-helloranges-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-helloranges-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-helloranges-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-helloranges-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-helloranges-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-helloranges-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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