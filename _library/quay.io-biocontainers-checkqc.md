---
layout: container
name:  "quay.io/biocontainers/checkqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/checkqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/checkqc/container.yaml"
updated_at: "2023-01-27 03:37:47.071638"
latest: "3.7.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/checkqc"
aliases:
 - "checkqc"
 - "checkqc-ws"
 - "interop_aggregate"
 - "interop_dumpbin"
 - "interop_dumptext"
 - "interop_imaging_table"
 - "interop_index-summary"
 - "interop_plot_by_cycle"
 - "interop_plot_by_lane"
 - "interop_plot_flowcell"
 - "interop_plot_qscore_heatmap"
 - "interop_plot_qscore_histogram"
 - "interop_plot_sample_qc"
 - "interop_summary"
 - "sample-sheet"
 - "tabulate"
 - "normalizer"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "3.6.6--pyhdfd78af_0"
 - "3.7.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for checkqc"
config: {"url": "https://biocontainers.pro/tools/checkqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for checkqc", "latest": {"3.7.0--pyhdfd78af_0": "sha256:0ed4e0db46a8dd04045115b5712621808b54b8fc69e14588fa6285cd5656f5b4"}, "tags": {"3.6.6--pyhdfd78af_0": "sha256:fc4178f83f08068d1f4cc56d93918b4da6b760d85d7d9505381020104e13a8d8", "3.7.0--pyhdfd78af_0": "sha256:0ed4e0db46a8dd04045115b5712621808b54b8fc69e14588fa6285cd5656f5b4"}, "docker": "quay.io/biocontainers/checkqc", "aliases": {"checkqc": "/usr/local/bin/checkqc", "checkqc-ws": "/usr/local/bin/checkqc-ws", "interop_aggregate": "/usr/local/bin/interop_aggregate", "interop_dumpbin": "/usr/local/bin/interop_dumpbin", "interop_dumptext": "/usr/local/bin/interop_dumptext", "interop_imaging_table": "/usr/local/bin/interop_imaging_table", "interop_index-summary": "/usr/local/bin/interop_index-summary", "interop_plot_by_cycle": "/usr/local/bin/interop_plot_by_cycle", "interop_plot_by_lane": "/usr/local/bin/interop_plot_by_lane", "interop_plot_flowcell": "/usr/local/bin/interop_plot_flowcell", "interop_plot_qscore_heatmap": "/usr/local/bin/interop_plot_qscore_heatmap", "interop_plot_qscore_histogram": "/usr/local/bin/interop_plot_qscore_histogram", "interop_plot_sample_qc": "/usr/local/bin/interop_plot_sample_qc", "interop_summary": "/usr/local/bin/interop_summary", "sample-sheet": "/usr/local/bin/sample-sheet", "tabulate": "/usr/local/bin/tabulate", "normalizer": "/usr/local/bin/normalizer", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/checkqc.
shpc-registry automated BioContainers addition for checkqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/checkqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/checkqc:3.7.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/checkqc/3.7.0--pyhdfd78af_0
$ module help quay.io/biocontainers/checkqc/3.7.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### checkqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### checkqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### checkqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### checkqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### checkqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### checkqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### checkqc

```bash
$ singularity exec <container> /usr/local/bin/checkqc
$ podman run --it --rm --entrypoint /usr/local/bin/checkqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkqc-ws

```bash
$ singularity exec <container> /usr/local/bin/checkqc-ws
$ podman run --it --rm --entrypoint /usr/local/bin/checkqc-ws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkqc-ws   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_aggregate

```bash
$ singularity exec <container> /usr/local/bin/interop_aggregate
$ podman run --it --rm --entrypoint /usr/local/bin/interop_aggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_aggregate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_dumpbin

```bash
$ singularity exec <container> /usr/local/bin/interop_dumpbin
$ podman run --it --rm --entrypoint /usr/local/bin/interop_dumpbin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_dumpbin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_dumptext

```bash
$ singularity exec <container> /usr/local/bin/interop_dumptext
$ podman run --it --rm --entrypoint /usr/local/bin/interop_dumptext   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_dumptext   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_imaging_table

```bash
$ singularity exec <container> /usr/local/bin/interop_imaging_table
$ podman run --it --rm --entrypoint /usr/local/bin/interop_imaging_table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_imaging_table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_index-summary

```bash
$ singularity exec <container> /usr/local/bin/interop_index-summary
$ podman run --it --rm --entrypoint /usr/local/bin/interop_index-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_index-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_by_cycle

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_by_cycle
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_by_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_by_cycle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_by_lane

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_by_lane
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_by_lane   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_by_lane   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_flowcell

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_flowcell
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_flowcell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_flowcell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_qscore_heatmap

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_qscore_heatmap
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_heatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_heatmap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_qscore_histogram

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_qscore_histogram
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_qscore_histogram   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_plot_sample_qc

```bash
$ singularity exec <container> /usr/local/bin/interop_plot_sample_qc
$ podman run --it --rm --entrypoint /usr/local/bin/interop_plot_sample_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_plot_sample_qc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interop_summary

```bash
$ singularity exec <container> /usr/local/bin/interop_summary
$ podman run --it --rm --entrypoint /usr/local/bin/interop_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interop_summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sample-sheet

```bash
$ singularity exec <container> /usr/local/bin/sample-sheet
$ podman run --it --rm --entrypoint /usr/local/bin/sample-sheet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sample-sheet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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