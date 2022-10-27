---
layout: container
name:  "quay.io/biocontainers/xyalign"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xyalign/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/xyalign/container.yaml"
updated_at: "2022-10-27 01:08:19.482618"
latest: "1.1.5--py_1"
container_url: "https://biocontainers.pro/tools/xyalign"
aliases:
 - "compare_vcfs"
 - "explore_thresholds"
 - "platypus"
 - "plot_count_stats"
 - "plot_window_differences"
 - "xyalign"
versions:
 - "1.1.5--py_1"
description: "shpc-registry automated BioContainers addition for xyalign"
config: {"url": "https://biocontainers.pro/tools/xyalign", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xyalign", "latest": {"1.1.5--py_1": "sha256:d9572aa1b2666a1f053dd15e4597bbacd21236b0cd51ede4499193126af0d31d"}, "tags": {"1.1.5--py_1": "sha256:d9572aa1b2666a1f053dd15e4597bbacd21236b0cd51ede4499193126af0d31d"}, "docker": "quay.io/biocontainers/xyalign", "aliases": {"compare_vcfs": "/usr/local/bin/compare_vcfs", "explore_thresholds": "/usr/local/bin/explore_thresholds", "platypus": "/usr/local/bin/platypus", "plot_count_stats": "/usr/local/bin/plot_count_stats", "plot_window_differences": "/usr/local/bin/plot_window_differences", "xyalign": "/usr/local/bin/xyalign"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xyalign.
shpc-registry automated BioContainers addition for xyalign
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xyalign
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xyalign:1.1.5--py_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xyalign/1.1.5--py_1
$ module help quay.io/biocontainers/xyalign/1.1.5--py_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xyalign-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xyalign-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xyalign-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xyalign-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xyalign-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xyalign-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### compare_vcfs

```bash
$ singularity exec <container> /usr/local/bin/compare_vcfs
$ podman run --it --rm --entrypoint /usr/local/bin/compare_vcfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compare_vcfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### explore_thresholds

```bash
$ singularity exec <container> /usr/local/bin/explore_thresholds
$ podman run --it --rm --entrypoint /usr/local/bin/explore_thresholds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/explore_thresholds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### platypus

```bash
$ singularity exec <container> /usr/local/bin/platypus
$ podman run --it --rm --entrypoint /usr/local/bin/platypus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/platypus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_count_stats

```bash
$ singularity exec <container> /usr/local/bin/plot_count_stats
$ podman run --it --rm --entrypoint /usr/local/bin/plot_count_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_count_stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_window_differences

```bash
$ singularity exec <container> /usr/local/bin/plot_window_differences
$ podman run --it --rm --entrypoint /usr/local/bin/plot_window_differences   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_window_differences   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xyalign

```bash
$ singularity exec <container> /usr/local/bin/xyalign
$ podman run --it --rm --entrypoint /usr/local/bin/xyalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xyalign   -v ${PWD} -w ${PWD} <container> -c " $@"
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