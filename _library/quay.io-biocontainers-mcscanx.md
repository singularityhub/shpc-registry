---
layout: container
name:  "quay.io/biocontainers/mcscanx"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mcscanx/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mcscanx/container.yaml"
updated_at: "2025-03-03 03:45:47.410863"
latest: "1.0.0--h9948957_0"
container_url: "https://biocontainers.pro/tools/mcscanx"
aliases:
 - "MCScanX"
 - "MCScanX_h"
 - "duplicate_gene_classifier"
versions:
 - "0.1--h9948957_0"
 - "1.0.0--h9948957_0"
description: "singularity registry hpc automated addition for mcscanx"
config: {"url": "https://biocontainers.pro/tools/mcscanx", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mcscanx", "latest": {"1.0.0--h9948957_0": "sha256:bdf176aedfe9d1d7f11b58aefe12a96f4e9550a62be05d28809ad0c87832767c"}, "tags": {"0.1--h9948957_0": "sha256:e11c3cce3cce5339789302b164747aea4023b70c3da9b6b64161c95f27baf57d", "1.0.0--h9948957_0": "sha256:bdf176aedfe9d1d7f11b58aefe12a96f4e9550a62be05d28809ad0c87832767c"}, "docker": "quay.io/biocontainers/mcscanx", "aliases": {"MCScanX": "/usr/local/bin/MCScanX", "MCScanX_h": "/usr/local/bin/MCScanX_h", "duplicate_gene_classifier": "/usr/local/bin/duplicate_gene_classifier"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mcscanx.
singularity registry hpc automated addition for mcscanx
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mcscanx
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mcscanx:1.0.0--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mcscanx/1.0.0--h9948957_0
$ module help quay.io/biocontainers/mcscanx/1.0.0--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mcscanx-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mcscanx-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mcscanx-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mcscanx-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mcscanx-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mcscanx-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MCScanX

```bash
$ singularity exec <container> /usr/local/bin/MCScanX
$ podman run --it --rm --entrypoint /usr/local/bin/MCScanX   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MCScanX   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### MCScanX_h

```bash
$ singularity exec <container> /usr/local/bin/MCScanX_h
$ podman run --it --rm --entrypoint /usr/local/bin/MCScanX_h   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MCScanX_h   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### duplicate_gene_classifier

```bash
$ singularity exec <container> /usr/local/bin/duplicate_gene_classifier
$ podman run --it --rm --entrypoint /usr/local/bin/duplicate_gene_classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/duplicate_gene_classifier   -v ${PWD} -w ${PWD} <container> -c " $@"
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