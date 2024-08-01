---
layout: container
name:  "quay.io/biocontainers/bioconductor-greylistchip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-greylistchip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-greylistchip/container.yaml"
updated_at: "2024-08-01 03:52:04.952780"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-greylistchip"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-greylistchip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-greylistchip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-greylistchip", "latest": {"1.34.0--r43hdfd78af_0": "sha256:70124e337b4825b6abb69bfd9847c33d91e503a51460af11ac615e970c4fe0a9"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:b480b0f16495d38024b723fc5d7622146185540b66ccfa888a6a6036a84f7194", "1.30.0--r42hdfd78af_0": "sha256:ce7e0d7674e530c03f7a7f3e62d7a1e0dae7256c7be714477e8b475118fb3fd7", "1.32.0--r43hdfd78af_0": "sha256:0b5d5e6bf6c3dfb6c53b4499c44befea622a750b21d34af1cc83965efacedb92", "1.34.0--r43hdfd78af_0": "sha256:70124e337b4825b6abb69bfd9847c33d91e503a51460af11ac615e970c4fe0a9"}, "docker": "quay.io/biocontainers/bioconductor-greylistchip"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-greylistchip.
shpc-registry automated BioContainers addition for bioconductor-greylistchip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-greylistchip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-greylistchip:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-greylistchip/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-greylistchip/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-greylistchip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-greylistchip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-greylistchip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-greylistchip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-greylistchip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-greylistchip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-greylistchip

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