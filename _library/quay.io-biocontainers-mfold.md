---
layout: container
name:  "quay.io/biocontainers/mfold"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mfold/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mfold/container.yaml"
updated_at: "2026-02-04 04:52:15.768928"
latest: "3.6--h8537716_3"
container_url: "https://biocontainers.pro/tools/mfold"
aliases:
 - "add_dHdSTm"
 - "add_dHdSTm2"
 - "auxgen"
 - "boxplot_ng"
 - "ct2bp"
 - "ct_boxplot_ng"
 - "ct_compare"
 - "distance"
 - "efn"
 - "efn2"
 - "filter-sort"
 - "h-num"
 - "h_num"
 - "mfold"
 - "mfold_datdir"
 - "mfold_quik"
 - "myps2img.bash"
 - "myps2jpg.bash"
 - "myps2pdf.bash"
 - "myps2png.bash"
 - "nafold"
 - "newtemp"
 - "overlay_boxplot_ng"
 - "quikfold"
 - "reformat-seq.sh"
 - "sav2p_num"
 - "sav2plot"
 - "scorer"
 - "sir_graph"
 - "ss_count"
versions:
 - "3.6--h1aed7a7_1"
 - "3.6--h8537716_3"
description: "singularity registry hpc automated addition for mfold"
config: {"url": "https://biocontainers.pro/tools/mfold", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mfold", "latest": {"3.6--h8537716_3": "sha256:328376d1ade487fdabc8123895a38e9da7b8d3e67c53887b2255cd367b286ce8"}, "tags": {"3.6--h1aed7a7_1": "sha256:757bbdbfde35024a3ec25fb33ef53b5479e2ddf53de0d65bb5e155b2492a0194", "3.6--h8537716_3": "sha256:328376d1ade487fdabc8123895a38e9da7b8d3e67c53887b2255cd367b286ce8"}, "docker": "quay.io/biocontainers/mfold", "aliases": {"add_dHdSTm": "/usr/local/bin/add_dHdSTm", "add_dHdSTm2": "/usr/local/bin/add_dHdSTm2", "auxgen": "/usr/local/bin/auxgen", "boxplot_ng": "/usr/local/bin/boxplot_ng", "ct2bp": "/usr/local/bin/ct2bp", "ct_boxplot_ng": "/usr/local/bin/ct_boxplot_ng", "ct_compare": "/usr/local/bin/ct_compare", "distance": "/usr/local/bin/distance", "efn": "/usr/local/bin/efn", "efn2": "/usr/local/bin/efn2", "filter-sort": "/usr/local/bin/filter-sort", "h-num": "/usr/local/bin/h-num", "h_num": "/usr/local/bin/h_num", "mfold": "/usr/local/bin/mfold", "mfold_datdir": "/usr/local/bin/mfold_datdir", "mfold_quik": "/usr/local/bin/mfold_quik", "myps2img.bash": "/usr/local/bin/myps2img.bash", "myps2jpg.bash": "/usr/local/bin/myps2jpg.bash", "myps2pdf.bash": "/usr/local/bin/myps2pdf.bash", "myps2png.bash": "/usr/local/bin/myps2png.bash", "nafold": "/usr/local/bin/nafold", "newtemp": "/usr/local/bin/newtemp", "overlay_boxplot_ng": "/usr/local/bin/overlay_boxplot_ng", "quikfold": "/usr/local/bin/quikfold", "reformat-seq.sh": "/usr/local/bin/reformat-seq.sh", "sav2p_num": "/usr/local/bin/sav2p_num", "sav2plot": "/usr/local/bin/sav2plot", "scorer": "/usr/local/bin/scorer", "sir_graph": "/usr/local/bin/sir_graph", "ss_count": "/usr/local/bin/ss_count"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mfold.
singularity registry hpc automated addition for mfold
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mfold
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mfold:3.6--h8537716_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mfold/3.6--h8537716_3
$ module help quay.io/biocontainers/mfold/3.6--h8537716_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mfold-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mfold-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mfold-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mfold-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mfold-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mfold-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### add_dHdSTm

```bash
$ singularity exec <container> /usr/local/bin/add_dHdSTm
$ podman run --it --rm --entrypoint /usr/local/bin/add_dHdSTm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_dHdSTm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### add_dHdSTm2

```bash
$ singularity exec <container> /usr/local/bin/add_dHdSTm2
$ podman run --it --rm --entrypoint /usr/local/bin/add_dHdSTm2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/add_dHdSTm2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### auxgen

```bash
$ singularity exec <container> /usr/local/bin/auxgen
$ podman run --it --rm --entrypoint /usr/local/bin/auxgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/auxgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### boxplot_ng

```bash
$ singularity exec <container> /usr/local/bin/boxplot_ng
$ podman run --it --rm --entrypoint /usr/local/bin/boxplot_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/boxplot_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct2bp

```bash
$ singularity exec <container> /usr/local/bin/ct2bp
$ podman run --it --rm --entrypoint /usr/local/bin/ct2bp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct2bp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct_boxplot_ng

```bash
$ singularity exec <container> /usr/local/bin/ct_boxplot_ng
$ podman run --it --rm --entrypoint /usr/local/bin/ct_boxplot_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct_boxplot_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ct_compare

```bash
$ singularity exec <container> /usr/local/bin/ct_compare
$ podman run --it --rm --entrypoint /usr/local/bin/ct_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ct_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distance

```bash
$ singularity exec <container> /usr/local/bin/distance
$ podman run --it --rm --entrypoint /usr/local/bin/distance   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distance   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### efn

```bash
$ singularity exec <container> /usr/local/bin/efn
$ podman run --it --rm --entrypoint /usr/local/bin/efn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/efn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### efn2

```bash
$ singularity exec <container> /usr/local/bin/efn2
$ podman run --it --rm --entrypoint /usr/local/bin/efn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/efn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-sort

```bash
$ singularity exec <container> /usr/local/bin/filter-sort
$ podman run --it --rm --entrypoint /usr/local/bin/filter-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h-num

```bash
$ singularity exec <container> /usr/local/bin/h-num
$ podman run --it --rm --entrypoint /usr/local/bin/h-num   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h-num   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h_num

```bash
$ singularity exec <container> /usr/local/bin/h_num
$ podman run --it --rm --entrypoint /usr/local/bin/h_num   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h_num   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mfold

```bash
$ singularity exec <container> /usr/local/bin/mfold
$ podman run --it --rm --entrypoint /usr/local/bin/mfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mfold_datdir

```bash
$ singularity exec <container> /usr/local/bin/mfold_datdir
$ podman run --it --rm --entrypoint /usr/local/bin/mfold_datdir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfold_datdir   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mfold_quik

```bash
$ singularity exec <container> /usr/local/bin/mfold_quik
$ podman run --it --rm --entrypoint /usr/local/bin/mfold_quik   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mfold_quik   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myps2img.bash

```bash
$ singularity exec <container> /usr/local/bin/myps2img.bash
$ podman run --it --rm --entrypoint /usr/local/bin/myps2img.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myps2img.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myps2jpg.bash

```bash
$ singularity exec <container> /usr/local/bin/myps2jpg.bash
$ podman run --it --rm --entrypoint /usr/local/bin/myps2jpg.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myps2jpg.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myps2pdf.bash

```bash
$ singularity exec <container> /usr/local/bin/myps2pdf.bash
$ podman run --it --rm --entrypoint /usr/local/bin/myps2pdf.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myps2pdf.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### myps2png.bash

```bash
$ singularity exec <container> /usr/local/bin/myps2png.bash
$ podman run --it --rm --entrypoint /usr/local/bin/myps2png.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/myps2png.bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nafold

```bash
$ singularity exec <container> /usr/local/bin/nafold
$ podman run --it --rm --entrypoint /usr/local/bin/nafold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nafold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### newtemp

```bash
$ singularity exec <container> /usr/local/bin/newtemp
$ podman run --it --rm --entrypoint /usr/local/bin/newtemp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/newtemp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### overlay_boxplot_ng

```bash
$ singularity exec <container> /usr/local/bin/overlay_boxplot_ng
$ podman run --it --rm --entrypoint /usr/local/bin/overlay_boxplot_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/overlay_boxplot_ng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quikfold

```bash
$ singularity exec <container> /usr/local/bin/quikfold
$ podman run --it --rm --entrypoint /usr/local/bin/quikfold   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quikfold   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### reformat-seq.sh

```bash
$ singularity exec <container> /usr/local/bin/reformat-seq.sh
$ podman run --it --rm --entrypoint /usr/local/bin/reformat-seq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/reformat-seq.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sav2p_num

```bash
$ singularity exec <container> /usr/local/bin/sav2p_num
$ podman run --it --rm --entrypoint /usr/local/bin/sav2p_num   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sav2p_num   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sav2plot

```bash
$ singularity exec <container> /usr/local/bin/sav2plot
$ podman run --it --rm --entrypoint /usr/local/bin/sav2plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sav2plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scorer

```bash
$ singularity exec <container> /usr/local/bin/scorer
$ podman run --it --rm --entrypoint /usr/local/bin/scorer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scorer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sir_graph

```bash
$ singularity exec <container> /usr/local/bin/sir_graph
$ podman run --it --rm --entrypoint /usr/local/bin/sir_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sir_graph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ss_count

```bash
$ singularity exec <container> /usr/local/bin/ss_count
$ podman run --it --rm --entrypoint /usr/local/bin/ss_count   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ss_count   -v ${PWD} -w ${PWD} <container> -c " $@"
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