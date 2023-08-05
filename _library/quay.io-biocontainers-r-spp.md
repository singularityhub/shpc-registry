---
layout: container
name:  "quay.io/biocontainers/r-spp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-spp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-spp/container.yaml"
updated_at: "2023-08-05 02:54:45.372950"
latest: "1.16.0--r43h21a89ab_9"
container_url: "https://biocontainers.pro/tools/r-spp"

versions:
 - "1.16.0--r41hecf12ef_6"
 - "1.16.0--r42hecf12ef_7"
 - "1.16.0--r42h21a89ab_8"
 - "1.16.0--r43h21a89ab_9"
description: "shpc-registry automated BioContainers addition for r-spp"
config: {"url": "https://biocontainers.pro/tools/r-spp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-spp", "latest": {"1.16.0--r43h21a89ab_9": "sha256:3bf7e48337aa98beb9f5f5164b6f38efaca955e7b5906a5283d7a0355e48cf26"}, "tags": {"1.16.0--r41hecf12ef_6": "sha256:95447507e939d7ac532ab7958cddcc2d5b19d4c69931058961251a91cc38821a", "1.16.0--r42hecf12ef_7": "sha256:6681fcc17c0a6308163d96359af9e2aedf2e64cd7772edb4f709e446ea043781", "1.16.0--r42h21a89ab_8": "sha256:ced9a8d5b0beea4b10e18f3572aff948701dce3443696014d6c4cdc24a9cf383", "1.16.0--r43h21a89ab_9": "sha256:3bf7e48337aa98beb9f5f5164b6f38efaca955e7b5906a5283d7a0355e48cf26"}, "docker": "quay.io/biocontainers/r-spp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-spp.
shpc-registry automated BioContainers addition for r-spp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-spp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-spp:1.16.0--r43h21a89ab_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-spp/1.16.0--r43h21a89ab_9
$ module help quay.io/biocontainers/r-spp/1.16.0--r43h21a89ab_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-spp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-spp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-spp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-spp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-spp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-spp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-spp

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