---
layout: container
name:  "quay.io/biocontainers/bioconductor-huexexonprobesetlocation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-huexexonprobesetlocation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-huexexonprobesetlocation/container.yaml"
updated_at: "2023-02-27 03:30:32.018036"
latest: "1.15.0--r42hdfd78af_10"
container_url: "https://biocontainers.pro/tools/bioconductor-huexexonprobesetlocation"

versions:
 - "1.15.0--r41hdfd78af_9"
 - "1.15.0--r42hdfd78af_10"
description: "shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-huexexonprobesetlocation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocation", "latest": {"1.15.0--r42hdfd78af_10": "sha256:a6473c973419147351e76179d482c363318f3c04aa2fca0c445f3a7abdb806ed"}, "tags": {"1.15.0--r41hdfd78af_9": "sha256:6cca1c46908581d1a4d4d68b83bcd5b0be1ae2045cea9529163fd45c5946e2f3", "1.15.0--r42hdfd78af_10": "sha256:a6473c973419147351e76179d482c363318f3c04aa2fca0c445f3a7abdb806ed"}, "docker": "quay.io/biocontainers/bioconductor-huexexonprobesetlocation"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-huexexonprobesetlocation.
shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-huexexonprobesetlocation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-huexexonprobesetlocation:1.15.0--r42hdfd78af_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-huexexonprobesetlocation/1.15.0--r42hdfd78af_10
$ module help quay.io/biocontainers/bioconductor-huexexonprobesetlocation/1.15.0--r42hdfd78af_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-huexexonprobesetlocation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huexexonprobesetlocation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huexexonprobesetlocation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-huexexonprobesetlocation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-huexexonprobesetlocation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-huexexonprobesetlocation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-huexexonprobesetlocation

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