---
layout: container
name:  "quay.io/biocontainers/bioconductor-alabaster.schemas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-alabaster.schemas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-alabaster.schemas/container.yaml"
updated_at: "2024-02-25 02:44:42.682456"
latest: "1.2.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-alabaster.schemas"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.2--r43hdfd78af_0"
 - "1.2.0--r43hdfd78af_1"
description: "singularity registry hpc automated addition for bioconductor-alabaster.schemas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-alabaster.schemas", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-alabaster.schemas", "latest": {"1.2.0--r43hdfd78af_1": "sha256:945dbcabef738369cc430a2dcd09b4c27aceefe5dd1fa60c507d0afb5d76f6a0"}, "tags": {"1.0.2--r43hdfd78af_0": "sha256:55253066339f278dba6189b1102bb83edd4fc25b75ec4eca0046914ba9e82b98", "1.2.0--r43hdfd78af_1": "sha256:945dbcabef738369cc430a2dcd09b4c27aceefe5dd1fa60c507d0afb5d76f6a0"}, "docker": "quay.io/biocontainers/bioconductor-alabaster.schemas", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-alabaster.schemas.
singularity registry hpc automated addition for bioconductor-alabaster.schemas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-alabaster.schemas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-alabaster.schemas:1.2.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-alabaster.schemas/1.2.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-alabaster.schemas/1.2.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-alabaster.schemas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alabaster.schemas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-alabaster.schemas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-alabaster.schemas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-alabaster.schemas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-alabaster.schemas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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