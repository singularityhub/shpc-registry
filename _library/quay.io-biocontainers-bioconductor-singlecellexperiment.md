---
layout: container
name:  "quay.io/biocontainers/bioconductor-singlecellexperiment"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-singlecellexperiment/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-singlecellexperiment/container.yaml"
updated_at: "2023-10-21 03:08:03.396489"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-singlecellexperiment"

versions:
 - "1.8.0--r36_0"
 - "1.20.0--r42hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.1--r41hdfd78af_0"
 - "1.12.0--r40hdfd78af_1"
 - "1.10.1--r40_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-singlecellexperiment"
config: {"url": "https://biocontainers.pro/tools/bioconductor-singlecellexperiment", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-singlecellexperiment", "latest": {"1.22.0--r43hdfd78af_0": "sha256:21dcb3f25d0511b031e4c5053c0d61264ad0ad07e7f0d5f372339060e5e926cc"}, "tags": {"1.8.0--r36_0": "sha256:169679d7a8ee83f8e832d6a8b1b63124bf09f7c22f1b8b10846d67d0513a2bfc", "1.20.0--r42hdfd78af_0": "sha256:4a57f49434d290a3370ff3781f3db1c28b1480205f47a0345fab7a356adf4b58", "1.16.0--r41hdfd78af_0": "sha256:947c24032ebcc692d05d6f82df25d2228b843be89c689b2cf148e0df2474ebfc", "1.14.1--r41hdfd78af_0": "sha256:95c3b0bc29fd4ccbf80ca7f92fc2336815bf1df9bc95e1d67a337610066647b7", "1.12.0--r40hdfd78af_1": "sha256:472de84e45fe585ebd41c7a00fef940d2c6a09a0e99db20166e6ded652e1ac68", "1.10.1--r40_0": "sha256:8e1a5d9f82034b7d9bb06ccff059010fd7ea2d3b1afbb101acab33e8b50ccb1a", "1.22.0--r43hdfd78af_0": "sha256:21dcb3f25d0511b031e4c5053c0d61264ad0ad07e7f0d5f372339060e5e926cc"}, "docker": "quay.io/biocontainers/bioconductor-singlecellexperiment"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-singlecellexperiment.
shpc-registry automated BioContainers addition for bioconductor-singlecellexperiment
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecellexperiment
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-singlecellexperiment:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-singlecellexperiment/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-singlecellexperiment/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-singlecellexperiment-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecellexperiment-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-singlecellexperiment-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-singlecellexperiment-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-singlecellexperiment-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-singlecellexperiment-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-singlecellexperiment

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