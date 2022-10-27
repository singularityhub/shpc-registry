---
layout: container
name:  "quay.io/biocontainers/pmx_biobb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pmx_biobb/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/pmx_biobb/container.yaml"
updated_at: "2022-10-27 00:42:02.736576"
latest: "1.0.0--py37hc94c342_3"
container_url: "https://biocontainers.pro/tools/pmx_biobb"
aliases:
 - "pmx"
versions:
 - "1.0.0--py37hc94c342_3"
description: "shpc-registry automated BioContainers addition for pmx_biobb"
config: {"url": "https://biocontainers.pro/tools/pmx_biobb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pmx_biobb", "latest": {"1.0.0--py37hc94c342_3": "sha256:131e2e50a98da7e1dfe8d1f4c33e80d3cf1ef6d5c87486115800d4252a38e12d"}, "tags": {"1.0.0--py37hc94c342_3": "sha256:131e2e50a98da7e1dfe8d1f4c33e80d3cf1ef6d5c87486115800d4252a38e12d"}, "docker": "quay.io/biocontainers/pmx_biobb", "aliases": {"pmx": "/usr/local/bin/pmx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pmx_biobb.
shpc-registry automated BioContainers addition for pmx_biobb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pmx_biobb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pmx_biobb:1.0.0--py37hc94c342_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pmx_biobb/1.0.0--py37hc94c342_3
$ module help quay.io/biocontainers/pmx_biobb/1.0.0--py37hc94c342_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pmx_biobb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pmx_biobb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pmx_biobb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pmx_biobb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pmx_biobb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pmx_biobb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pmx

```bash
$ singularity exec <container> /usr/local/bin/pmx
$ podman run --it --rm --entrypoint /usr/local/bin/pmx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pmx   -v ${PWD} -w ${PWD} <container> -c " $@"
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