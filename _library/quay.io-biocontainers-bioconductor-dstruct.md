---
layout: container
name:  "quay.io/biocontainers/bioconductor-dstruct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dstruct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dstruct/container.yaml"
updated_at: "2025-03-20 04:32:21.011107"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dstruct"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dstruct"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dstruct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dstruct", "latest": {"1.12.0--r44hdfd78af_0": "sha256:9c48bdbf36b47e8d521019dfaa6168c90b2f6002a8a1a43f57da4f172b816225"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:10f38ea906d4358a23f7601aa9bfc48f0f90687bf85d71b6fbfe15a2c136ad24", "1.4.0--r42hdfd78af_0": "sha256:ebc9f088cf279976c6349fdcdba52c6db2a7f9f649db90bf2b7ddc85fb2d6f5e", "1.6.0--r43hdfd78af_0": "sha256:8808f108494e69a10ce105bb36f4f2936f7df4030d4299c43d0c5503d5348d4b", "1.8.0--r43hdfd78af_0": "sha256:0783667b950057bce1a8cb39c280a5dbbc8291b91f79408db918e9cad3da2a72", "1.12.0--r44hdfd78af_0": "sha256:9c48bdbf36b47e8d521019dfaa6168c90b2f6002a8a1a43f57da4f172b816225"}, "docker": "quay.io/biocontainers/bioconductor-dstruct"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dstruct.
shpc-registry automated BioContainers addition for bioconductor-dstruct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dstruct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dstruct:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dstruct/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dstruct/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dstruct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dstruct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dstruct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dstruct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dstruct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dstruct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dstruct

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