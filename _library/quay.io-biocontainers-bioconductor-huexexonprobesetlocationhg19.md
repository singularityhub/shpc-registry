---
layout: container
name:  "quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19/container.yaml"
updated_at: "2026-01-01 07:08:48.919147"
latest: "0.0.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-huexexonprobesetlocationhg19"

versions:
 - "0.0.3--r41hdfd78af_9"
 - "0.0.3--r42hdfd78af_10"
 - "0.0.3--r43hdfd78af_11"
 - "0.0.3--r43hdfd78af_12"
 - "0.0.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocationhg19"
config: {"url": "https://biocontainers.pro/tools/bioconductor-huexexonprobesetlocationhg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocationhg19", "latest": {"0.0.3--r44hdfd78af_13": "sha256:75f1e6a0ee0869695d4de1a2eb237778896384d7baae2409804bc3fe36343435"}, "tags": {"0.0.3--r41hdfd78af_9": "sha256:641465091828550b682ec971a6475026fae67bfde330a217fdd91dc528633ed6", "0.0.3--r42hdfd78af_10": "sha256:4667de47c95c05ca7306cf671b9e2791672d195d159e9e85303865c07eb022ba", "0.0.3--r43hdfd78af_11": "sha256:981e537ac85e900d320c1b68cc57b3e5e75292a971b34ed9abd358deb5b60c31", "0.0.3--r43hdfd78af_12": "sha256:fcf735b39e230d41da8290072fabc58c3e9bdd50ef7ac27002f1e6c0629ee68b", "0.0.3--r44hdfd78af_13": "sha256:75f1e6a0ee0869695d4de1a2eb237778896384d7baae2409804bc3fe36343435"}, "docker": "quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19.
shpc-registry automated BioContainers addition for bioconductor-huexexonprobesetlocationhg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19:0.0.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19/0.0.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-huexexonprobesetlocationhg19/0.0.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-huexexonprobesetlocationhg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huexexonprobesetlocationhg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-huexexonprobesetlocationhg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-huexexonprobesetlocationhg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-huexexonprobesetlocationhg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-huexexonprobesetlocationhg19-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-huexexonprobesetlocationhg19

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