---
layout: container
name:  "quay.io/biocontainers/mapsembler2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mapsembler2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mapsembler2/container.yaml"
updated_at: "2023-03-25 03:08:39.344984"
latest: "2.2.4--2"
container_url: "https://biocontainers.pro/tools/mapsembler2"
aliases:
 - "kissreads"
 - "kissreads_graph"
 - "mapsembler2_extend"
 - "mapsembler2_extremities"
 - "run_mapsembler2_pipeline.sh"
versions:
 - "2.2.4--2"
description: "shpc-registry automated BioContainers addition for mapsembler2"
config: {"url": "https://biocontainers.pro/tools/mapsembler2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mapsembler2", "latest": {"2.2.4--2": "sha256:6c00d13dec280c7250f2c6d44753a075f843a583a1681fc3af10813a6ef8f6a8"}, "tags": {"2.2.4--2": "sha256:6c00d13dec280c7250f2c6d44753a075f843a583a1681fc3af10813a6ef8f6a8"}, "docker": "quay.io/biocontainers/mapsembler2", "aliases": {"kissreads": "/usr/local/bin/kissreads", "kissreads_graph": "/usr/local/bin/kissreads_graph", "mapsembler2_extend": "/usr/local/bin/mapsembler2_extend", "mapsembler2_extremities": "/usr/local/bin/mapsembler2_extremities", "run_mapsembler2_pipeline.sh": "/usr/local/bin/run_mapsembler2_pipeline.sh"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mapsembler2.
shpc-registry automated BioContainers addition for mapsembler2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mapsembler2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mapsembler2:2.2.4--2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mapsembler2/2.2.4--2
$ module help quay.io/biocontainers/mapsembler2/2.2.4--2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mapsembler2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mapsembler2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mapsembler2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mapsembler2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mapsembler2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mapsembler2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### kissreads

```bash
$ singularity exec <container> /usr/local/bin/kissreads
$ podman run --it --rm --entrypoint /usr/local/bin/kissreads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kissreads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kissreads_graph

```bash
$ singularity exec <container> /usr/local/bin/kissreads_graph
$ podman run --it --rm --entrypoint /usr/local/bin/kissreads_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kissreads_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapsembler2_extend

```bash
$ singularity exec <container> /usr/local/bin/mapsembler2_extend
$ podman run --it --rm --entrypoint /usr/local/bin/mapsembler2_extend   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapsembler2_extend   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mapsembler2_extremities

```bash
$ singularity exec <container> /usr/local/bin/mapsembler2_extremities
$ podman run --it --rm --entrypoint /usr/local/bin/mapsembler2_extremities   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mapsembler2_extremities   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_mapsembler2_pipeline.sh

```bash
$ singularity exec <container> /usr/local/bin/run_mapsembler2_pipeline.sh
$ podman run --it --rm --entrypoint /usr/local/bin/run_mapsembler2_pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_mapsembler2_pipeline.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
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