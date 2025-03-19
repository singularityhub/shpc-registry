---
layout: container
name:  "quay.io/biocontainers/bioconductor-atena"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-atena/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-atena/container.yaml"
updated_at: "2025-03-19 03:37:54.048015"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-atena"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-atena"
config: {"url": "https://biocontainers.pro/tools/bioconductor-atena", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-atena", "latest": {"1.12.0--r44hdfd78af_0": "sha256:98c77ae1420aec70d77c520cc42477ae41d1852d9e81faab12d62d4c9b694157"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:4348c6122fedb367c156c4f7144cd4ae74cdddc03898cb282cb94cae4df452a1", "1.4.0--r42hdfd78af_0": "sha256:fcbe9ea21c3e91a87a6d4ac27b45eacb9991bc1695a77bd48e527ad8bede9a19", "1.6.0--r43hdfd78af_0": "sha256:e0d2377ce8d2c453d24f1762884f8ca7218e98fc6d7fbbcd1413d06d3b9127fc", "1.8.0--r43hdfd78af_0": "sha256:c00c9453f641b53929c5c9e109e80b9601cf4a22cb7f9bcee70781adf5bd0201", "1.12.0--r44hdfd78af_0": "sha256:98c77ae1420aec70d77c520cc42477ae41d1852d9e81faab12d62d4c9b694157"}, "docker": "quay.io/biocontainers/bioconductor-atena"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-atena.
shpc-registry automated BioContainers addition for bioconductor-atena
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-atena
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-atena:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-atena/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-atena/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-atena-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-atena-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-atena-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-atena-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-atena-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-atena-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-atena

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