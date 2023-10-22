---
layout: container
name:  "quay.io/biocontainers/r-diffcorr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-diffcorr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-diffcorr/container.yaml"
updated_at: "2023-10-22 03:14:21.089597"
latest: "0.4.3--r43h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-diffcorr"

versions:
 - "0.4.2--r41h3342da4_0"
 - "0.4.2--r42h3342da4_1"
 - "0.4.2--r43h3342da4_2"
 - "0.4.3--r43h3342da4_0"
description: "shpc-registry automated BioContainers addition for r-diffcorr"
config: {"url": "https://biocontainers.pro/tools/r-diffcorr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-diffcorr", "latest": {"0.4.3--r43h3342da4_0": "sha256:f6f6de0ebb0ae4726edee8438eeb961293e72f8f46aa1acd38735e6fe1bce84a"}, "tags": {"0.4.2--r41h3342da4_0": "sha256:6be201058cf0c4526b7b67d5798253110dbbfcac1867a41fb88274d65654248f", "0.4.2--r42h3342da4_1": "sha256:9f558f966ec4e3b952085edf049a91c32020b87b9d6f474a690081fa0f0ac6d7", "0.4.2--r43h3342da4_2": "sha256:283ca1c7588bc40c7c0f6605900675ecc2ad33ee1036d45706cbd7563826dc85", "0.4.3--r43h3342da4_0": "sha256:f6f6de0ebb0ae4726edee8438eeb961293e72f8f46aa1acd38735e6fe1bce84a"}, "docker": "quay.io/biocontainers/r-diffcorr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-diffcorr.
shpc-registry automated BioContainers addition for r-diffcorr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-diffcorr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-diffcorr:0.4.3--r43h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-diffcorr/0.4.3--r43h3342da4_0
$ module help quay.io/biocontainers/r-diffcorr/0.4.3--r43h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-diffcorr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-diffcorr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-diffcorr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-diffcorr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-diffcorr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-diffcorr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-diffcorr

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