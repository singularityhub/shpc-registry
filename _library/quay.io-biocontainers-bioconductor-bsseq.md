---
layout: container
name:  "quay.io/biocontainers/bioconductor-bsseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bsseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bsseq/container.yaml"
updated_at: "2024-03-04 05:06:22.027482"
latest: "1.38.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bsseq"

versions:
 - "1.30.0--r41hc247a5b_2"
 - "1.34.0--r42hc247a5b_0"
 - "1.34.0--r42hf17093f_1"
 - "1.36.0--r43hf17093f_0"
 - "1.38.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bsseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bsseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bsseq", "latest": {"1.38.0--r43hf17093f_0": "sha256:a4d5bc7461caf1ccb6472d3560d92d07f55d252cc34d2015de9d77bd4229f4b2"}, "tags": {"1.30.0--r41hc247a5b_2": "sha256:0aaef682fbbd002a38cacaa6efca9e4e4c1daaa23508b2888fdd942a120dbf7a", "1.34.0--r42hc247a5b_0": "sha256:2147adfd6e3964c317607e5ec521e1f55c8d2c273602e5d87cd073f83031cfc6", "1.34.0--r42hf17093f_1": "sha256:555d81f47378a62c9e678c99b83eb14d4b54b2fca6f8462a0eb6d2fa7c9c3905", "1.36.0--r43hf17093f_0": "sha256:0df9299bf199c4b4c04e382eb7388dec06e2a762a486de5f0537a9a64309ed6a", "1.38.0--r43hf17093f_0": "sha256:a4d5bc7461caf1ccb6472d3560d92d07f55d252cc34d2015de9d77bd4229f4b2"}, "docker": "quay.io/biocontainers/bioconductor-bsseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bsseq.
shpc-registry automated BioContainers addition for bioconductor-bsseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bsseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bsseq:1.38.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bsseq/1.38.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-bsseq/1.38.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bsseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bsseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bsseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bsseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bsseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bsseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-bsseq

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