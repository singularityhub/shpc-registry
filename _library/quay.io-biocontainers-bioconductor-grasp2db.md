---
layout: container
name:  "quay.io/biocontainers/bioconductor-grasp2db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-grasp2db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-grasp2db/container.yaml"
updated_at: "2023-08-26 02:38:32.452609"
latest: "1.1.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-grasp2db"

versions:
 - "1.1.0--r41hdfd78af_9"
 - "1.1.0--r41hdfd78af_10"
 - "1.1.0--r42hdfd78af_11"
 - "1.1.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-grasp2db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-grasp2db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-grasp2db", "latest": {"1.1.0--r43hdfd78af_12": "sha256:c346d3be0610a6fcd93b3acddc9e47de46766feaf87510d7e79c6022600ded3c"}, "tags": {"1.1.0--r41hdfd78af_9": "sha256:02543353a8b5f63baf1570f614fe0d8fd2a2edb5d0cc53758315a7b31d50c9e3", "1.1.0--r41hdfd78af_10": "sha256:103cf3058c01b66b85067a46568a03bf3012eb0a111aef479fc154d131bdd659", "1.1.0--r42hdfd78af_11": "sha256:c7566a5280af864a124f494f2936520a0e636b8725f5340296087f205d53c506", "1.1.0--r43hdfd78af_12": "sha256:c346d3be0610a6fcd93b3acddc9e47de46766feaf87510d7e79c6022600ded3c"}, "docker": "quay.io/biocontainers/bioconductor-grasp2db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-grasp2db.
shpc-registry automated BioContainers addition for bioconductor-grasp2db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-grasp2db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-grasp2db:1.1.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-grasp2db/1.1.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-grasp2db/1.1.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-grasp2db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grasp2db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-grasp2db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-grasp2db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-grasp2db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-grasp2db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-grasp2db

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