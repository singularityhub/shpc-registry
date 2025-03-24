---
layout: container
name:  "quay.io/biocontainers/bioconductor-seq2pathway.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seq2pathway.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seq2pathway.data/container.yaml"
updated_at: "2025-03-24 03:42:33.978070"
latest: "1.38.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seq2pathway.data"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.30.0--r42hdfd78af_1"
 - "1.29.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.38.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seq2pathway.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seq2pathway.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seq2pathway.data", "latest": {"1.38.0--r44hdfd78af_0": "sha256:b32f854d7f3ee6228482dc79f1a19d3e08debe4d4679e1f72de2a8828c12f187"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:ecfb7940f8bc1e5e50e0b37d5e920ff0f3d303ec0d62bf3f8c8540502b0464a1", "1.30.0--r42hdfd78af_1": "sha256:104a2c694832ab3125dbac174c35983932c671005491d2c0178136df6a7188d7", "1.29.0--r42hdfd78af_0": "sha256:396fa1e4bb878b8dcde23b059ae7d3ed03750bed6d0b9fed04f25b513dd61f7f", "1.32.0--r43hdfd78af_0": "sha256:3a5322b7e8303c84972fbcfdb145ce622b8a0e74292815de323f111f64901419", "1.34.0--r43hdfd78af_0": "sha256:ef742a7566ecc1df4c44b68784c55eb59dc1f94626b4bf2c61bd649cda34c0f0", "1.38.0--r44hdfd78af_0": "sha256:b32f854d7f3ee6228482dc79f1a19d3e08debe4d4679e1f72de2a8828c12f187"}, "docker": "quay.io/biocontainers/bioconductor-seq2pathway.data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seq2pathway.data.
shpc-registry automated BioContainers addition for bioconductor-seq2pathway.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seq2pathway.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seq2pathway.data:1.38.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seq2pathway.data/1.38.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seq2pathway.data/1.38.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seq2pathway.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seq2pathway.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seq2pathway.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seq2pathway.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seq2pathway.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seq2pathway.data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seq2pathway.data

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