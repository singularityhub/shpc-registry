---
layout: container
name:  "quay.io/biocontainers/atactk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/atactk/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/atactk/container.yaml"
updated_at: "2022-10-27 01:10:06.365699"
latest: "0.1.9--pyh3252c3a_0"
container_url: "https://biocontainers.pro/tools/atactk"
aliases:
 - "make_cut_matrix"
 - "make_midpoint_matrix"
 - "measure_features"
 - "measure_signal"
 - "plot_aggregate_cut_matrix.R"
 - "plot_aggregate_midpoint_matrix.R"
 - "plot_signal.R"
 - "trim_adapters"
versions:
 - "0.1.9--pyh3252c3a_0"
description: "shpc-registry automated BioContainers addition for atactk"
config: {"url": "https://biocontainers.pro/tools/atactk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for atactk", "latest": {"0.1.9--pyh3252c3a_0": "sha256:48487ce68e263e471ce4c97fbf3289242fd03b9d726d54c8c2866d62f2ee3a4f"}, "tags": {"0.1.9--pyh3252c3a_0": "sha256:48487ce68e263e471ce4c97fbf3289242fd03b9d726d54c8c2866d62f2ee3a4f"}, "docker": "quay.io/biocontainers/atactk", "aliases": {"make_cut_matrix": "/usr/local/bin/make_cut_matrix", "make_midpoint_matrix": "/usr/local/bin/make_midpoint_matrix", "measure_features": "/usr/local/bin/measure_features", "measure_signal": "/usr/local/bin/measure_signal", "plot_aggregate_cut_matrix.R": "/usr/local/bin/plot_aggregate_cut_matrix.R", "plot_aggregate_midpoint_matrix.R": "/usr/local/bin/plot_aggregate_midpoint_matrix.R", "plot_signal.R": "/usr/local/bin/plot_signal.R", "trim_adapters": "/usr/local/bin/trim_adapters"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/atactk.
shpc-registry automated BioContainers addition for atactk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/atactk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/atactk:0.1.9--pyh3252c3a_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/atactk/0.1.9--pyh3252c3a_0
$ module help quay.io/biocontainers/atactk/0.1.9--pyh3252c3a_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### atactk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### atactk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### atactk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### atactk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### atactk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### atactk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### make_cut_matrix

```bash
$ singularity exec <container> /usr/local/bin/make_cut_matrix
$ podman run --it --rm --entrypoint /usr/local/bin/make_cut_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_cut_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_midpoint_matrix

```bash
$ singularity exec <container> /usr/local/bin/make_midpoint_matrix
$ podman run --it --rm --entrypoint /usr/local/bin/make_midpoint_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_midpoint_matrix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### measure_features

```bash
$ singularity exec <container> /usr/local/bin/measure_features
$ podman run --it --rm --entrypoint /usr/local/bin/measure_features   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/measure_features   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### measure_signal

```bash
$ singularity exec <container> /usr/local/bin/measure_signal
$ podman run --it --rm --entrypoint /usr/local/bin/measure_signal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/measure_signal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_aggregate_cut_matrix.R

```bash
$ singularity exec <container> /usr/local/bin/plot_aggregate_cut_matrix.R
$ podman run --it --rm --entrypoint /usr/local/bin/plot_aggregate_cut_matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_aggregate_cut_matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_aggregate_midpoint_matrix.R

```bash
$ singularity exec <container> /usr/local/bin/plot_aggregate_midpoint_matrix.R
$ podman run --it --rm --entrypoint /usr/local/bin/plot_aggregate_midpoint_matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_aggregate_midpoint_matrix.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot_signal.R

```bash
$ singularity exec <container> /usr/local/bin/plot_signal.R
$ podman run --it --rm --entrypoint /usr/local/bin/plot_signal.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot_signal.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim_adapters

```bash
$ singularity exec <container> /usr/local/bin/trim_adapters
$ podman run --it --rm --entrypoint /usr/local/bin/trim_adapters   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim_adapters   -v ${PWD} -w ${PWD} <container> -c " $@"
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