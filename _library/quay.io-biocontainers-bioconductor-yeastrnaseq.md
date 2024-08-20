---
layout: container
name:  "quay.io/biocontainers/bioconductor-yeastrnaseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yeastrnaseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yeastrnaseq/container.yaml"
updated_at: "2024-08-20 03:05:41.069401"
latest: "0.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-yeastrnaseq"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.35.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-yeastrnaseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yeastrnaseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yeastrnaseq", "latest": {"0.40.0--r43hdfd78af_0": "sha256:481c3a5d4128fc319c268f3a92e12255a584c272f54638aed9eaab56a4da9cfa"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:3b71b0bcf818b6e0bc98684602920f304e6972d0f98b58c525e459a0bec27101", "0.35.0--r42hdfd78af_0": "sha256:9d2bd34842d12a59f65c879b66a67b129c91ce4a209180060512ac6bcbcd83d0", "0.38.0--r43hdfd78af_0": "sha256:69a0b1aa0e0c154ad564e2925441dee7d289b0b2a8e7ec0b148242667cba8d98", "0.40.0--r43hdfd78af_0": "sha256:481c3a5d4128fc319c268f3a92e12255a584c272f54638aed9eaab56a4da9cfa"}, "docker": "quay.io/biocontainers/bioconductor-yeastrnaseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yeastrnaseq.
shpc-registry automated BioContainers addition for bioconductor-yeastrnaseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastrnaseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastrnaseq:0.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yeastrnaseq/0.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-yeastrnaseq/0.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yeastrnaseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastrnaseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastrnaseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yeastrnaseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yeastrnaseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yeastrnaseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-yeastrnaseq

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