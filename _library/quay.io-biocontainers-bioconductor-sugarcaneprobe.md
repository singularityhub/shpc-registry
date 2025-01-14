---
layout: container
name:  "quay.io/biocontainers/bioconductor-sugarcaneprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sugarcaneprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sugarcaneprobe/container.yaml"
updated_at: "2025-01-14 02:45:22.744525"
latest: "2.18.0--r43hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-sugarcaneprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r43hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-sugarcaneprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sugarcaneprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sugarcaneprobe", "latest": {"2.18.0--r43hdfd78af_13": "sha256:a008b1d5360622ed44fc832d30e98c22befd3ff88194fe425a866dceb1d2a0e5"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:53f28be5637da45715f7653550687debb1df806a6a5481b9471d398dbb372abd", "2.18.0--r42hdfd78af_11": "sha256:a6a09b2ed21c529cd3e833871e71d319d6ac7d59e4ca869d7ef7e58d7ce294f3", "2.18.0--r43hdfd78af_12": "sha256:86599a8d56544d81cee0af39d247bc80fcc9dfb2ed985641abac0a78227f7caa", "2.18.0--r43hdfd78af_13": "sha256:a008b1d5360622ed44fc832d30e98c22befd3ff88194fe425a866dceb1d2a0e5"}, "docker": "quay.io/biocontainers/bioconductor-sugarcaneprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sugarcaneprobe.
shpc-registry automated BioContainers addition for bioconductor-sugarcaneprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sugarcaneprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sugarcaneprobe:2.18.0--r43hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sugarcaneprobe/2.18.0--r43hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-sugarcaneprobe/2.18.0--r43hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sugarcaneprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sugarcaneprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sugarcaneprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sugarcaneprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sugarcaneprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sugarcaneprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sugarcaneprobe

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