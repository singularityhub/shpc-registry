---
layout: container
name:  "quay.io/biocontainers/bioconductor-u133aaofav2cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-u133aaofav2cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-u133aaofav2cdf/container.yaml"
updated_at: "2024-02-13 02:49:58.843685"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-u133aaofav2cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-u133aaofav2cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-u133aaofav2cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-u133aaofav2cdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:c0d8e0392925f4db7a622465eb0c75364c9c441e4de570660bbdf3a02be2ba67"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:4febb3cdc81750411c1b230864066905c194c37798b9c70c8bd4f70105d8e108", "2.18.0--r42hdfd78af_10": "sha256:0d0a4217b2ea5a14edde24e995bb971a0bfe3d4f4d99f23332cf47c16a245c75", "2.18.0--r43hdfd78af_11": "sha256:a08db026e7a795646c9cb459dea6642d3d319c0df0a1f2000d43fa50d4e35358", "2.18.0--r43hdfd78af_12": "sha256:c0d8e0392925f4db7a622465eb0c75364c9c441e4de570660bbdf3a02be2ba67"}, "docker": "quay.io/biocontainers/bioconductor-u133aaofav2cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-u133aaofav2cdf.
shpc-registry automated BioContainers addition for bioconductor-u133aaofav2cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-u133aaofav2cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-u133aaofav2cdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-u133aaofav2cdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-u133aaofav2cdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-u133aaofav2cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133aaofav2cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-u133aaofav2cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-u133aaofav2cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-u133aaofav2cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-u133aaofav2cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-u133aaofav2cdf

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