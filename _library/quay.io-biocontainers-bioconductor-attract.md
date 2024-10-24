---
layout: container
name:  "quay.io/biocontainers/bioconductor-attract"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-attract/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-attract/container.yaml"
updated_at: "2024-10-24 10:33:46.074519"
latest: "1.52.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-attract"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-attract"
config: {"url": "https://biocontainers.pro/tools/bioconductor-attract", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-attract", "latest": {"1.52.0--r43hdfd78af_0": "sha256:acacf539a36c0ad8485a5410fdb888e3d3cf42c2474e7955d9e8c47c94d7a192"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:c13b1d6a4fc14094ba2a0f0361bbc9e67760830abf9054ed59a3a51d66b89234", "1.50.0--r42hdfd78af_0": "sha256:18229fde062f3b4cc7f1e4fbb7cb1fa44377bf5cb32711c2ed5e55f0a33ec1d4", "1.52.0--r43hdfd78af_0": "sha256:acacf539a36c0ad8485a5410fdb888e3d3cf42c2474e7955d9e8c47c94d7a192"}, "docker": "quay.io/biocontainers/bioconductor-attract"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-attract.
shpc-registry automated BioContainers addition for bioconductor-attract
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-attract
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-attract:1.52.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-attract/1.52.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-attract/1.52.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-attract-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-attract-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-attract-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-attract-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-attract-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-attract-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-attract

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