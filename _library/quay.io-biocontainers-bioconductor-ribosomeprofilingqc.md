---
layout: container
name:  "quay.io/biocontainers/bioconductor-ribosomeprofilingqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ribosomeprofilingqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ribosomeprofilingqc/container.yaml"
updated_at: "2025-11-06 03:56:03.265298"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ribosomeprofilingqc"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ribosomeprofilingqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ribosomeprofilingqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ribosomeprofilingqc", "latest": {"1.18.0--r44hdfd78af_0": "sha256:de7b607530521df4ccadaa53cf62f59f55798f0f9e7c88b88705cca9093069a8"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:cb0671d16ad850719da2abcc8defba05a7c4ba1bb958c91f061fd19e98e9191f", "1.10.0--r42hdfd78af_0": "sha256:db76a5c5983293ea2db5f300fce09b977e288394861b8ff2bc3bc2674cd92253", "1.12.0--r43hdfd78af_0": "sha256:671411cc593668b075dda83cfaf73f1afe7bf7df0563b75fb4a77cf899063806", "1.14.0--r43hdfd78af_0": "sha256:6ebab3d74ac60ce15bbfb29e39db664272b9a091f4522c8d105afd3987121166", "1.18.0--r44hdfd78af_0": "sha256:de7b607530521df4ccadaa53cf62f59f55798f0f9e7c88b88705cca9093069a8"}, "docker": "quay.io/biocontainers/bioconductor-ribosomeprofilingqc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ribosomeprofilingqc.
shpc-registry automated BioContainers addition for bioconductor-ribosomeprofilingqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ribosomeprofilingqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ribosomeprofilingqc:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ribosomeprofilingqc/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ribosomeprofilingqc/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ribosomeprofilingqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ribosomeprofilingqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ribosomeprofilingqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ribosomeprofilingqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ribosomeprofilingqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ribosomeprofilingqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ribosomeprofilingqc

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