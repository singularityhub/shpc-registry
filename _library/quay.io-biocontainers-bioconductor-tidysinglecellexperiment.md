---
layout: container
name:  "quay.io/biocontainers/bioconductor-tidysinglecellexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tidysinglecellexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tidysinglecellexperiment/container.yaml"
updated_at: "2024-05-24 02:39:08.394370"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tidysinglecellexperiment"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tidysinglecellexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tidysinglecellexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tidysinglecellexperiment", "latest": {"1.12.0--r43hdfd78af_0": "sha256:52074eb0b994b0b5daf658a894b51c41787baf1876f44edcaf924d3ba5951803"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:675a74d04c5c911789d978c5dc2c6a132290e862b772930f5d32854902953f80", "1.8.0--r42hdfd78af_0": "sha256:85417eb67f879b3eddeb34605a8a3bcd1f1fdc0edc607fb48a2b48e0cd6bd6f5", "1.10.0--r43hdfd78af_0": "sha256:fee4e28dfdd5d9777ce12c7573fa1b27cecf919f89c10c058c2fbc8794e14b23", "1.12.0--r43hdfd78af_0": "sha256:52074eb0b994b0b5daf658a894b51c41787baf1876f44edcaf924d3ba5951803"}, "docker": "quay.io/biocontainers/bioconductor-tidysinglecellexperiment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tidysinglecellexperiment.
shpc-registry automated BioContainers addition for bioconductor-tidysinglecellexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tidysinglecellexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tidysinglecellexperiment:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tidysinglecellexperiment/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tidysinglecellexperiment/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tidysinglecellexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidysinglecellexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidysinglecellexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tidysinglecellexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tidysinglecellexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tidysinglecellexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tidysinglecellexperiment

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