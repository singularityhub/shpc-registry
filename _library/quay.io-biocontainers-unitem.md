---
layout: container
name:  "quay.io/biocontainers/unitem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/unitem/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/unitem/container.yaml"
updated_at: "2022-10-29 05:39:10.861540"
latest: "1.2.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/unitem"
aliases:
 - "aggregateBinDepths.pl"
 - "aggregateContigOverlapsByBin.pl"
 - "contigOverlaps"
 - "jgi_summarize_bam_contig_depths"
 - "merge_depths.pl"
 - "metabat"
 - "metabat1"
 - "metabat2"
 - "runMetaBat.sh"
 - "run_MaxBin.pl"
 - "unitem"
 - "2to3-3.9"
 - "FragGeneScan"
 - "Makefile"
 - "Makefile.am"
 - "Makefile.in"
 - "aclocal.bak"
 - "alimask"
 - "autoheader.bak"
 - "autom4te.bak"
 - "automake.bak"
versions:
 - "1.2.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for unitem"
config: {"url": "https://biocontainers.pro/tools/unitem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for unitem", "latest": {"1.2.1--pyhdfd78af_0": "sha256:f91f000bbe2867fd260df8f34421d4c2941c00d05fd3e48fafaf43f5c8e20d64"}, "tags": {"1.2.1--pyhdfd78af_0": "sha256:f91f000bbe2867fd260df8f34421d4c2941c00d05fd3e48fafaf43f5c8e20d64"}, "docker": "quay.io/biocontainers/unitem", "aliases": {"aggregateBinDepths.pl": "/usr/local/bin/aggregateBinDepths.pl", "aggregateContigOverlapsByBin.pl": "/usr/local/bin/aggregateContigOverlapsByBin.pl", "contigOverlaps": "/usr/local/bin/contigOverlaps", "jgi_summarize_bam_contig_depths": "/usr/local/bin/jgi_summarize_bam_contig_depths", "merge_depths.pl": "/usr/local/bin/merge_depths.pl", "metabat": "/usr/local/bin/metabat", "metabat1": "/usr/local/bin/metabat1", "metabat2": "/usr/local/bin/metabat2", "runMetaBat.sh": "/usr/local/bin/runMetaBat.sh", "run_MaxBin.pl": "/usr/local/bin/run_MaxBin.pl", "unitem": "/usr/local/bin/unitem", "2to3-3.9": "/usr/local/bin/2to3-3.9", "FragGeneScan": "/usr/local/bin/FragGeneScan", "Makefile": "/usr/local/bin/Makefile", "Makefile.am": "/usr/local/bin/Makefile.am", "Makefile.in": "/usr/local/bin/Makefile.in", "aclocal.bak": "/usr/local/bin/aclocal.bak", "alimask": "/usr/local/bin/alimask", "autoheader.bak": "/usr/local/bin/autoheader.bak", "autom4te.bak": "/usr/local/bin/autom4te.bak", "automake.bak": "/usr/local/bin/automake.bak"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/unitem.
shpc-registry automated BioContainers addition for unitem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/unitem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/unitem:1.2.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/unitem/1.2.1--pyhdfd78af_0
$ module help quay.io/biocontainers/unitem/1.2.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### unitem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### unitem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### unitem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### unitem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### unitem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### unitem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aggregateBinDepths.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateBinDepths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateBinDepths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregateContigOverlapsByBin.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregateContigOverlapsByBin.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregateContigOverlapsByBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contigOverlaps

```bash
$ singularity exec <container> /usr/local/bin/contigOverlaps
$ podman run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contigOverlaps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jgi_summarize_bam_contig_depths

```bash
$ singularity exec <container> /usr/local/bin/jgi_summarize_bam_contig_depths
$ podman run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jgi_summarize_bam_contig_depths   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_depths.pl

```bash
$ singularity exec <container> /usr/local/bin/merge_depths.pl
$ podman run --it --rm --entrypoint /usr/local/bin/merge_depths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_depths.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat

```bash
$ singularity exec <container> /usr/local/bin/metabat
$ podman run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat1

```bash
$ singularity exec <container> /usr/local/bin/metabat1
$ podman run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### metabat2

```bash
$ singularity exec <container> /usr/local/bin/metabat2
$ podman run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metabat2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMetaBat.sh

```bash
$ singularity exec <container> /usr/local/bin/runMetaBat.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_MaxBin.pl

```bash
$ singularity exec <container> /usr/local/bin/run_MaxBin.pl
$ podman run --it --rm --entrypoint /usr/local/bin/run_MaxBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_MaxBin.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unitem

```bash
$ singularity exec <container> /usr/local/bin/unitem
$ podman run --it --rm --entrypoint /usr/local/bin/unitem   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unitem   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### FragGeneScan

```bash
$ singularity exec <container> /usr/local/bin/FragGeneScan
$ podman run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/FragGeneScan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Makefile

```bash
$ singularity exec <container> /usr/local/bin/Makefile
$ podman run --it --rm --entrypoint /usr/local/bin/Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Makefile.am

```bash
$ singularity exec <container> /usr/local/bin/Makefile.am
$ podman run --it --rm --entrypoint /usr/local/bin/Makefile.am   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Makefile.am   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### Makefile.in

```bash
$ singularity exec <container> /usr/local/bin/Makefile.in
$ podman run --it --rm --entrypoint /usr/local/bin/Makefile.in   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Makefile.in   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aclocal.bak

```bash
$ singularity exec <container> /usr/local/bin/aclocal.bak
$ podman run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aclocal.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autoheader.bak

```bash
$ singularity exec <container> /usr/local/bin/autoheader.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autoheader.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### autom4te.bak

```bash
$ singularity exec <container> /usr/local/bin/autom4te.bak
$ podman run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/autom4te.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### automake.bak

```bash
$ singularity exec <container> /usr/local/bin/automake.bak
$ podman run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/automake.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
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