---
layout: container
name:  "quay.io/biocontainers/bioconductor-tsrchitect"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tsrchitect/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tsrchitect/container.yaml"
updated_at: "2025-12-14 03:58:02.369401"
latest: "1.20.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tsrchitect"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.9--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tsrchitect"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tsrchitect", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tsrchitect", "latest": {"1.20.0--r41hdfd78af_0": "sha256:f3c060104205cfc84e8d8c8f0d1647b20c19c1904abca7377a0cdb73f4cae5b2"}, "tags": {"1.8.9--r351_0": "sha256:278f033baf2452044c1a3c9082566eb3df6aa7dc8d08a74b50a88b7a07f17686", "1.20.0--r41hdfd78af_0": "sha256:f3c060104205cfc84e8d8c8f0d1647b20c19c1904abca7377a0cdb73f4cae5b2", "1.18.0--r41hdfd78af_0": "sha256:822b92d0b7bff889fe66072f665a58fc23a87b442f4bd76cb665fb3561925fd1", "1.16.0--r40hdfd78af_1": "sha256:fb044dd5cf6f86abe3ce8702af91e952dade63619003b72817da17bd66a047dc", "1.14.0--r40_0": "sha256:ace03288d4e015a300df3d84c2f443af287656a478a4e7e42116f849726e8b8a", "1.12.0--r36_0": "sha256:75c6838cf28055459811628523d7b876daabbc571c68cd00fe15d980c08e02c6"}, "docker": "quay.io/biocontainers/bioconductor-tsrchitect", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tsrchitect.
shpc-registry automated BioContainers addition for bioconductor-tsrchitect
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tsrchitect
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tsrchitect:1.20.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tsrchitect/1.20.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tsrchitect/1.20.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tsrchitect-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tsrchitect-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tsrchitect-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tsrchitect-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tsrchitect-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tsrchitect-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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