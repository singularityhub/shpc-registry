---
layout: container
name:  "quay.io/biocontainers/bioconductor-mbamethyl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mbamethyl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mbamethyl/container.yaml"
updated_at: "2024-02-20 02:57:43.934431"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mbamethyl"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mbamethyl"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mbamethyl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mbamethyl", "latest": {"1.36.0--r43hdfd78af_0": "sha256:bfb70375a485c801cb1dc6f5f72ef629b5b4da577a545d71304085c418e6741c"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:7b316bf7a4b160dfbaff749e09e9c1bc3bfa22a53e7505be7987f680fb4d9a83", "1.32.0--r42hdfd78af_0": "sha256:1de3f9d0a70c8cf29569d8563ffe81fe8d3b2edbdb06726d3fa8920de0f91b46", "1.34.0--r43hdfd78af_0": "sha256:629486d1d002750924a8fff1f81fe374d2cd621cb589e654e1cc7ed23ca65cb0", "1.36.0--r43hdfd78af_0": "sha256:bfb70375a485c801cb1dc6f5f72ef629b5b4da577a545d71304085c418e6741c"}, "docker": "quay.io/biocontainers/bioconductor-mbamethyl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mbamethyl.
shpc-registry automated BioContainers addition for bioconductor-mbamethyl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mbamethyl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mbamethyl:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mbamethyl/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mbamethyl/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mbamethyl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbamethyl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mbamethyl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mbamethyl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mbamethyl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mbamethyl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mbamethyl

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