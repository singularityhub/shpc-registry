---
layout: container
name:  "quay.io/biocontainers/bioconductor-pigengene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pigengene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pigengene/container.yaml"
updated_at: "2025-10-13 04:28:56.701099"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pigengene"
aliases:
 - "wget"
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
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pigengene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pigengene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pigengene", "latest": {"1.32.0--r44hdfd78af_0": "sha256:2f83db8b127f9b155f43a3b5dc169bf1db8308c6b04d9fcc7eb19585db2bf598"}, "tags": {"1.8.0--r351_0": "sha256:d22abb6b3c4015c0e94b8fbd04504a99accba53929d937bd61dde783bb9f897a", "1.20.0--r41hdfd78af_0": "sha256:2d09c4dee61e5a2969156f1e19b146ea0d67fd7dd1262be7e41f399f5f3d0651", "1.18.0--r41hdfd78af_0": "sha256:86544143656fb4492ebeb2aa11ea4c3fe9b7b7a6dfc79bc73ec8bbbd9e996a96", "1.16.0--r40hdfd78af_1": "sha256:f43fce393d32bf357942f954f3f8a710fcfa4946cf5e1bbef7b7242af333df62", "1.14.0--r40_0": "sha256:8b122d64b35e28a9def42af636a4896a54b6224a5bbda3d635014ca057e18876", "1.12.0--r36_0": "sha256:8398e3c21111de760330f1bdcfb2447e16b05c9287d40d56eda599cc5d61c5a2", "1.24.0--r42hdfd78af_0": "sha256:61dfa9578ad1a1b055b13e59937c0587fad5fa7bd67ac4833f85e444d5668f55", "1.26.0--r43hdfd78af_0": "sha256:bf96010d73c92420936f600249827f89cdfc16d24c338a7cb84edf8c06469d4c", "1.28.0--r43hdfd78af_0": "sha256:2153234c9d4797c318010c6c51c464a066e296b3e4a8962a7a14011ae3285e0c", "1.32.0--r44hdfd78af_0": "sha256:2f83db8b127f9b155f43a3b5dc169bf1db8308c6b04d9fcc7eb19585db2bf598"}, "docker": "quay.io/biocontainers/bioconductor-pigengene", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pigengene.
shpc-registry automated BioContainers addition for bioconductor-pigengene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pigengene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pigengene:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pigengene/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pigengene/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pigengene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pigengene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pigengene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pigengene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pigengene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pigengene-inspect-deffile:

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