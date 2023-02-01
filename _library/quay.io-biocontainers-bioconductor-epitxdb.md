---
layout: container
name:  "quay.io/biocontainers/bioconductor-epitxdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epitxdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epitxdb/container.yaml"
updated_at: "2023-02-01 03:33:07.366216"
latest: "1.10.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epitxdb"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epitxdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epitxdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epitxdb", "latest": {"1.10.0--r42hdfd78af_0": "sha256:daeddbd072fbb8eb351de9ab5554acb2be4ec41bb85c701eed0e3ddefd1d6111"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:e9052ca98c818b4a1e60f9d4ae97f84345c5a461ae3134e21dad3abaf1f32b22", "1.10.0--r42hdfd78af_0": "sha256:daeddbd072fbb8eb351de9ab5554acb2be4ec41bb85c701eed0e3ddefd1d6111"}, "docker": "quay.io/biocontainers/bioconductor-epitxdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epitxdb.
shpc-registry automated BioContainers addition for bioconductor-epitxdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epitxdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epitxdb:1.10.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epitxdb/1.10.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epitxdb/1.10.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epitxdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epitxdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epitxdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epitxdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epitxdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epitxdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-epitxdb

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