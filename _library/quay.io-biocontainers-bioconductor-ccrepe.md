---
layout: container
name:  "quay.io/biocontainers/bioconductor-ccrepe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ccrepe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ccrepe/container.yaml"
updated_at: "2023-05-27 02:35:06.110115"
latest: "1.34.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ccrepe"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ccrepe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ccrepe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ccrepe", "latest": {"1.34.0--r42hdfd78af_0": "sha256:e742014fc0ecd1f02c9514766a7acfde83dc21674b5d98658b3382c0dd5c953a"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:bbb16f069adfe3ecb2b651f119b9e25957b7ea2e22d223ff9f831bfed3729144", "1.34.0--r42hdfd78af_0": "sha256:e742014fc0ecd1f02c9514766a7acfde83dc21674b5d98658b3382c0dd5c953a"}, "docker": "quay.io/biocontainers/bioconductor-ccrepe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ccrepe.
shpc-registry automated BioContainers addition for bioconductor-ccrepe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ccrepe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ccrepe:1.34.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ccrepe/1.34.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ccrepe/1.34.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ccrepe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccrepe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccrepe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ccrepe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ccrepe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ccrepe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ccrepe

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