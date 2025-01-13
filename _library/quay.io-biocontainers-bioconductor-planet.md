---
layout: container
name:  "quay.io/biocontainers/bioconductor-planet"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-planet/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-planet/container.yaml"
updated_at: "2025-01-13 03:18:39.353094"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-planet"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_1"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-planet"
config: {"url": "https://biocontainers.pro/tools/bioconductor-planet", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-planet", "latest": {"1.14.0--r44hdfd78af_0": "sha256:d48ffaad8eaf3d4036d3f0418592d83484f9a5561ec5a94fa20e7286dd036c60"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:798a740f510e5b83fcd6d6ff98d0278238ead921605bdc6d9dbdf3ae5b892add", "1.6.0--r42hdfd78af_0": "sha256:d27a70abfd1c614e6af35df1a6710a36eb8936548879d7f2c770ea8313f6a480", "1.8.0--r43hdfd78af_0": "sha256:631ce2e0b72bf0a9df8153d5da7bbb6fa55aa44493cce6710ee7055f6d26bbf2", "1.10.0--r43hdfd78af_1": "sha256:44f9603b90370137bc7d458aaf7f4a470b1ef1bb67b5253ba7619a1a5ee667bf", "1.14.0--r44hdfd78af_0": "sha256:d48ffaad8eaf3d4036d3f0418592d83484f9a5561ec5a94fa20e7286dd036c60"}, "docker": "quay.io/biocontainers/bioconductor-planet"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-planet.
shpc-registry automated BioContainers addition for bioconductor-planet
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-planet
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-planet:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-planet/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-planet/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-planet-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-planet-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-planet-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-planet-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-planet-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-planet-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-planet

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