---
layout: container
name:  "quay.io/biocontainers/bioconductor-scater"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scater/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scater/container.yaml"
updated_at: "2024-05-29 03:10:06.857133"
latest: "1.30.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scater"

versions:
 - "1.8.4--r351hfc679d8_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.6--r40hdfd78af_0"
 - "1.16.0--r40h5f743cb_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scater"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scater", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scater", "latest": {"1.30.1--r43hdfd78af_0": "sha256:5b92c8632959b9529caffaf190f9cf9719327321c7dfa76909bd428913b7618e"}, "tags": {"1.8.4--r351hfc679d8_0": "sha256:d8c02a5a0b6fef5664549dff8a26b082ee540dfde8dd83b8a8522bc0f49e44a8", "1.26.0--r42hdfd78af_0": "sha256:91f8a14ab7af989df42f98e4aea24ebf47730ec2673308ae61eb02c41bcfa657", "1.22.0--r41hdfd78af_0": "sha256:fd913e404005e256c542137f65e8968af4c2434ed18a960cc4320be69eef47d8", "1.20.0--r41hdfd78af_0": "sha256:76158d870acc7991ff05b0bbfc98e545c5a30310ea47e050cbb12879089724a7", "1.18.6--r40hdfd78af_0": "sha256:04c50f04942fa0503241458be649f6f0babd346991c1dac777e569576bbbc61b", "1.16.0--r40h5f743cb_0": "sha256:de9116ddfadf0823a1ac3e0003310041cdf235ffdce05ed84a4286c64634ba99", "1.28.0--r43hdfd78af_0": "sha256:3912883643a6689bd78281abf19d9de00ae5e9d5726700c135d6c9facdf58376", "1.30.1--r43hdfd78af_0": "sha256:5b92c8632959b9529caffaf190f9cf9719327321c7dfa76909bd428913b7618e"}, "docker": "quay.io/biocontainers/bioconductor-scater"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scater.
shpc-registry automated BioContainers addition for bioconductor-scater
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scater
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scater:1.30.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scater/1.30.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scater/1.30.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scater-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scater-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scater-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scater-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scater-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scater-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scater

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