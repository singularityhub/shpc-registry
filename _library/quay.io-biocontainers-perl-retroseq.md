---
layout: container
name:  "quay.io/biocontainers/perl-retroseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-retroseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-retroseq/container.yaml"
updated_at: "2023-10-29 02:57:27.454788"
latest: "1.5--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-retroseq"
aliases:
 - "esd2esi"
 - "exonerate"
 - "exonerate-server"
 - "fasta2esd"
 - "fastaannotatecdna"
 - "fastachecksum"
 - "fastaclean"
 - "fastaclip"
 - "fastacomposition"
 - "fastadiff"
 - "fastaexplode"
 - "fastafetch"
 - "fastahardmask"
 - "fastaindex"
 - "fastalength"
 - "fastanrdb"
 - "fastaoverlap"
 - "fastareformat"
 - "fastaremove"
 - "fastarevcomp"
 - "fastasoftmask"
 - "fastasort"
 - "fastasplit"
 - "fastasubseq"
 - "fastatranslate"
 - "fastavalidcds"
 - "ipcress"
 - "retroseq.pl"
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
 - "bamToFastq"
 - "bed12ToBed6"
 - "bedToBam"
 - "bedToIgv"
 - "bedpeToBam"
 - "bedtools"
 - "closestBed"
 - "clusterBed"
 - "complementBed"
 - "coverageBed"
 - "expandCols"
 - "fastaFromBed"
 - "flankBed"
 - "genomeCoverageBed"
 - "getOverlap"
 - "groupBy"
 - "intersectBed"
versions:
 - "1.5--pl5321hdfd78af_0"
 - "1.5--pl5321hdfd78af_1"
