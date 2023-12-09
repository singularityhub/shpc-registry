---
layout: container
name:  "quay.io/biocontainers/bioconductor-gp53cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gp53cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gp53cdf/container.yaml"
updated_at: "2023-12-09 02:59:59.294252"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-gp53cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-gp53cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gp53cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gp53cdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:8c9c4109ef92930bf3f3d0c16a56649705e30b0f786ee0e1e0eeacf514b41839"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:87242f8bd62f0173a9006f37ae6d0ee6f56c389b4e71c010cd795aa10e6f7751", "2.18.0--r42hdfd78af_10": "sha256:579c336123aa20c8d96e09bf56e81d520a6cd8d887f348731920e3254a8d46c9", "2.18.0--r43hdfd78af_11": "sha256:8c9c4109ef92930bf3f3d0c16a56649705e30b0f786ee0e1e0eeacf514b41839"}, "docker": "quay.io/biocontainers/bioconductor-gp53cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gp53cdf.
shpc-registry automated BioContainers addition for bioconductor-gp53cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gp53cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gp53cdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gp53cdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-gp53cdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gp53cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gp53cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gp53cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gp53cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gp53cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gp53cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gp53cdf

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