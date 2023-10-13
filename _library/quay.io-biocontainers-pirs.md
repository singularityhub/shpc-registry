---
layout: container
name:  "quay.io/biocontainers/pirs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pirs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pirs/container.yaml"
updated_at: "2023-10-13 03:11:00.695737"
latest: "2.0.2--h466657f_6"
container_url: "https://biocontainers.pro/tools/pirs"
aliases:
 - "2bwt-builder"
 - "AUTHORS"
 - "COPYING"
 - "NEWS"
 - "alignment_stator"
 - "baseCalling_Matrix_analyzer"
 - "baseCalling_Matrix_calculator"
 - "baseCalling_Matrix_merger"
 - "gc_coverage_bias"
 - "gc_coverage_bias_plot"
 - "indelstat_sam_bam"
 - "pirs"
 - "soap"
 - "soap.coverage"
 - "chrpath"
 - "gnuplot"
 - "basenc"
 - "xkbcli"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
versions:
 - "2.0.2--h466657f_6"
description: "shpc-registry automated BioContainers addition for pirs"
config: {"url": "https://biocontainers.pro/tools/pirs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pirs", "latest": {"2.0.2--h466657f_6": "sha256:159052ca3d7861da9e9c6f93f3d4c506afcf22a53d2bf3209430ea0dbf56a216"}, "tags": {"2.0.2--h466657f_6": "sha256:159052ca3d7861da9e9c6f93f3d4c506afcf22a53d2bf3209430ea0dbf56a216"}, "docker": "quay.io/biocontainers/pirs", "aliases": {"2bwt-builder": "/usr/local/bin/2bwt-builder", "AUTHORS": "/usr/local/bin/AUTHORS", "COPYING": "/usr/local/bin/COPYING", "NEWS": "/usr/local/bin/NEWS", "alignment_stator": "/usr/local/bin/alignment_stator", "baseCalling_Matrix_analyzer": "/usr/local/bin/baseCalling_Matrix_analyzer", "baseCalling_Matrix_calculator": "/usr/local/bin/baseCalling_Matrix_calculator", "baseCalling_Matrix_merger": "/usr/local/bin/baseCalling_Matrix_merger", "gc_coverage_bias": "/usr/local/bin/gc_coverage_bias", "gc_coverage_bias_plot": "/usr/local/bin/gc_coverage_bias_plot", "indelstat_sam_bam": "/usr/local/bin/indelstat_sam_bam", "pirs": "/usr/local/bin/pirs", "soap": "/usr/local/bin/soap", "soap.coverage": "/usr/local/bin/soap.coverage", "chrpath": "/usr/local/bin/chrpath", "gnuplot": "/usr/local/bin/gnuplot", "basenc": "/usr/local/bin/basenc", "xkbcli": "/usr/local/bin/xkbcli", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pirs.
shpc-registry automated BioContainers addition for pirs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pirs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pirs:2.0.2--h466657f_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pirs/2.0.2--h466657f_6
$ module help quay.io/biocontainers/pirs/2.0.2--h466657f_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pirs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pirs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pirs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pirs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pirs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pirs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2bwt-builder

```bash
$ singularity exec <container> /usr/local/bin/2bwt-builder
$ podman run --it --rm --entrypoint /usr/local/bin/2bwt-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2bwt-builder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### AUTHORS

```bash
$ singularity exec <container> /usr/local/bin/AUTHORS
$ podman run --it --rm --entrypoint /usr/local/bin/AUTHORS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/AUTHORS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### COPYING

```bash
$ singularity exec <container> /usr/local/bin/COPYING
$ podman run --it --rm --entrypoint /usr/local/bin/COPYING   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/COPYING   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### NEWS

```bash
$ singularity exec <container> /usr/local/bin/NEWS
$ podman run --it --rm --entrypoint /usr/local/bin/NEWS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NEWS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alignment_stator

```bash
$ singularity exec <container> /usr/local/bin/alignment_stator
$ podman run --it --rm --entrypoint /usr/local/bin/alignment_stator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alignment_stator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseCalling_Matrix_analyzer

```bash
$ singularity exec <container> /usr/local/bin/baseCalling_Matrix_analyzer
$ podman run --it --rm --entrypoint /usr/local/bin/baseCalling_Matrix_analyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseCalling_Matrix_analyzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseCalling_Matrix_calculator

```bash
$ singularity exec <container> /usr/local/bin/baseCalling_Matrix_calculator
$ podman run --it --rm --entrypoint /usr/local/bin/baseCalling_Matrix_calculator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseCalling_Matrix_calculator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### baseCalling_Matrix_merger

```bash
$ singularity exec <container> /usr/local/bin/baseCalling_Matrix_merger
$ podman run --it --rm --entrypoint /usr/local/bin/baseCalling_Matrix_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/baseCalling_Matrix_merger   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc_coverage_bias

```bash
$ singularity exec <container> /usr/local/bin/gc_coverage_bias
$ podman run --it --rm --entrypoint /usr/local/bin/gc_coverage_bias   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc_coverage_bias   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc_coverage_bias_plot

```bash
$ singularity exec <container> /usr/local/bin/gc_coverage_bias_plot
$ podman run --it --rm --entrypoint /usr/local/bin/gc_coverage_bias_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc_coverage_bias_plot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indelstat_sam_bam

```bash
$ singularity exec <container> /usr/local/bin/indelstat_sam_bam
$ podman run --it --rm --entrypoint /usr/local/bin/indelstat_sam_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indelstat_sam_bam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pirs

```bash
$ singularity exec <container> /usr/local/bin/pirs
$ podman run --it --rm --entrypoint /usr/local/bin/pirs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pirs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap

```bash
$ singularity exec <container> /usr/local/bin/soap
$ podman run --it --rm --entrypoint /usr/local/bin/soap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### soap.coverage

```bash
$ singularity exec <container> /usr/local/bin/soap.coverage
$ podman run --it --rm --entrypoint /usr/local/bin/soap.coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/soap.coverage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chrpath

```bash
$ singularity exec <container> /usr/local/bin/chrpath
$ podman run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chrpath   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnuplot

```bash
$ singularity exec <container> /usr/local/bin/gnuplot
$ podman run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnuplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xkbcli

```bash
$ singularity exec <container> /usr/local/bin/xkbcli
$ podman run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xkbcli   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat

```bash
$ singularity exec <container> /usr/local/bin/cat
$ podman run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chcon

```bash
$ singularity exec <container> /usr/local/bin/chcon
$ podman run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
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