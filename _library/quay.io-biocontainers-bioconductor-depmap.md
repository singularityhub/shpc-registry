---
layout: container
name:  "quay.io/biocontainers/bioconductor-depmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-depmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-depmap/container.yaml"
updated_at: "2025-12-21 04:32:35.165468"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-depmap"

versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.12.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-depmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-depmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-depmap", "latest": {"1.20.0--r44hdfd78af_0": "sha256:828565b8e3f7e821360d854b4367d13cfe4da5c211d3fdc8fb456b2bf1e3bd9b"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:7b9535db882b1f71e486e06c0af358553094bfbef3f6f971facefd7cf11a7330", "1.12.0--r42hdfd78af_0": "sha256:ec33d06075320fb68ce63527acbe139bb3179d99b8b8caeb9ce3a3c8da52660b", "1.14.0--r43hdfd78af_0": "sha256:3c11fbce209d3cd1f2f893ff56dc578b68d8fde4c9151f5c5fb9e79f5a0b6d5b", "1.16.0--r43hdfd78af_0": "sha256:652b0a2a08d609a4d275d7817c751dbdae6e01b2af4b249b673767bfdc480f15", "1.20.0--r44hdfd78af_0": "sha256:828565b8e3f7e821360d854b4367d13cfe4da5c211d3fdc8fb456b2bf1e3bd9b"}, "docker": "quay.io/biocontainers/bioconductor-depmap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-depmap.
shpc-registry automated BioContainers addition for bioconductor-depmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-depmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-depmap:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-depmap/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-depmap/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-depmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-depmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-depmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-depmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-depmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-depmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-depmap

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