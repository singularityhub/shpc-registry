---
layout: container
name:  "quay.io/biocontainers/translig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/translig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/translig/container.yaml"
updated_at: "2025-01-14 02:58:33.652155"
latest: "1.3--h56fc30b_0"
container_url: "https://biocontainers.pro/tools/translig"
aliases:
 - "Assemble"
 - "Get_output"
 - "TransLiG_iteration"
 - "connect_graph"
 - "refine"
versions:
 - "1.3--h56fc30b_0"
description: "shpc-registry automated BioContainers addition for translig"
config: {"url": "https://biocontainers.pro/tools/translig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for translig", "latest": {"1.3--h56fc30b_0": "sha256:f1f62b34a7a51df41e96948fe8114937da331e18405c5b1b99b23452221232a2"}, "tags": {"1.3--h56fc30b_0": "sha256:f1f62b34a7a51df41e96948fe8114937da331e18405c5b1b99b23452221232a2"}, "docker": "quay.io/biocontainers/translig", "aliases": {"Assemble": "/usr/local/bin/Assemble", "Get_output": "/usr/local/bin/Get_output", "TransLiG_iteration": "/usr/local/bin/TransLiG_iteration", "connect_graph": "/usr/local/bin/connect_graph", "refine": "/usr/local/bin/refine"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/translig.
shpc-registry automated BioContainers addition for translig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/translig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/translig:1.3--h56fc30b_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/translig/1.3--h56fc30b_0
$ module help quay.io/biocontainers/translig/1.3--h56fc30b_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### translig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### translig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### translig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### translig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### translig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### translig-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Assemble

```bash
$ singularity exec <container> /usr/local/bin/Assemble
$ podman run --it --rm --entrypoint /usr/local/bin/Assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Assemble   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Get_output

```bash
$ singularity exec <container> /usr/local/bin/Get_output
$ podman run --it --rm --entrypoint /usr/local/bin/Get_output   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Get_output   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### TransLiG_iteration

```bash
$ singularity exec <container> /usr/local/bin/TransLiG_iteration
$ podman run --it --rm --entrypoint /usr/local/bin/TransLiG_iteration   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/TransLiG_iteration   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### connect_graph

```bash
$ singularity exec <container> /usr/local/bin/connect_graph
$ podman run --it --rm --entrypoint /usr/local/bin/connect_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/connect_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### refine

```bash
$ singularity exec <container> /usr/local/bin/refine
$ podman run --it --rm --entrypoint /usr/local/bin/refine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/refine   -v ${PWD} -w ${PWD} <container> -c " $@"
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