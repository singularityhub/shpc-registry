---
layout: container
name:  "quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18/container.yaml"
updated_at: "2023-07-29 03:27:51.781391"
latest: "0.0.2--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-huexexonprobesetlocationhg18"

versions:
 - "0.0.2--r41hdfd78af_9"
 - "0.0.2--r42hdfd78af_10"
 - "0.0.2--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocationhg18"
config: {"url": "https://biocontainers.pro/tools/bioconductor-huexexonprobesetlocationhg18", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocationhg18", "latest": {"0.0.2--r43hdfd78af_11": "sha256:73813912eab1dfdb17d8860287d4c9d8e950485ffc0afb3dac6eee7e9fda6ab9"}, "tags": {"0.0.2--r41hdfd78af_9": "sha256:1b001aa29b3d5d3dac6896078a1e07879c7014945938c6d71e96176445d2f1b6", "0.0.2--r42hdfd78af_10": "sha256:fd22f869d15039b434f5b2e284de6bcc98a963a9aa5e0a4b3df0780c737cb4e9", "0.0.2--r43hdfd78af_11": "sha256:73813912eab1dfdb17d8860287d4c9d8e950485ffc0afb3dac6eee7e9fda6ab9"}, "docker": "quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18.
shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocationhg18
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18:0.0.2--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18/0.0.2--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg18/0.0.2--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-huexexonprobesetlocationhg18-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huexexonprobesetlocationhg18-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huexexonprobesetlocationhg18-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-huexexonprobesetlocationhg18-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-huexexonprobesetlocationhg18-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-huexexonprobesetlocationhg18-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-huexexonprobesetlocationhg18

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