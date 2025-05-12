---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu133aprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu133aprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu133aprobe/container.yaml"
updated_at: "2025-05-12 03:50:28.667997"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu133aprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu133aprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu133aprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu133aprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:1b4fad181acfcb51ceae61b69e28170bc6d9928261258d83c0e41d6c53aca924"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:99c1fabb41396337f629a8eb99534b57d34c1312c5ea09762781abaa5bb16dbd", "2.18.0--r42hdfd78af_10": "sha256:0005ecb7fa7d716fad8bf243e338c80b8676ce7c1f69581adc82e3e3485a4157", "2.18.0--r43hdfd78af_11": "sha256:2e9c306936e7462a8e0f31e13ff011b99c78519355c74329d54101f2ecde16d0", "2.18.0--r43hdfd78af_12": "sha256:307b540c6e955b3dd8df6f84f326455feb2f276a90f4886e4e636b0a98a0deae", "2.18.0--r44hdfd78af_13": "sha256:1b4fad181acfcb51ceae61b69e28170bc6d9928261258d83c0e41d6c53aca924"}, "docker": "quay.io/biocontainers/bioconductor-hgu133aprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu133aprobe.
shpc-registry automated BioContainers addition for bioconductor-hgu133aprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133aprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu133aprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu133aprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu133aprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu133aprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133aprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu133aprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu133aprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu133aprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu133aprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu133aprobe

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