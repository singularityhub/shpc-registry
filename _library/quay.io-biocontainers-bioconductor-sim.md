---
layout: container
name:  "quay.io/biocontainers/bioconductor-sim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sim/container.yaml"
updated_at: "2023-10-06 03:11:24.059267"
latest: "1.70.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sim"

versions:
 - "1.64.0--r41hc0cfd56_2"
 - "1.68.0--r42hc0cfd56_0"
 - "1.70.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sim", "latest": {"1.70.0--r43ha9d7317_0": "sha256:a6fca26793bd710448adfecea851d0df7c7c668ac7177c2399f8eb44fa27478f"}, "tags": {"1.64.0--r41hc0cfd56_2": "sha256:2dbdc7989d751947023d56be791daaf25f8e9dc409b8041e855ab6d1303d8adf", "1.68.0--r42hc0cfd56_0": "sha256:cee82d6a811c0e6c1868373cdcfaa8698032ddee1ebefd0ef0927025c71d5c77", "1.70.0--r43ha9d7317_0": "sha256:a6fca26793bd710448adfecea851d0df7c7c668ac7177c2399f8eb44fa27478f"}, "docker": "quay.io/biocontainers/bioconductor-sim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sim.
shpc-registry automated BioContainers addition for bioconductor-sim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sim:1.70.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sim/1.70.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-sim/1.70.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sim

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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