---
layout: container
name:  "quay.io/biocontainers/bioconductor-hgu95av2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hgu95av2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hgu95av2cdf/container.yaml"
updated_at: "2025-01-08 03:21:02.606746"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hgu95av2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hgu95av2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hgu95av2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hgu95av2cdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:c4162631d2f8c5bcb4234e93324fc6ee433904e7345876d26fe339ee58779620"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:9e02febad828bfd41e28bd5212aa9c93141bd39776a87a3dd31988f594340b3d", "2.18.0--r42hdfd78af_10": "sha256:07703d9f9607c939817b3c83827430207c41cff396f047760aac7f1484cec4b5", "2.18.0--r43hdfd78af_11": "sha256:bada631bd1d5e5a4788a32ef9aa5897fcf9c42f911ca9a6a9b0ed963235d9f2b", "2.18.0--r43hdfd78af_12": "sha256:c5ee795597e85f11ebe6d3c4857f9e4bf25286c6f8b44248ba9b896a93f6d4d5", "2.18.0--r44hdfd78af_13": "sha256:c4162631d2f8c5bcb4234e93324fc6ee433904e7345876d26fe339ee58779620"}, "docker": "quay.io/biocontainers/bioconductor-hgu95av2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hgu95av2cdf.
shpc-registry automated BioContainers addition for bioconductor-hgu95av2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95av2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hgu95av2cdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hgu95av2cdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hgu95av2cdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hgu95av2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95av2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hgu95av2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hgu95av2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hgu95av2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hgu95av2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hgu95av2cdf

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