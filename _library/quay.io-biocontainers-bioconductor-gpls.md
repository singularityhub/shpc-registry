---
layout: container
name:  "quay.io/biocontainers/bioconductor-gpls"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gpls/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gpls/container.yaml"
updated_at: "2025-01-02 03:03:26.676595"
latest: "1.78.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gpls"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_1"
 - "1.78.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gpls"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gpls", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gpls", "latest": {"1.78.0--r44hdfd78af_0": "sha256:16d682db4b87b229177fdb53dd4750170ab0fa7faab9ca109b7e067d29962132"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:6b08bcf5d21e61147468eccbd5f1a44dcf56bd26109327bcbc81450cd74e1495", "1.70.0--r42hdfd78af_0": "sha256:538d91d6d48d62807132393cdaab4a8e433b0f92712bdec5790f6fa5fc7a415d", "1.72.0--r43hdfd78af_0": "sha256:9f5ec025704a75a90d8396c428c0405c96582a2e70634ee71779e790bc2a5250", "1.74.0--r43hdfd78af_1": "sha256:c4fb17033c053f598135552ce493b36dfcdbb57a341723083fca3dd6206a3060", "1.78.0--r44hdfd78af_0": "sha256:16d682db4b87b229177fdb53dd4750170ab0fa7faab9ca109b7e067d29962132"}, "docker": "quay.io/biocontainers/bioconductor-gpls"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gpls.
shpc-registry automated BioContainers addition for bioconductor-gpls
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gpls
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gpls:1.78.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gpls/1.78.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gpls/1.78.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gpls-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpls-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gpls-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gpls-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gpls-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gpls-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gpls

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