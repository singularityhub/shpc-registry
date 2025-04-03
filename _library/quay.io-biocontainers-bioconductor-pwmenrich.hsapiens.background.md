---
layout: container
name:  "quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background/container.yaml"
updated_at: "2025-04-03 03:20:13.595355"
latest: "4.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pwmenrich.hsapiens.background"

versions:
 - "4.28.0--r41hdfd78af_1"
 - "4.32.0--r42hdfd78af_0"
 - "4.34.0--r43hdfd78af_0"
 - "4.36.0--r43hdfd78af_0"
 - "4.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pwmenrich.hsapiens.background"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pwmenrich.hsapiens.background", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pwmenrich.hsapiens.background", "latest": {"4.40.0--r44hdfd78af_0": "sha256:e9de95c5a57397a3b971fc48bb0f7e635c8873fe20a049c1ed9bdb15e7180e01"}, "tags": {"4.28.0--r41hdfd78af_1": "sha256:97341cafd2a70fc45c51c7e3329499f887e53efee306e1fde9a1057176169637", "4.32.0--r42hdfd78af_0": "sha256:64b4cdef6d6684f96a01c5ac276a6bd23c719ca5c465360dc29c4ea8eace6467", "4.34.0--r43hdfd78af_0": "sha256:8702b3e942cb9645923142bd737604fac281ef142ee00df7762206e5dca4c6e7", "4.36.0--r43hdfd78af_0": "sha256:52c1298716c55e2b7de51bf26035ff85aa12063708edeec5c92f0438f3ba8d4d", "4.40.0--r44hdfd78af_0": "sha256:e9de95c5a57397a3b971fc48bb0f7e635c8873fe20a049c1ed9bdb15e7180e01"}, "docker": "quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background.
shpc-registry automated BioContainers addition for bioconductor-pwmenrich.hsapiens.background
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background:4.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background/4.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pwmenrich.hsapiens.background/4.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pwmenrich.hsapiens.background-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwmenrich.hsapiens.background-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwmenrich.hsapiens.background-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pwmenrich.hsapiens.background-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pwmenrich.hsapiens.background-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pwmenrich.hsapiens.background-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pwmenrich.hsapiens.background

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