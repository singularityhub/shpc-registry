---
layout: container
name:  "quay.io/biocontainers/bioconductor-branchpointer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-branchpointer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-branchpointer/container.yaml"
updated_at: "2023-11-29 02:51:09.080759"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-branchpointer"
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
description: "shpc-registry automated BioContainers addition for bioconductor-branchpointer"
config: {"url": "https://biocontainers.pro/tools/bioconductor-branchpointer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-branchpointer", "latest": {"1.26.0--r43hdfd78af_0": "sha256:7556ce5fd2651743ee7037c3fcf66c6db44a83adac6c31bc4e72d6b12de53975"}, "tags": {"1.8.0--r351_0": "sha256:44a0bd4c349c2b752b6ee08b1b8fd93da8dbd9019bc555634757a305f271d2fc", "1.24.0--r42hdfd78af_0": "sha256:025b01459a99d873e81c40e7b03df3702ca185183264e91ae88e7c7450896e8d", "1.20.0--r41hdfd78af_0": "sha256:21849d2c9a177576c1d181acb413e40c7c215e6550c2cfc086b8bbd05ddf9629", "1.18.0--r41hdfd78af_0": "sha256:ec4b5e39fe253b513c3cebc5675d69defa459b4aad91e541ce19ce0e9c34b66d", "1.16.0--r40hdfd78af_1": "sha256:d0dbeab8bfb67f09b30fb2ad7b5c57982b774bddfd8689841ea6517816333444", "1.14.0--r40_0": "sha256:aed629920cf27b29d24629f1ebb92f8610ef71704d3a58bd5bebf14ed0be2eb8", "1.26.0--r43hdfd78af_0": "sha256:7556ce5fd2651743ee7037c3fcf66c6db44a83adac6c31bc4e72d6b12de53975"}, "docker": "quay.io/biocontainers/bioconductor-branchpointer", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-branchpointer.
shpc-registry automated BioContainers addition for bioconductor-branchpointer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-branchpointer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-branchpointer:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-branchpointer/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-branchpointer/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-branchpointer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-branchpointer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-branchpointer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-branchpointer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-branchpointer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-branchpointer-inspect-deffile:

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