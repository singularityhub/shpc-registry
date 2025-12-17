---
layout: container
name:  "quay.io/biocontainers/bioconductor-qfeatures"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-qfeatures/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-qfeatures/container.yaml"
updated_at: "2025-12-17 04:08:23.777485"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-qfeatures"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-qfeatures"
config: {"url": "https://biocontainers.pro/tools/bioconductor-qfeatures", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-qfeatures", "latest": {"1.16.0--r44hdfd78af_0": "sha256:6fd99b9d291efe6f4f7d416fddec41ae73659a9a408bb64b1d6b19934fb05d5a"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:2d3f121be603cb463dbf0adf58e93ead4a1e617147c2d0edca36b21d0613db58", "1.8.0--r42hdfd78af_0": "sha256:4218c6050ab0673195e9abc08f7a884e6d059512ac513972550a719c7dc8a5db", "1.10.0--r43hdfd78af_0": "sha256:fdd94f4914c2aeba95262f7795f7d4c771debbe9eb706a30e90e75194d90ae78", "1.12.0--r43hdfd78af_0": "sha256:d74f2bc5a3d98aaf62dad3c7fce5b29e791a52e732f594b36166c2649b93c197", "1.16.0--r44hdfd78af_0": "sha256:6fd99b9d291efe6f4f7d416fddec41ae73659a9a408bb64b1d6b19934fb05d5a"}, "docker": "quay.io/biocontainers/bioconductor-qfeatures"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-qfeatures.
shpc-registry automated BioContainers addition for bioconductor-qfeatures
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-qfeatures
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-qfeatures:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-qfeatures/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-qfeatures/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-qfeatures-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qfeatures-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-qfeatures-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-qfeatures-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-qfeatures-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-qfeatures-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-qfeatures

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