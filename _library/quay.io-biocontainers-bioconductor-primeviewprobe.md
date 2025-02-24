---
layout: container
name:  "quay.io/biocontainers/bioconductor-primeviewprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-primeviewprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-primeviewprobe/container.yaml"
updated_at: "2025-02-24 03:08:21.455740"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-primeviewprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-primeviewprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-primeviewprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-primeviewprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:fae9d2ae7438b32d344a24213e6779b4a441c9f348b0114f8009a6e4b7ddb02e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:14ceacc8c5f2bd82d11de6d1457ab9075255863eb1cfdd452fc0021c960996df", "2.18.0--r42hdfd78af_10": "sha256:d6830c721d1fc7b20da5b8f7a81c939726dc38673924b590386d43f262d298ce", "2.18.0--r43hdfd78af_11": "sha256:6e77bf1a0c127f5867079b6980dbced3aaa7d027a6b32fc0a53d445a30069e5c", "2.18.0--r43hdfd78af_12": "sha256:ae5e7a4e2af2e361f0b3a602005a64eb8620817ad81bd6a64e145bf024428b42", "2.18.0--r44hdfd78af_13": "sha256:fae9d2ae7438b32d344a24213e6779b4a441c9f348b0114f8009a6e4b7ddb02e"}, "docker": "quay.io/biocontainers/bioconductor-primeviewprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-primeviewprobe.
shpc-registry automated BioContainers addition for bioconductor-primeviewprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-primeviewprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-primeviewprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-primeviewprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-primeviewprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-primeviewprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-primeviewprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-primeviewprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-primeviewprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-primeviewprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-primeviewprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-primeviewprobe

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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