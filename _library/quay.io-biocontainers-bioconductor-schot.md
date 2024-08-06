---
layout: container
name:  "quay.io/biocontainers/bioconductor-schot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-schot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-schot/container.yaml"
updated_at: "2024-08-06 03:14:17.054800"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-schot"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-schot"
config: {"url": "https://biocontainers.pro/tools/bioconductor-schot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-schot", "latest": {"1.14.0--r43hdfd78af_0": "sha256:9694259048336d42a752630e45a2065d73eec781de2ea9125a7e2d7e572f375f"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:7cc91888307f64078ee6e3bc48ed3c65e682ac2d8edf0e4addf0b0c663bab6ca", "1.10.0--r42hdfd78af_0": "sha256:c710dc7910f8afa67d074d6edf6dcc27a1d961357252e7dd629563f652e1c8ad", "1.12.0--r43hdfd78af_0": "sha256:404d1ce14ca64ae1fb7f55c0a72629e764bcc48bcd08e96534fa7006d3f88e68", "1.14.0--r43hdfd78af_0": "sha256:9694259048336d42a752630e45a2065d73eec781de2ea9125a7e2d7e572f375f"}, "docker": "quay.io/biocontainers/bioconductor-schot"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-schot.
shpc-registry automated BioContainers addition for bioconductor-schot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-schot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-schot:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-schot/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-schot/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-schot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-schot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-schot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-schot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-schot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-schot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-schot

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