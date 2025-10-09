---
layout: container
name:  "quay.io/biocontainers/bioconductor-degseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-degseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-degseq/container.yaml"
updated_at: "2025-10-09 03:30:33.696510"
latest: "1.60.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-degseq"

versions:
 - "1.48.0--r41hc247a5b_2"
 - "1.52.0--r42hc247a5b_0"
 - "1.52.0--r42hf17093f_1"
 - "1.54.0--r43hf17093f_0"
 - "1.56.1--r43hf17093f_0"
 - "1.56.1--r43hf17093f_1"
 - "1.60.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-degseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-degseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-degseq", "latest": {"1.60.0--r44he5774e6_0": "sha256:3743daa50a80b5edab73799c685a5c4576e4e7d12ff65a454e9b8260ebf1b8c9"}, "tags": {"1.48.0--r41hc247a5b_2": "sha256:79452c545f45628ff758b7d0ec07c8179defdf991e9b87bdd2498f2ef81606a5", "1.52.0--r42hc247a5b_0": "sha256:f82812edf6a0a437934d16ce1bcf486c043892bfde606d7d828ea7021eaadfcc", "1.52.0--r42hf17093f_1": "sha256:d1f795f72e82d5d372469e3c51b46f63771231b500060925c3299fad0b38064c", "1.54.0--r43hf17093f_0": "sha256:4f85871545f0085ed4b7df4c5706a3b035790243ab2e2420bd3b7f42e69f88d8", "1.56.1--r43hf17093f_0": "sha256:9c502fc394d32ab90e47fd4d5d2b28fbde3540fc485a2e922c6e95a5779ed5c0", "1.56.1--r43hf17093f_1": "sha256:1faacd1c5c65aea613df8db2ff5a04a45580da2d787c9062b9466505866d8c25", "1.60.0--r44he5774e6_0": "sha256:3743daa50a80b5edab73799c685a5c4576e4e7d12ff65a454e9b8260ebf1b8c9"}, "docker": "quay.io/biocontainers/bioconductor-degseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-degseq.
shpc-registry automated BioContainers addition for bioconductor-degseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-degseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-degseq:1.60.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-degseq/1.60.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-degseq/1.60.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-degseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-degseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-degseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-degseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-degseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-degseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-degseq

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