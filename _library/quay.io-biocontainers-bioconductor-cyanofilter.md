---
layout: container
name:  "quay.io/biocontainers/bioconductor-cyanofilter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cyanofilter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cyanofilter/container.yaml"
updated_at: "2024-07-08 02:56:25.370833"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cyanofilter"
aliases:
 - "geosop"
 - "geos-config"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cyanofilter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cyanofilter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cyanofilter", "latest": {"1.10.0--r43hdfd78af_0": "sha256:15db4a02f74bc821e2b1de88e70478ffa883c46635064e47f2663e236c1bedc7"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:cec3a76eeca3b237a7b5c5ae6d96d6dd6c6230c6ab6a977798782e8f462422d4", "1.6.0--r42hdfd78af_0": "sha256:d7618c0437c0b93ba9cbb62aa5db6791eae6f35e940bf48fa88948b7b1f5de9a", "1.8.0--r43hdfd78af_0": "sha256:3a297ec9789f85f223944d7f51ff40554315d2d4ab92b85f935eac105b9d7291", "1.10.0--r43hdfd78af_0": "sha256:15db4a02f74bc821e2b1de88e70478ffa883c46635064e47f2663e236c1bedc7"}, "docker": "quay.io/biocontainers/bioconductor-cyanofilter", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cyanofilter.
shpc-registry automated BioContainers addition for bioconductor-cyanofilter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cyanofilter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cyanofilter:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cyanofilter/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cyanofilter/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cyanofilter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cyanofilter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cyanofilter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cyanofilter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cyanofilter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cyanofilter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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