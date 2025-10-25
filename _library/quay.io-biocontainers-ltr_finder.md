---
layout: container
name:  "quay.io/biocontainers/ltr_finder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ltr_finder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ltr_finder/container.yaml"
updated_at: "2025-10-25 03:09:28.121588"
latest: "1.07--h9948957_5"
container_url: "https://biocontainers.pro/tools/ltr_finder"
aliases:
 - "check_result.pl"
 - "down_tRNA.pl"
 - "filter_rt.pl"
 - "genome_plot.pl"
 - "genome_plot2.pl"
 - "genome_plot_svg.pl"
 - "ltr_finder"
 - "psearch"
 - "bdf2gdfont.pl"
 - "bdftogd"
 - "gd2copypal"
 - "gd2togif"
 - "gd2topng"
 - "gdcmpgif"
 - "gdparttopng"
 - "gdtopng"
 - "giftogd2"
 - "pngtogd"
versions:
 - "1.07--h9f5acd7_2"
 - "1.07--h4ac6f70_3"
 - "1.07--h9948957_4"
 - "1.07--h9948957_5"
description: "shpc-registry automated BioContainers addition for ltr_finder"
config: {"url": "https://biocontainers.pro/tools/ltr_finder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ltr_finder", "latest": {"1.07--h9948957_5": "sha256:73ddadae3f447bd8486fa78ba1116b64c044029c3cd80f3cadb85c1de3a887e7"}, "tags": {"1.07--h9f5acd7_2": "sha256:04062fd669ff8c2f6dc9dbaffecdb6dec5ce9e555c929ecc1c6c2f81cc69d309", "1.07--h4ac6f70_3": "sha256:81ad6d01a96bddd5467dbab72d5d7592b6a90c24ca99b45c3e1219c0015e5db7", "1.07--h9948957_4": "sha256:5511a84df07ed32a9196ee861e8f5b3a1de321eb31515de0759dc0af6920dc4f", "1.07--h9948957_5": "sha256:73ddadae3f447bd8486fa78ba1116b64c044029c3cd80f3cadb85c1de3a887e7"}, "docker": "quay.io/biocontainers/ltr_finder", "aliases": {"check_result.pl": "/usr/local/bin/check_result.pl", "down_tRNA.pl": "/usr/local/bin/down_tRNA.pl", "filter_rt.pl": "/usr/local/bin/filter_rt.pl", "genome_plot.pl": "/usr/local/bin/genome_plot.pl", "genome_plot2.pl": "/usr/local/bin/genome_plot2.pl", "genome_plot_svg.pl": "/usr/local/bin/genome_plot_svg.pl", "ltr_finder": "/usr/local/bin/ltr_finder", "psearch": "/usr/local/bin/psearch", "bdf2gdfont.pl": "/usr/local/bin/bdf2gdfont.pl", "bdftogd": "/usr/local/bin/bdftogd", "gd2copypal": "/usr/local/bin/gd2copypal", "gd2togif": "/usr/local/bin/gd2togif", "gd2topng": "/usr/local/bin/gd2topng", "gdcmpgif": "/usr/local/bin/gdcmpgif", "gdparttopng": "/usr/local/bin/gdparttopng", "gdtopng": "/usr/local/bin/gdtopng", "giftogd2": "/usr/local/bin/giftogd2", "pngtogd": "/usr/local/bin/pngtogd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ltr_finder.
shpc-registry automated BioContainers addition for ltr_finder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ltr_finder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ltr_finder:1.07--h9948957_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ltr_finder/1.07--h9948957_5
$ module help quay.io/biocontainers/ltr_finder/1.07--h9948957_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ltr_finder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ltr_finder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ltr_finder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ltr_finder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ltr_finder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ltr_finder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check_result.pl

```bash
$ singularity exec <container> /usr/local/bin/check_result.pl
$ podman run --it --rm --entrypoint /usr/local/bin/check_result.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check_result.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### down_tRNA.pl

```bash
$ singularity exec <container> /usr/local/bin/down_tRNA.pl
$ podman run --it --rm --entrypoint /usr/local/bin/down_tRNA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/down_tRNA.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter_rt.pl

```bash
$ singularity exec <container> /usr/local/bin/filter_rt.pl
$ podman run --it --rm --entrypoint /usr/local/bin/filter_rt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter_rt.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/genome_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genome_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_plot2.pl

```bash
$ singularity exec <container> /usr/local/bin/genome_plot2.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genome_plot2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_plot2.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_plot_svg.pl

```bash
$ singularity exec <container> /usr/local/bin/genome_plot_svg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/genome_plot_svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_plot_svg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ltr_finder

```bash
$ singularity exec <container> /usr/local/bin/ltr_finder
$ podman run --it --rm --entrypoint /usr/local/bin/ltr_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ltr_finder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psearch

```bash
$ singularity exec <container> /usr/local/bin/psearch
$ podman run --it --rm --entrypoint /usr/local/bin/psearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdf2gdfont.pl

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bdftogd

```bash
$ singularity exec <container> /usr/local/bin/bdftogd
$ podman run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdftogd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2copypal

```bash
$ singularity exec <container> /usr/local/bin/gd2copypal
$ podman run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2copypal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2togif

```bash
$ singularity exec <container> /usr/local/bin/gd2togif
$ podman run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2togif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gd2topng

```bash
$ singularity exec <container> /usr/local/bin/gd2topng
$ podman run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gd2topng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdcmpgif

```bash
$ singularity exec <container> /usr/local/bin/gdcmpgif
$ podman run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdcmpgif   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdparttopng

```bash
$ singularity exec <container> /usr/local/bin/gdparttopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdparttopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdtopng

```bash
$ singularity exec <container> /usr/local/bin/gdtopng
$ podman run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdtopng   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### giftogd2

```bash
$ singularity exec <container> /usr/local/bin/giftogd2
$ podman run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/giftogd2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pngtogd

```bash
$ singularity exec <container> /usr/local/bin/pngtogd
$ podman run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pngtogd   -v ${PWD} -w ${PWD} <container> -c " $@"
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