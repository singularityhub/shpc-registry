---
layout: container
name:  "nvcr.io/nvidia/hpc-benchmarks"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/nvcr.io/nvidia/hpc-benchmarks/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/nvcr.io/nvidia/hpc-benchmarks/container.yaml"
updated_at: "2025-06-13 03:19:47.554467"
latest: "20.10-hpl"
container_url: "https://ngc.nvidia.com/catalog/containers/nvidia:hpc-benchmarks/tags"

versions:
 - "20.10-hpl"
 - "20.10-hpcg"
description: "The NVIDIA HPC-Benchmarks collection provides three NVIDIA accelerated HPC benchmarks: HPL-NVIDIA, HPL-AI-NVIDIA, and HPCG-NVIDIA."
config: {"docker": "nvcr.io/nvidia/hpc-benchmarks", "latest": {"20.10-hpl": "sha256:b8df1e330b9e0dbcda2108c88a5350795293b1f1cd231c40a763bceaf94eda98"}, "tags": {"20.10-hpl": "sha256:b8df1e330b9e0dbcda2108c88a5350795293b1f1cd231c40a763bceaf94eda98", "20.10-hpcg": "sha256:c52ce8822537f8b520aed30dab26cc811f7be934dcf3f80e804f81cf0e129e19"}, "filter": ["20.10*"], "maintainer": "@vsoch", "url": "https://ngc.nvidia.com/catalog/containers/nvidia:hpc-benchmarks/tags", "description": "The NVIDIA HPC-Benchmarks collection provides three NVIDIA accelerated HPC benchmarks: HPL-NVIDIA, HPL-AI-NVIDIA, and HPCG-NVIDIA.", "features": {"gpu": true}}
---

This module is a singularity container wrapper for nvcr.io/nvidia/hpc-benchmarks.
The NVIDIA HPC-Benchmarks collection provides three NVIDIA accelerated HPC benchmarks: HPL-NVIDIA, HPL-AI-NVIDIA, and HPCG-NVIDIA.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install nvcr.io/nvidia/hpc-benchmarks
```

Or a specific version:

```bash
$ shpc install nvcr.io/nvidia/hpc-benchmarks:20.10-hpl
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load nvcr.io/nvidia/hpc-benchmarks/20.10-hpl
$ module help nvcr.io/nvidia/hpc-benchmarks/20.10-hpl
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hpc-benchmarks-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hpc-benchmarks-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hpc-benchmarks-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hpc-benchmarks-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hpc-benchmarks-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hpc-benchmarks-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### hpc-benchmarks

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