description: "singularity registry hpc automated addition for perl-retroseq"
config: {"url": "https://biocontainers.pro/tools/perl-retroseq", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-retroseq", "latest": {"1.5--pl5321hdfd78af_1": "sha256:65a209445d9e44d254837d33be082a658ab698dd5c7f4fb57a0809193fd5e664"}, "tags": {"1.5--pl5321hdfd78af_0": "sha256:e52ca6f617029195434fbb599fcd00b2d96b3961262576ea1ad1c6357644692c", "1.5--pl5321hdfd78af_1": "sha256:65a209445d9e44d254837d33be082a658ab698dd5c7f4fb57a0809193fd5e664"}, "docker": "quay.io/biocontainers/perl-retroseq", "aliases": {"esd2esi": "/usr/local/bin/esd2esi", "exonerate": "/usr/local/bin/exonerate", "exonerate-server": "/usr/local/bin/exonerate-server", "fasta2esd": "/usr/local/bin/fasta2esd", "fastaannotatecdna": "/usr/local/bin/fastaannotatecdna", "fastachecksum": "/usr/local/bin/fastachecksum", "fastaclean": "/usr/local/bin/fastaclean", "fastaclip": "/usr/local/bin/fastaclip", "fastacomposition": "/usr/local/bin/fastacomposition", "fastadiff": "/usr/local/bin/fastadiff", "fastaexplode": "/usr/local/bin/fastaexplode", "fastafetch": "/usr/local/bin/fastafetch", "fastahardmask": "/usr/local/bin/fastahardmask", "fastaindex": "/usr/local/bin/fastaindex", "fastalength": "/usr/local/bin/fastalength", "fastanrdb": "/usr/local/bin/fastanrdb", "fastaoverlap": "/usr/local/bin/fastaoverlap", "fastareformat": "/usr/local/bin/fastareformat", "fastaremove": "/usr/local/bin/fastaremove", "fastarevcomp": "/usr/local/bin/fastarevcomp", "fastasoftmask": "/usr/local/bin/fastasoftmask", "fastasort": "/usr/local/bin/fastasort", "fastasplit": "/usr/local/bin/fastasplit", "fastasubseq": "/usr/local/bin/fastasubseq", "fastatranslate": "/usr/local/bin/fastatranslate", "fastavalidcds": "/usr/local/bin/fastavalidcds", "ipcress": "/usr/local/bin/ipcress", "retroseq.pl": "/usr/local/bin/retroseq.pl", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "bed12ToBed6": "/usr/local/bin/bed12ToBed6", "bedToBam": "/usr/local/bin/bedToBam", "bedToIgv": "/usr/local/bin/bedToIgv", "bedpeToBam": "/usr/local/bin/bedpeToBam", "bedtools": "/usr/local/bin/bedtools", "closestBed": "/usr/local/bin/closestBed", "clusterBed": "/usr/local/bin/clusterBed", "complementBed": "/usr/local/bin/complementBed", "coverageBed": "/usr/local/bin/coverageBed", "expandCols": "/usr/local/bin/expandCols", "fastaFromBed": "/usr/local/bin/fastaFromBed", "flankBed": "/usr/local/bin/flankBed", "genomeCoverageBed": "/usr/local/bin/genomeCoverageBed", "getOverlap": "/usr/local/bin/getOverlap", "groupBy": "/usr/local/bin/groupBy", "intersectBed": "/usr/local/bin/intersectBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-retroseq.
singularity registry hpc automated addition for perl-retroseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-retroseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-retroseq:1.5--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-retroseq/1.5--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-retroseq/1.5--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-retroseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-retroseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-retroseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-retroseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-retroseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-retroseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### esd2esi

```bash
$ singularity exec <container> /usr/local/bin/esd2esi
$ podman run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esd2esi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate

```bash
$ singularity exec <container> /usr/local/bin/exonerate
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### exonerate-server

```bash
$ singularity exec <container> /usr/local/bin/exonerate-server
$ podman run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/exonerate-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta2esd

```bash
$ singularity exec <container> /usr/local/bin/fasta2esd
$ podman run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta2esd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaannotatecdna

```bash
$ singularity exec <container> /usr/local/bin/fastaannotatecdna
$ podman run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaannotatecdna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastachecksum

```bash
$ singularity exec <container> /usr/local/bin/fastachecksum
$ podman run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastachecksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaclean

```bash
$ singularity exec <container> /usr/local/bin/fastaclean
$ podman run --it --rm --entrypoint /usr/local/bin/fastaclean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaclean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaclip

```bash
$ singularity exec <container> /usr/local/bin/fastaclip
$ podman run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastacomposition

```bash
$ singularity exec <container> /usr/local/bin/fastacomposition
$ podman run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastacomposition   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastadiff

```bash
$ singularity exec <container> /usr/local/bin/fastadiff
$ podman run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastadiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaexplode

```bash
$ singularity exec <container> /usr/local/bin/fastaexplode
$ podman run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaexplode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastafetch

```bash
$ singularity exec <container> /usr/local/bin/fastafetch
$ podman run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastafetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastahardmask

```bash
$ singularity exec <container> /usr/local/bin/fastahardmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastahardmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaindex

```bash
$ singularity exec <container> /usr/local/bin/fastaindex
$ podman run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaindex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastalength

```bash
$ singularity exec <container> /usr/local/bin/fastalength
$ podman run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastalength   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastanrdb

```bash
$ singularity exec <container> /usr/local/bin/fastanrdb
$ podman run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastanrdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaoverlap

```bash
$ singularity exec <container> /usr/local/bin/fastaoverlap
$ podman run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaoverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastareformat

```bash
$ singularity exec <container> /usr/local/bin/fastareformat
$ podman run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastareformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaremove

```bash
$ singularity exec <container> /usr/local/bin/fastaremove
$ podman run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaremove   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastarevcomp

```bash
$ singularity exec <container> /usr/local/bin/fastarevcomp
$ podman run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastarevcomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasoftmask

```bash
$ singularity exec <container> /usr/local/bin/fastasoftmask
$ podman run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasoftmask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasort

```bash
$ singularity exec <container> /usr/local/bin/fastasort
$ podman run --it --rm --entrypoint /usr/local/bin/fastasort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasplit

```bash
$ singularity exec <container> /usr/local/bin/fastasplit
$ podman run --it --rm --entrypoint /usr/local/bin/fastasplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastasubseq

```bash
$ singularity exec <container> /usr/local/bin/fastasubseq
$ podman run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastasubseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastatranslate

```bash
$ singularity exec <container> /usr/local/bin/fastatranslate
$ podman run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastatranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastavalidcds

```bash
$ singularity exec <container> /usr/local/bin/fastavalidcds
$ podman run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastavalidcds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ipcress

```bash
$ singularity exec <container> /usr/local/bin/ipcress
$ podman run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ipcress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### retroseq.pl

```bash
$ singularity exec <container> /usr/local/bin/retroseq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/retroseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/retroseq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBam

```bash
$ singularity exec <container> /usr/local/bin/bedToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToIgv

```bash
$ singularity exec <container> /usr/local/bin/bedToIgv
$ podman run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToIgv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedpeToBam

```bash
$ singularity exec <container> /usr/local/bin/bedpeToBam
$ podman run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedpeToBam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedtools

```bash
$ singularity exec <container> /usr/local/bin/bedtools
$ podman run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### closestBed

```bash
$ singularity exec <container> /usr/local/bin/closestBed
$ podman run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/closestBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clusterBed

```bash
$ singularity exec <container> /usr/local/bin/clusterBed
$ podman run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clusterBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### complementBed

```bash
$ singularity exec <container> /usr/local/bin/complementBed
$ podman run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/complementBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverageBed

```bash
$ singularity exec <container> /usr/local/bin/coverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### expandCols

```bash
$ singularity exec <container> /usr/local/bin/expandCols
$ podman run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/expandCols   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastaFromBed

```bash
$ singularity exec <container> /usr/local/bin/fastaFromBed
$ podman run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastaFromBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flankBed

```bash
$ singularity exec <container> /usr/local/bin/flankBed
$ podman run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flankBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genomeCoverageBed

```bash
$ singularity exec <container> /usr/local/bin/genomeCoverageBed
$ podman run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genomeCoverageBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getOverlap

```bash
$ singularity exec <container> /usr/local/bin/getOverlap
$ podman run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getOverlap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### groupBy

```bash
$ singularity exec <container> /usr/local/bin/groupBy
$ podman run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/groupBy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intersectBed

```bash
$ singularity exec <container> /usr/local/bin/intersectBed
$ podman run --it --rm --entrypoint /usr/local/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intersectBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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