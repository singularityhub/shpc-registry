---
layout: container
name:  "quay.io/biocontainers/bioconductor-scbubbletree"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scbubbletree/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scbubbletree/container.yaml"
updated_at: "2024-12-23 03:18:50.834629"
latest: "1.4.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scbubbletree"
aliases:
 - "geosop"
 - "geos-config"
 - "glpsol"
versions:
 - "1.0.0--r42hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-scbubbletree"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scbubbletree", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-scbubbletree", "latest": {"1.4.0--r43hdfd78af_0": "sha256:6fc425b88067a20d8fe22acd2a417c96f2abe15550c4f0a05143002e78b6638d"}, "tags": {"1.0.0--r42hdfd78af_0": "sha256:e838cb0a8c5ce2f339285f965ffa711d42b72e231d43afd425d6f7610e18816f", "1.2.0--r43hdfd78af_0": "sha256:f5d2b50f087b7c841bb050e1ade9f9711d44d7c97bd7c94ae90cb90c10905bcd", "1.4.0--r43hdfd78af_0": "sha256:6fc425b88067a20d8fe22acd2a417c96f2abe15550c4f0a05143002e78b6638d"}, "docker": "quay.io/biocontainers/bioconductor-scbubbletree", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scbubbletree.
singularity registry hpc automated addition for bioconductor-scbubbletree
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scbubbletree
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scbubbletree:1.4.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scbubbletree/1.4.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scbubbletree/1.4.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scbubbletree-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scbubbletree-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scbubbletree-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scbubbletree-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scbubbletree-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scbubbletree-inspect-deffile:

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


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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