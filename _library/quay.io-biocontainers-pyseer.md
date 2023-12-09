---
layout: container
name:  "quay.io/biocontainers/pyseer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pyseer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pyseer/container.yaml"
updated_at: "2023-12-09 03:34:50.457282"
latest: "1.3.11--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/pyseer"
aliases:
 - "annotate_hits_pyseer"
 - "enet_predict_pyseer"
 - "phandango_mapper"
 - "pyseer"
 - "scree_plot_pyseer"
 - "similarity_pyseer"
 - "square_mash"
 - "bam2bed"
 - "bam2bed-float128"
 - "bam2bed-megarow"
 - "bam2bed-typical"
 - "bam2bed_gnuParallel"
 - "bam2bed_gnuParallel-float128"
 - "bam2bed_gnuParallel-megarow"
 - "bam2bed_gnuParallel-typical"
 - "bam2bed_sge"
 - "bam2bed_sge-float128"
versions:
 - "1.3.9--pyh5e36f6f_0"
 - "1.3.10--pyh5e36f6f_0"
 - "1.3.11--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for pyseer"
config: {"url": "https://biocontainers.pro/tools/pyseer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pyseer", "latest": {"1.3.11--pyh7cba7a3_0": "sha256:03617802ba499529c6979869692d242ad67d3aac3dc1a3175e5ceb6581771410"}, "tags": {"1.3.9--pyh5e36f6f_0": "sha256:703d932e154bc3eefbfa977300987bbc14d9bfe08e2ccff6c9861b153f51801e", "1.3.10--pyh5e36f6f_0": "sha256:1db6b7b3bf8c0f2d07b434dca71a4a13a0a9b5d7e4e29c4290c20da2fdf0a65e", "1.3.11--pyh7cba7a3_0": "sha256:03617802ba499529c6979869692d242ad67d3aac3dc1a3175e5ceb6581771410"}, "docker": "quay.io/biocontainers/pyseer", "aliases": {"annotate_hits_pyseer": "/usr/local/bin/annotate_hits_pyseer", "enet_predict_pyseer": "/usr/local/bin/enet_predict_pyseer", "phandango_mapper": "/usr/local/bin/phandango_mapper", "pyseer": "/usr/local/bin/pyseer", "scree_plot_pyseer": "/usr/local/bin/scree_plot_pyseer", "similarity_pyseer": "/usr/local/bin/similarity_pyseer", "square_mash": "/usr/local/bin/square_mash", "bam2bed": "/usr/local/bin/bam2bed", "bam2bed-float128": "/usr/local/bin/bam2bed-float128", "bam2bed-megarow": "/usr/local/bin/bam2bed-megarow", "bam2bed-typical": "/usr/local/bin/bam2bed-typical", "bam2bed_gnuParallel": "/usr/local/bin/bam2bed_gnuParallel", "bam2bed_gnuParallel-float128": "/usr/local/bin/bam2bed_gnuParallel-float128", "bam2bed_gnuParallel-megarow": "/usr/local/bin/bam2bed_gnuParallel-megarow", "bam2bed_gnuParallel-typical": "/usr/local/bin/bam2bed_gnuParallel-typical", "bam2bed_sge": "/usr/local/bin/bam2bed_sge", "bam2bed_sge-float128": "/usr/local/bin/bam2bed_sge-float128"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pyseer.
shpc-registry automated BioContainers addition for pyseer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pyseer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pyseer:1.3.11--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pyseer/1.3.11--pyh7cba7a3_0
$ module help quay.io/biocontainers/pyseer/1.3.11--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pyseer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pyseer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pyseer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pyseer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pyseer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pyseer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotate_hits_pyseer

```bash
$ singularity exec <container> /usr/local/bin/annotate_hits_pyseer
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_hits_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_hits_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enet_predict_pyseer

```bash
$ singularity exec <container> /usr/local/bin/enet_predict_pyseer
$ podman run --it --rm --entrypoint /usr/local/bin/enet_predict_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enet_predict_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phandango_mapper

```bash
$ singularity exec <container> /usr/local/bin/phandango_mapper
$ podman run --it --rm --entrypoint /usr/local/bin/phandango_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phandango_mapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyseer

```bash
$ singularity exec <container> /usr/local/bin/pyseer
$ podman run --it --rm --entrypoint /usr/local/bin/pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scree_plot_pyseer

```bash
$ singularity exec <container> /usr/local/bin/scree_plot_pyseer
$ podman run --it --rm --entrypoint /usr/local/bin/scree_plot_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scree_plot_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### similarity_pyseer

```bash
$ singularity exec <container> /usr/local/bin/similarity_pyseer
$ podman run --it --rm --entrypoint /usr/local/bin/similarity_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/similarity_pyseer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### square_mash

```bash
$ singularity exec <container> /usr/local/bin/square_mash
$ podman run --it --rm --entrypoint /usr/local/bin/square_mash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/square_mash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed

```bash
$ singularity exec <container> /usr/local/bin/bam2bed
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
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