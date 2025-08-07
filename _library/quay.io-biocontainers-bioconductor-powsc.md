---
layout: container
name:  "quay.io/biocontainers/bioconductor-powsc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-powsc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-powsc/container.yaml"
updated_at: "2025-08-07 10:14:27.184415"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-powsc"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-powsc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-powsc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-powsc", "latest": {"1.14.0--r44hdfd78af_0": "sha256:aa40e71a75ba22417d9d7f837730ad9e1bfa3661c4a8fb23a8deb2fe12b78082"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:ceb8dde2ce5e6ca674cc442e347f32e4e3800e681782d331d0a39a4e06a1a09b", "1.6.0--r42hdfd78af_0": "sha256:828db860b4e024aabf9bc4c842e80663ff7ac7edd67219c52e33a486ba8e9ab2", "1.8.0--r43hdfd78af_0": "sha256:4f2a3e455ab37c3eeb28f08fd193b335b18cae83c78c061821625e81897dfb87", "1.10.0--r43hdfd78af_0": "sha256:bbc6f375ac3d0e79147d9b4db9376429474f661ad56ced62c53ee6287cb01df1", "1.14.0--r44hdfd78af_0": "sha256:aa40e71a75ba22417d9d7f837730ad9e1bfa3661c4a8fb23a8deb2fe12b78082"}, "docker": "quay.io/biocontainers/bioconductor-powsc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-powsc.
shpc-registry automated BioContainers addition for bioconductor-powsc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-powsc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-powsc:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-powsc/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-powsc/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-powsc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-powsc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-powsc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-powsc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-powsc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-powsc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-powsc

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