---
layout: container
name:  "quay.io/biocontainers/hmnillumina"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmnillumina/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hmnillumina/container.yaml"
updated_at: "2024-12-19 04:27:46.550390"
latest: "1.5.1--hdcf5f25_0"
container_url: "https://biocontainers.pro/tools/hmnillumina"
aliases:
 - "HmnIllumina"
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
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "py.test"
 - "pytest"
 - "python3.1"
versions:
 - "1.5.0--hd03093a_0"
 - "1.5.0--hdcf5f25_1"
 - "1.5.1--hdcf5f25_0"
description: "singularity registry hpc automated addition for hmnillumina"
config: {"url": "https://biocontainers.pro/tools/hmnillumina", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for hmnillumina", "latest": {"1.5.1--hdcf5f25_0": "sha256:9dc5da9563a9baee8121a161cb4e553e727cc53cc7859043c81acb075b7710a0"}, "tags": {"1.5.0--hd03093a_0": "sha256:8c4669da955082570e8835f355e4a39a92830f6f036cdcf8450f7c7490eebca4", "1.5.0--hdcf5f25_1": "sha256:cdd6728de8c8563db0c0bb4cf98269ab71c943b2d5534c1aeec3bc27deda4a76", "1.5.1--hdcf5f25_0": "sha256:9dc5da9563a9baee8121a161cb4e553e727cc53cc7859043c81acb075b7710a0"}, "docker": "quay.io/biocontainers/hmnillumina", "aliases": {"HmnIllumina": "/usr/local/bin/HmnIllumina", "interop_aggregate": "/usr/local/bin/interop_aggregate", "interop_dumpbin": "/usr/local/bin/interop_dumpbin", "interop_dumptext": "/usr/local/bin/interop_dumptext", "interop_imaging_table": "/usr/local/bin/interop_imaging_table", "interop_index-summary": "/usr/local/bin/interop_index-summary", "interop_plot_by_cycle": "/usr/local/bin/interop_plot_by_cycle", "interop_plot_by_lane": "/usr/local/bin/interop_plot_by_lane", "interop_plot_flowcell": "/usr/local/bin/interop_plot_flowcell", "interop_plot_qscore_heatmap": "/usr/local/bin/interop_plot_qscore_heatmap", "interop_plot_qscore_histogram": "/usr/local/bin/interop_plot_qscore_histogram", "interop_plot_sample_qc": "/usr/local/bin/interop_plot_sample_qc", "interop_summary": "/usr/local/bin/interop_summary", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "py.test": "/usr/local/bin/py.test", "pytest": "/usr/local/bin/pytest", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmnillumina.
singularity registry hpc automated addition for hmnillumina
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmnillumina
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmnillumina:1.5.1--hdcf5f25_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmnillumina/1.5.1--hdcf5f25_0
$ module help quay.io/biocontainers/hmnillumina/1.5.1--hdcf5f25_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmnillumina-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmnillumina-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmnillumina-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmnillumina-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmnillumina-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmnillumina-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HmnIllumina

```bash
$ singularity exec <container> /usr/local/bin/HmnIllumina
$ podman run --it --rm --entrypoint /usr/local/bin/HmnIllumina   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HmnIllumina   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### py.test

```bash
$ singularity exec <container> /usr/local/bin/py.test
$ podman run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/py.test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pytest

```bash
$ singularity exec <container> /usr/local/bin/pytest
$ podman run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pytest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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