---
layout: container
name:  "quay.io/biocontainers/bioconductor-sugarcanecdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sugarcanecdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sugarcanecdf/container.yaml"
updated_at: "2025-09-15 03:11:06.953518"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-sugarcanecdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-sugarcanecdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sugarcanecdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sugarcanecdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:632fb0e6b112f97b947e6ddd1ee47673f179ebe6f32580c04fba373f3fae2177"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:0225248830c508d08be12db0ee7b7f6d14f72c65be3cc6579a8b7ee9878f4e18", "2.18.0--r42hdfd78af_10": "sha256:b8ae649d244269cd281ffabb2ce08aa595577d202183e56279bdf806096d40cb", "2.18.0--r43hdfd78af_11": "sha256:9aa00b6bd9b6c5d386a9626846abfd352ecdd0251d00f053c959bd6189707023", "2.18.0--r43hdfd78af_12": "sha256:ef22454b747ed36d40388fd0cf52d9137a1532bcfd53f4cb3807d5965b904d0b", "2.18.0--r44hdfd78af_13": "sha256:632fb0e6b112f97b947e6ddd1ee47673f179ebe6f32580c04fba373f3fae2177"}, "docker": "quay.io/biocontainers/bioconductor-sugarcanecdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sugarcanecdf.
shpc-registry automated BioContainers addition for bioconductor-sugarcanecdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sugarcanecdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sugarcanecdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sugarcanecdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-sugarcanecdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sugarcanecdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sugarcanecdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sugarcanecdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sugarcanecdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sugarcanecdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sugarcanecdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sugarcanecdf

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