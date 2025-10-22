---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgu34bcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgu34bcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgu34bcdf/container.yaml"
updated_at: "2025-10-22 03:33:52.860614"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-rgu34bcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-rgu34bcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgu34bcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgu34bcdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:028e58cd07c8121a1e740231c9dd139b4020d37526bd2329e438c042fb9507bf"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:53d14a560d7622ef9c9b86c38e76b2a4d52e1db1e77af13e323b00af955091ca", "2.18.0--r42hdfd78af_10": "sha256:27b6c824a0eea5955a097647e8196a96ddc03a99862541a0a968d788a193eae2", "2.18.0--r43hdfd78af_11": "sha256:5f6d79cbd2e6a4bbcfb1ac88ec076eba40b38b130d279fb6cd2dd7eeb8d9587e", "2.18.0--r43hdfd78af_12": "sha256:ebe7a9d5200f2b1b02ea039e98cb4e344bc6a5adf11f2e1c61a9d992ab794e50", "2.18.0--r44hdfd78af_13": "sha256:028e58cd07c8121a1e740231c9dd139b4020d37526bd2329e438c042fb9507bf"}, "docker": "quay.io/biocontainers/bioconductor-rgu34bcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgu34bcdf.
shpc-registry automated BioContainers addition for bioconductor-rgu34bcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34bcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34bcdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgu34bcdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-rgu34bcdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgu34bcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34bcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34bcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgu34bcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgu34bcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgu34bcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgu34bcdf

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