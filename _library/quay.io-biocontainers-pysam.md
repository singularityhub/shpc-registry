---
layout: container
name:  "quay.io/biocontainers/pysam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pysam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pysam/container.yaml"
updated_at: "2024-11-13 03:34:36.220901"
latest: "0.22.1--py39h61809e1_2"
container_url: "https://biocontainers.pro/tools/pysam"
aliases:
 - "color-chrs.pl"
 - "plot-vcfstats"
 - "bcftools"
 - "vcfutils.pl"
 - "2to3-3.6"
 - "idle3.6"
 - "pydoc3.6"
 - "python3.6"
 - "python3.6-config"
 - "python3.6m"
versions:
 - "0.9.1--py36h92ddc84_6"
 - "0.15.2--py37h1671916_1"
 - "0.13.0--py27_htslib1.6_0"
 - "0.12.0.1--py35_htslib1.6_2"
 - "0.11.2.2--htslib1.5_2"
 - "0.10.0--py36h92ddc84_7"
 - "0.22.0--py38h15b938a_1"
 - "0.21.0--py38h15b938a_1"
 - "0.20.0--py27h7835474_0"
 - "0.19.1--py39h9abd093_1"
 - "0.18.0--py36hea1697a_2"
 - "0.22.1--py38h15b938a_0"
 - "0.22.1--py311h1f0e11c_1"
 - "0.22.1--py39h61809e1_2"
description: "shpc-registry automated BioContainers addition for pysam"
config: {"url": "https://biocontainers.pro/tools/pysam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pysam", "latest": {"0.22.1--py39h61809e1_2": "sha256:812005cdae395cff59e3ed8f7e022d760a591f080faa68ad323513ddef017e99"}, "tags": {"0.9.1--py36h92ddc84_6": "sha256:5441e9ff21e79d0ffbdfcd8c926c39be15d4ea33bb439fe948cdf198cc93fb43", "0.15.2--py37h1671916_1": "sha256:625e8741eea36e4452c87917e4cbbbd8131d0528f5264de503069815d380ff5e", "0.13.0--py27_htslib1.6_0": "sha256:e24cbb944b06f875fb2b5858106381933f608c5868f84f946aa55290c88f7b5e", "0.12.0.1--py35_htslib1.6_2": "sha256:ce2792b0b2b09c1935d70ebf7c3ad1eb03fdf62b09d88774f615a81ea19c4a61", "0.11.2.2--htslib1.5_2": "sha256:abade42e42833651552e1da960244a1da4ef56581a8f7969f7dae3d7c9a32b4b", "0.10.0--py36h92ddc84_7": "sha256:ed74b7eedfbdd56a051515542a94b0e63607145f05559522d326207f3738a4d6", "0.22.0--py38h15b938a_1": "sha256:bf1c692abbbc42c855779cd5d1f21c2bd7abd35fcc881579715dc8e2bc544df4", "0.21.0--py38h15b938a_1": "sha256:da1149bb0bd8404a06feb0847ff21d431475bcc5b9ef941938255d2737dc3f78", "0.20.0--py27h7835474_0": "sha256:e3c5885235cfe882b0b3c085c6e90cb36aa0023016ed390ac79e48b31ef48ebf", "0.19.1--py39h9abd093_1": "sha256:484905243541dc3f7d46871d9d8af26b59acb52c1cbb5105d5d0d1d6c230d308", "0.18.0--py36hea1697a_2": "sha256:91e53cb84b8a6c9c18d630e3f17743689635cb331d342c1ab94c9cb82bc95c36", "0.22.1--py38h15b938a_0": "sha256:2edb0abc5d33e892f734c0fa0e3d6ac053b22ca036b1b3e1c1a153cc6be34bd7", "0.22.1--py311h1f0e11c_1": "sha256:0afe5afd6d37f76451fef567753f169d10b4945296b53c9b924240387dd4002b", "0.22.1--py39h61809e1_2": "sha256:812005cdae395cff59e3ed8f7e022d760a591f080faa68ad323513ddef017e99"}, "docker": "quay.io/biocontainers/pysam", "aliases": {"color-chrs.pl": "/usr/local/bin/color-chrs.pl", "plot-vcfstats": "/usr/local/bin/plot-vcfstats", "bcftools": "/usr/local/bin/bcftools", "vcfutils.pl": "/usr/local/bin/vcfutils.pl", "2to3-3.6": "/usr/local/bin/2to3-3.6", "idle3.6": "/usr/local/bin/idle3.6", "pydoc3.6": "/usr/local/bin/pydoc3.6", "python3.6": "/usr/local/bin/python3.6", "python3.6-config": "/usr/local/bin/python3.6-config", "python3.6m": "/usr/local/bin/python3.6m"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pysam.
shpc-registry automated BioContainers addition for pysam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pysam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pysam:0.22.1--py39h61809e1_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pysam/0.22.1--py39h61809e1_2
$ module help quay.io/biocontainers/pysam/0.22.1--py39h61809e1_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pysam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pysam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pysam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pysam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pysam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pysam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-vcfstats

```bash
$ singularity exec <container> /usr/local/bin/plot-vcfstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-vcfstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vcfutils.pl

```bash
$ singularity exec <container> /usr/local/bin/vcfutils.pl
$ podman run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vcfutils.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.6

```bash
$ singularity exec <container> /usr/local/bin/idle3.6
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.6

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.6
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6

```bash
$ singularity exec <container> /usr/local/bin/python3.6
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6-config

```bash
$ singularity exec <container> /usr/local/bin/python3.6-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.6m

```bash
$ singularity exec <container> /usr/local/bin/python3.6m
$ podman run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.6m   -v ${PWD} -w ${PWD} <container> -c " $@"
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