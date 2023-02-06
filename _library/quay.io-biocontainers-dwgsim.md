---
layout: container
name:  "quay.io/biocontainers/dwgsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dwgsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dwgsim/container.yaml"
updated_at: "2023-02-06 02:55:44.318767"
latest: "1.1.13--h20b1175_1"
container_url: "https://biocontainers.pro/tools/dwgsim"
aliases:
 - "dwgsim"
 - "dwgsim_eval"
versions:
 - "1.1.13--h20b1175_1"
description: "shpc-registry automated BioContainers addition for dwgsim"
config: {"url": "https://biocontainers.pro/tools/dwgsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dwgsim", "latest": {"1.1.13--h20b1175_1": "sha256:1feccc22a532068d3b789242097fd6dc9adf556497eac0a840d86e86e2b514b2"}, "tags": {"1.1.13--h20b1175_1": "sha256:1feccc22a532068d3b789242097fd6dc9adf556497eac0a840d86e86e2b514b2"}, "docker": "quay.io/biocontainers/dwgsim", "aliases": {"dwgsim": "/usr/local/bin/dwgsim", "dwgsim_eval": "/usr/local/bin/dwgsim_eval"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dwgsim.
shpc-registry automated BioContainers addition for dwgsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dwgsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dwgsim:1.1.13--h20b1175_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dwgsim/1.1.13--h20b1175_1
$ module help quay.io/biocontainers/dwgsim/1.1.13--h20b1175_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dwgsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dwgsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dwgsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dwgsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dwgsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dwgsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dwgsim

```bash
$ singularity exec <container> /usr/local/bin/dwgsim
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dwgsim_eval

```bash
$ singularity exec <container> /usr/local/bin/dwgsim_eval
$ podman run --it --rm --entrypoint /usr/local/bin/dwgsim_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dwgsim_eval   -v ${PWD} -w ${PWD} <container> -c " $@"
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