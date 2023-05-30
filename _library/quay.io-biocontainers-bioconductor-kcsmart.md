---
layout: container
name:  "quay.io/biocontainers/bioconductor-kcsmart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-kcsmart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-kcsmart/container.yaml"
updated_at: "2023-05-30 18:08:14.938852"
latest: "2.56.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-kcsmart"

versions:
 - "2.52.0--r41hdfd78af_0"
 - "2.56.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-kcsmart"
config: {"url": "https://biocontainers.pro/tools/bioconductor-kcsmart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-kcsmart", "latest": {"2.56.0--r42hdfd78af_0": "sha256:73321381600cb437b4223322be11c9584ebe7a9e969429cdb916c954ed6f6554"}, "tags": {"2.52.0--r41hdfd78af_0": "sha256:24c7140dd930db7129265ce407bcbc77be66680c0317df07a1d1e34b38e8d0f1", "2.56.0--r42hdfd78af_0": "sha256:73321381600cb437b4223322be11c9584ebe7a9e969429cdb916c954ed6f6554"}, "docker": "quay.io/biocontainers/bioconductor-kcsmart"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-kcsmart.
shpc-registry automated BioContainers addition for bioconductor-kcsmart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-kcsmart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-kcsmart:2.56.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-kcsmart/2.56.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-kcsmart/2.56.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-kcsmart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kcsmart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-kcsmart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-kcsmart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-kcsmart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-kcsmart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-kcsmart

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