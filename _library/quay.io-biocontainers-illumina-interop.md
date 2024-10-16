---
layout: container
name:  "quay.io/biocontainers/illumina-interop"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/illumina-interop/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/illumina-interop/container.yaml"
updated_at: "2024-10-16 03:05:40.030426"
latest: "1.3.2--hdbdd923_0"
container_url: "https://biocontainers.pro/tools/illumina-interop"
aliases:
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
versions:
 - "1.1.9--he1b5a44_0"
 - "1.2.0--h87f3376_0"
 - "1.1.28--h87f3376_0"
 - "1.2.1--h87f3376_0"
 - "1.2.2--h87f3376_0"
 - "1.2.3--h87f3376_0"
 - "1.2.4--h87f3376_0"
 - "1.2.4--hdbdd923_2"
 - "1.3.1--hdbdd923_0"
 - "1.3.1--hdbdd923_1"
 - "1.3.2--hdbdd923_0"
description: "shpc-registry automated BioContainers addition for illumina-interop"
config: {"url": "https://biocontainers.pro/tools/illumina-interop", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for illumina-interop", "latest": {"1.3.2--hdbdd923_0": "sha256:49f76ff2d267a39b2c03795eedda363f714f4e82e20ba2fa3622b10ad03d49ea"}, "tags": {"1.1.9--he1b5a44_0": "sha256:158e011166925ed1ba899c06dc275a5720f243ccbe99f5256af8ec63fa5835a1", "1.2.0--h87f3376_0": "sha256:9dc9ef90da1073ff4e3d1ab5e21999f06c73974c9ba5350a523d37d83c696ee4", "1.1.28--h87f3376_0": "sha256:2e917edd725e6427ae589a776d17832619af67c4408837217c1897d640ef5fbd", "1.2.1--h87f3376_0": "sha256:d2752a7c91ae2c2f872cc68c329c2fa626cbeca9cf86b44a36c5a2b3fc69d883", "1.2.2--h87f3376_0": "sha256:baf1af55952281fa4ecd25d0a10c2358fe528b44b3797ef6dc17f5649fee583f", "1.2.3--h87f3376_0": "sha256:5de63c92ede2a05ce42ba3d8066298404c350049c6c1844136102a30e7c220fb", "1.2.4--h87f3376_0": "sha256:20a695f3ad530192a0e3564e85f4fc4a23fd296da1730a0b8b4295ca1f6732f3", "1.2.4--hdbdd923_2": "sha256:2922da792a0cb34516084c0c4920edf4b10d76d080303277c99840d0a381c1cf", "1.3.1--hdbdd923_0": "sha256:5b42f0e5cecb111e4e76b0e0f697f4730697e22e8315dbf4a481998c33c71f27", "1.3.1--hdbdd923_1": "sha256:7b2245248172948d7b49fbfa6a488d1c3a4b4ed1d1293a76e40f7859ec31d483", "1.3.2--hdbdd923_0": "sha256:49f76ff2d267a39b2c03795eedda363f714f4e82e20ba2fa3622b10ad03d49ea"}, "docker": "quay.io/biocontainers/illumina-interop", "aliases": {"interop_aggregate": "/usr/local/bin/interop_aggregate", "interop_dumpbin": "/usr/local/bin/interop_dumpbin", "interop_dumptext": "/usr/local/bin/interop_dumptext", "interop_imaging_table": "/usr/local/bin/interop_imaging_table", "interop_index-summary": "/usr/local/bin/interop_index-summary", "interop_plot_by_cycle": "/usr/local/bin/interop_plot_by_cycle", "interop_plot_by_lane": "/usr/local/bin/interop_plot_by_lane", "interop_plot_flowcell": "/usr/local/bin/interop_plot_flowcell", "interop_plot_qscore_heatmap": "/usr/local/bin/interop_plot_qscore_heatmap", "interop_plot_qscore_histogram": "/usr/local/bin/interop_plot_qscore_histogram", "interop_plot_sample_qc": "/usr/local/bin/interop_plot_sample_qc", "interop_summary": "/usr/local/bin/interop_summary"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/illumina-interop.
shpc-registry automated BioContainers addition for illumina-interop
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/illumina-interop
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/illumina-interop:1.3.2--hdbdd923_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/illumina-interop/1.3.2--hdbdd923_0
$ module help quay.io/biocontainers/illumina-interop/1.3.2--hdbdd923_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### illumina-interop-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### illumina-interop-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### illumina-interop-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### illumina-interop-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### illumina-interop-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### illumina-interop-inspect-deffile:

```bash
$ singularity inspect -d <container>
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