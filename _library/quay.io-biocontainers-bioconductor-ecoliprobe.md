---
layout: container
name:  "quay.io/biocontainers/bioconductor-ecoliprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ecoliprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ecoliprobe/container.yaml"
updated_at: "2025-01-26 03:00:44.636742"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-ecoliprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-ecoliprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ecoliprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ecoliprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:d8a3da750a2b4ced3e59dc838941e4bf7bafa85a0c73e5529e920f4c9219ed82"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:f4c3d5c95b2a786979e57334f22ed3fee4f3b734d9d51dedd09151060d1c20b0", "2.18.0--r42hdfd78af_10": "sha256:aeb5170dd6df9c7e274a4bd6ffecda3f6a5628c92d6643039c0b6650ca0c9075", "2.18.0--r43hdfd78af_11": "sha256:3680d16be14535694d572d34d128d00b73b523c45279a91023ad37e5e2b55426", "2.18.0--r43hdfd78af_12": "sha256:d8a3da750a2b4ced3e59dc838941e4bf7bafa85a0c73e5529e920f4c9219ed82"}, "docker": "quay.io/biocontainers/bioconductor-ecoliprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ecoliprobe.
shpc-registry automated BioContainers addition for bioconductor-ecoliprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoliprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ecoliprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ecoliprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-ecoliprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ecoliprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoliprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ecoliprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ecoliprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ecoliprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ecoliprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ecoliprobe

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