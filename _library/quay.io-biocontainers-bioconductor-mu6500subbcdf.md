---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu6500subbcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu6500subbcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu6500subbcdf/container.yaml"
updated_at: "2023-12-17 03:05:18.150124"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-mu6500subbcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-mu6500subbcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu6500subbcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu6500subbcdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:dfb0f3432ad5f671f7ae50ecb6f58c996e286b10cf09cef562d1de2a54a0178a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:3f5476175e0580f07b7e16d04be5ca73357f116e00377ba905319b8926739eb8", "2.18.0--r42hdfd78af_10": "sha256:381c4278ea4bc832b57a856f8e043745d026c9678f28cbb935f942907578e2b0", "2.18.0--r43hdfd78af_11": "sha256:dfb0f3432ad5f671f7ae50ecb6f58c996e286b10cf09cef562d1de2a54a0178a"}, "docker": "quay.io/biocontainers/bioconductor-mu6500subbcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu6500subbcdf.
shpc-registry automated BioContainers addition for bioconductor-mu6500subbcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu6500subbcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu6500subbcdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu6500subbcdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-mu6500subbcdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu6500subbcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu6500subbcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu6500subbcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu6500subbcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu6500subbcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu6500subbcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu6500subbcdf

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