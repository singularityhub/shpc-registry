---
layout: container
name:  "quay.io/biocontainers/bioconductor-tbx20bamsubset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tbx20bamsubset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tbx20bamsubset/container.yaml"
updated_at: "2024-11-29 03:12:53.934979"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tbx20bamsubset"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tbx20bamsubset"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tbx20bamsubset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tbx20bamsubset", "latest": {"1.38.0--r43hdfd78af_0": "sha256:ca8c69a6944a30000c0bbdf4820937f5ff7de5d93f95b4630227b48c940ef540"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:53beac5705ce8e2a9a5acf71b322ebd3d25072efcf858b4e366087bc0ed4a4be", "1.34.0--r42hdfd78af_0": "sha256:dd9b6590e25d5320305a00fef75aac03629a0fa0039d18ef31ceeda9b5126301", "1.36.0--r43hdfd78af_0": "sha256:ad9d064755b02d405d96a6068c540abd19190e8c3de300d0e5ea719d905fe8ac", "1.38.0--r43hdfd78af_0": "sha256:ca8c69a6944a30000c0bbdf4820937f5ff7de5d93f95b4630227b48c940ef540"}, "docker": "quay.io/biocontainers/bioconductor-tbx20bamsubset"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tbx20bamsubset.
shpc-registry automated BioContainers addition for bioconductor-tbx20bamsubset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tbx20bamsubset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tbx20bamsubset:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tbx20bamsubset/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tbx20bamsubset/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tbx20bamsubset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tbx20bamsubset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tbx20bamsubset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tbx20bamsubset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tbx20bamsubset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tbx20bamsubset-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tbx20bamsubset

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