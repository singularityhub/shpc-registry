---
layout: container
name:  "quay.io/biocontainers/bioconductor-riboseqr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-riboseqr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-riboseqr/container.yaml"
updated_at: "2025-01-11 03:26:15.998689"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-riboseqr"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-riboseqr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-riboseqr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-riboseqr", "latest": {"1.40.0--r44hdfd78af_0": "sha256:dbd5c918880035358179788ce97d952d774c586fdfc3f8659845daf6660bffe6"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:faa48e03f2e2ac84af95a57db5fc26ed56dcf06bf9e87ed894f16d4cbfaed66d", "1.32.0--r42hdfd78af_0": "sha256:451cfaf446a7febb7f7c370da3f3bc1c88377f827ee2be23bd5931b99565728d", "1.36.0--r43hdfd78af_0": "sha256:7c5356532cb7b81f11ed78e93eaf56a9ab33d18c274be2883f490d7bd33c7123", "1.40.0--r44hdfd78af_0": "sha256:dbd5c918880035358179788ce97d952d774c586fdfc3f8659845daf6660bffe6"}, "docker": "quay.io/biocontainers/bioconductor-riboseqr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-riboseqr.
shpc-registry automated BioContainers addition for bioconductor-riboseqr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-riboseqr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-riboseqr:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-riboseqr/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-riboseqr/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-riboseqr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-riboseqr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-riboseqr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-riboseqr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-riboseqr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-riboseqr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-riboseqr

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