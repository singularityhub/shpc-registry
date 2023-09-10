---
layout: container
name:  "quay.io/biocontainers/bioconductor-ffpeexampledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ffpeexampledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ffpeexampledata/container.yaml"
updated_at: "2023-09-10 02:33:14.889735"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ffpeexampledata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ffpeexampledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ffpeexampledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ffpeexampledata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:757308d10ec8089ee17a6099d505c1f6ef9cbae667f6e00dc6c5d5a3700308b8"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:bf2e7ef8a3567778da4172ea163a721f28166ec97fc7c42c57cf91d5a37d9294", "1.36.0--r42hdfd78af_0": "sha256:5e02919f62366f66bb8ac5fd71d3a08c261a3e1be09bf6daf3b87c598af79cf4", "1.38.0--r43hdfd78af_0": "sha256:757308d10ec8089ee17a6099d505c1f6ef9cbae667f6e00dc6c5d5a3700308b8"}, "docker": "quay.io/biocontainers/bioconductor-ffpeexampledata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ffpeexampledata.
shpc-registry automated BioContainers addition for bioconductor-ffpeexampledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ffpeexampledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ffpeexampledata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ffpeexampledata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ffpeexampledata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ffpeexampledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ffpeexampledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ffpeexampledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ffpeexampledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ffpeexampledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ffpeexampledata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ffpeexampledata

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