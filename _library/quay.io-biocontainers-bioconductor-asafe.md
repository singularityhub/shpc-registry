---
layout: container
name:  "quay.io/biocontainers/bioconductor-asafe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-asafe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-asafe/container.yaml"
updated_at: "2024-02-20 02:48:06.956650"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-asafe"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-asafe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-asafe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-asafe", "latest": {"1.28.0--r43hdfd78af_0": "sha256:4b61550e5d85c881e83bb129fe8d7e981b1ac46f279fdd25bb1bf94eafe4706b"}, "tags": {"1.8.0--r351_0": "sha256:6ddcc4f3440ad493c34dcc446070e8f83bccd4f1629f06b2c67cbb268c137fb0", "1.20.0--r41hdfd78af_0": "sha256:096117497eb78163eb4b30cbc2c2d5499ab9d072f3a4072e15a79dd0e9079b59", "1.18.0--r41hdfd78af_0": "sha256:84e1a4c966096ede44aaef9373af1621af5c4423276b7bd6de783389c6084e56", "1.16.0--r40hdfd78af_1": "sha256:d417e5d12c7ded7e2ee2e442fc615f1807984a824314a2cd8a21bfa04a49b194", "1.14.0--r40_0": "sha256:ef2adbebd5bb5ed422e48c40fdb065ebd0291332b74e795e9e0477cf12997183", "1.12.0--r36_0": "sha256:add49e53c2a43bf6be4e3533b0691382e7c974647a6f50a74849e493582b7ea0", "1.24.0--r42hdfd78af_0": "sha256:47651501db411a272571cd45563b7dd2c0af9367d6d36cea843ac5fd66cc807e", "1.26.0--r43hdfd78af_0": "sha256:a41823f14cf7bda4586ad6457d878ce0ed44394fe7c8ce9f5d8fba233c81b726", "1.28.0--r43hdfd78af_0": "sha256:4b61550e5d85c881e83bb129fe8d7e981b1ac46f279fdd25bb1bf94eafe4706b"}, "docker": "quay.io/biocontainers/bioconductor-asafe", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-asafe.
shpc-registry automated BioContainers addition for bioconductor-asafe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-asafe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-asafe:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-asafe/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-asafe/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-asafe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-asafe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-asafe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-asafe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-asafe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-asafe-inspect-deffile:

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