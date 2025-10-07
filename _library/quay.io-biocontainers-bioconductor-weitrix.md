---
layout: container
name:  "quay.io/biocontainers/bioconductor-weitrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-weitrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-weitrix/container.yaml"
updated_at: "2025-10-07 03:23:53.440782"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-weitrix"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-weitrix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-weitrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-weitrix", "latest": {"1.18.0--r44hdfd78af_0": "sha256:acc50a6a6cbde18be6c2d1c4595aae58ff31e2ddff9eac90a7bf91e53834566b"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:c5989f3483caadb7bda5a89e558444c312ba72cb45b6e6791c358ecb013be781", "1.10.0--r42hdfd78af_0": "sha256:e8fb4c6e3b18c33e981ba4bd85694016f2ce658718b605f14f34592f0b2b4180", "1.12.0--r43hdfd78af_0": "sha256:233f398adedd98794769fd09ddc69e720d1b845b55429d94eb06c090fc525aa7", "1.14.0--r43hdfd78af_0": "sha256:5df2c7e190f3a54677cf521b5bb9ea84e49a0e13a66d10f878666b060e72630b", "1.18.0--r44hdfd78af_0": "sha256:acc50a6a6cbde18be6c2d1c4595aae58ff31e2ddff9eac90a7bf91e53834566b"}, "docker": "quay.io/biocontainers/bioconductor-weitrix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-weitrix.
shpc-registry automated BioContainers addition for bioconductor-weitrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-weitrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-weitrix:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-weitrix/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-weitrix/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-weitrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-weitrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-weitrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-weitrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-weitrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-weitrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-weitrix

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