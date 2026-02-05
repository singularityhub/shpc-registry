---
layout: container
name:  "quay.io/biocontainers/bioconductor-ccpromise"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ccpromise/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ccpromise/container.yaml"
updated_at: "2026-02-05 04:56:34.043215"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ccpromise"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ccpromise"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ccpromise", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ccpromise", "latest": {"1.32.0--r44hdfd78af_0": "sha256:fc434d025d5040efacca335115ed965ebd6a8e56a9956d1a34b8a8e9f622efb7"}, "tags": {"1.8.0--r351_0": "sha256:be49e3fdf780e625ddc004d11d81d69e54587277d8e08ad19b102556c62143ef", "1.24.0--r42hdfd78af_0": "sha256:b941f43c6de49a03320d1f17547404ee505d26639c50c5bd8835939b431334b1", "1.20.0--r41hdfd78af_0": "sha256:69811ee5a1711e66756a296edd3901a0b4d2ae7d26bc374813b1e0da69fe3719", "1.18.0--r41hdfd78af_0": "sha256:1be2dbb19f181af528e5d9609794a0ff749f4fc4d24eb53d19f349aa784a39ef", "1.16.0--r40hdfd78af_1": "sha256:ed7c18739aa6147676cc1477b69f0b92c947939fc52ff1402ef7ac54b323a7d0", "1.14.0--r40_0": "sha256:852876f638d5c5e40468aeacdce3e4ea684eeff259f4d600a81d763610632d3f", "1.26.0--r43hdfd78af_0": "sha256:589cdb1d177b2fdb885a7d92c32881a461843442cdae1d5c9a4b7b45f62eae08", "1.32.0--r44hdfd78af_0": "sha256:fc434d025d5040efacca335115ed965ebd6a8e56a9956d1a34b8a8e9f622efb7"}, "docker": "quay.io/biocontainers/bioconductor-ccpromise", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ccpromise.
shpc-registry automated BioContainers addition for bioconductor-ccpromise
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ccpromise
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ccpromise:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ccpromise/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ccpromise/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ccpromise-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccpromise-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ccpromise-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ccpromise-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ccpromise-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ccpromise-inspect-deffile:

```bash
$ singularity inspect -d <container>
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