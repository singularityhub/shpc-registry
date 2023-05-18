---
layout: container
name:  "quay.io/biocontainers/xs-sim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xs-sim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xs-sim/container.yaml"
updated_at: "2023-05-18 04:24:27.312690"
latest: "2--hec16e2b_0"
container_url: "https://biocontainers.pro/tools/xs-sim"
aliases:
 - "XS"
versions:
 - "1.0.0--hec16e2b_2"
 - "2--hec16e2b_0"
description: "shpc-registry automated BioContainers addition for xs-sim"
config: {"url": "https://biocontainers.pro/tools/xs-sim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xs-sim", "latest": {"2--hec16e2b_0": "sha256:0f15956d614206128523486dceef409646538e16863827f491b75d3f46aebe5d"}, "tags": {"1.0.0--hec16e2b_2": "sha256:3ffc1886a4573f187e5ab8af18b93a5931e13b5fdfb1ca8de69a8fddded0fb75", "2--hec16e2b_0": "sha256:0f15956d614206128523486dceef409646538e16863827f491b75d3f46aebe5d"}, "docker": "quay.io/biocontainers/xs-sim", "aliases": {"XS": "/usr/local/bin/XS"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xs-sim.
shpc-registry automated BioContainers addition for xs-sim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xs-sim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xs-sim:2--hec16e2b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xs-sim/2--hec16e2b_0
$ module help quay.io/biocontainers/xs-sim/2--hec16e2b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xs-sim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xs-sim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xs-sim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xs-sim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xs-sim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xs-sim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### XS

```bash
$ singularity exec <container> /usr/local/bin/XS
$ podman run --it --rm --entrypoint /usr/local/bin/XS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/XS   -v ${PWD} -w ${PWD} <container> -c " $@"
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