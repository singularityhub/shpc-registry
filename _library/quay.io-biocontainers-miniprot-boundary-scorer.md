---
layout: container
name:  "quay.io/biocontainers/miniprot-boundary-scorer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/miniprot-boundary-scorer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/miniprot-boundary-scorer/container.yaml"
updated_at: "2024-10-05 03:22:51.101979"
latest: "1.0.0--h4ac6f70_0"
container_url: "https://biocontainers.pro/tools/miniprot-boundary-scorer"
aliases:
 - "miniprot_boundary_scorer"
versions:
 - "1.0.0--h4ac6f70_0"
description: "singularity registry hpc automated addition for miniprot-boundary-scorer"
config: {"url": "https://biocontainers.pro/tools/miniprot-boundary-scorer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for miniprot-boundary-scorer", "latest": {"1.0.0--h4ac6f70_0": "sha256:3a469b4e70a56c81c94fad5d2666304c7ad25402fe37ee563ef88346986560eb"}, "tags": {"1.0.0--h4ac6f70_0": "sha256:3a469b4e70a56c81c94fad5d2666304c7ad25402fe37ee563ef88346986560eb"}, "docker": "quay.io/biocontainers/miniprot-boundary-scorer", "aliases": {"miniprot_boundary_scorer": "/usr/local/bin/miniprot_boundary_scorer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/miniprot-boundary-scorer.
singularity registry hpc automated addition for miniprot-boundary-scorer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/miniprot-boundary-scorer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/miniprot-boundary-scorer:1.0.0--h4ac6f70_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/miniprot-boundary-scorer/1.0.0--h4ac6f70_0
$ module help quay.io/biocontainers/miniprot-boundary-scorer/1.0.0--h4ac6f70_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### miniprot-boundary-scorer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### miniprot-boundary-scorer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### miniprot-boundary-scorer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### miniprot-boundary-scorer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### miniprot-boundary-scorer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### miniprot-boundary-scorer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miniprot_boundary_scorer

```bash
$ singularity exec <container> /usr/local/bin/miniprot_boundary_scorer
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot_boundary_scorer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot_boundary_scorer   -v ${PWD} -w ${PWD} <container> -c " $@"
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