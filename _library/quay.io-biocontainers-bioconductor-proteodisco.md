---
layout: container
name:  "quay.io/biocontainers/bioconductor-proteodisco"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-proteodisco/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-proteodisco/container.yaml"
updated_at: "2024-11-15 02:49:58.436196"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-proteodisco"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-proteodisco"
config: {"url": "https://biocontainers.pro/tools/bioconductor-proteodisco", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-proteodisco", "latest": {"1.8.0--r43hdfd78af_0": "sha256:5b76be3507ccfe6a2e97f129c143854b0a7b8932b0c55d7db08d3195d7a03203"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:1ec748e5a167868599e65fc39e1c99562281c64f5266e9044f5843adb86f0f35", "1.4.0--r42hdfd78af_0": "sha256:7260d08a7d9677ff9aa08010807f2b6e618748b73f23dd29f2bac008ef100702", "1.6.0--r43hdfd78af_0": "sha256:45920247f362e5af6d9caa72686ed59d9dbeda8de68ae853d9e45be4336ea30b", "1.8.0--r43hdfd78af_0": "sha256:5b76be3507ccfe6a2e97f129c143854b0a7b8932b0c55d7db08d3195d7a03203"}, "docker": "quay.io/biocontainers/bioconductor-proteodisco"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-proteodisco.
shpc-registry automated BioContainers addition for bioconductor-proteodisco
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-proteodisco
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-proteodisco:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-proteodisco/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-proteodisco/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-proteodisco-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proteodisco-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-proteodisco-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-proteodisco-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-proteodisco-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-proteodisco-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-proteodisco

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