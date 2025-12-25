---
layout: container
name:  "quay.io/biocontainers/metaplatanus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metaplatanus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/metaplatanus/container.yaml"
updated_at: "2025-12-25 04:03:05.060551"
latest: "1.3.1--h6a68c12_1"
container_url: "https://biocontainers.pro/tools/metaplatanus"
aliases:
 - "aggregateBinDepths.pl"
 - "aggregateContigOverlapsByBin.pl"
 - "contigOverlaps"
 - "file"
 - "gunzip"
 - "gzexe"
 - "gzip"
 - "jgi_summarize_bam_contig_depths"
 - "merge_depths.pl"
 - "metabat"
 - "metabat1"
 - "metabat2"
 - "metaplatanus"
 - "runMetaBat.sh"
 - "tgsgapcloser"
 - "tgsgapcloser_mod"
 - "uncompress"
 - "zcat"
 - "zcmp"
 - "zdiff"
 - "zegrep"
 - "zfgrep"
 - "zforce"
 - "zgrep"
 - "zmore"
 - "znew"
 - "2to3-3.11"
 - "idle3.11"
 - "megahit_core"
 - "megahit_core_no_hw_accel"
 - "megahit_core_popcnt"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "megahit"
 - "megahit_toolkit"
 - "seqkit"
 - "racon"
 - "rampler"
 - "racon_wrapper"
 - "sdust"
 - "paftools.js"
 - "minimap2"
 - "k8"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
 - "fasta-sanitize.pl"
 - "plot-ampliconstats"
 - "ace2sam"
 - "blast2sam.pl"
versions:
 - "1.3.1--hf1761c0_0"
 - "1.3.1--h6a68c12_1"
description: "singularity registry hpc automated addition for metaplatanus"
config: {"url": "https://biocontainers.pro/tools/metaplatanus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for metaplatanus", "latest": {"1.3.1--h6a68c12_1": "sha256:42419497b64f33207342c04909feb5b879ad7322a1b433faf982fc70a66cc120"}, "tags": {"1.3.1--hf1761c0_0": "sha256:2da93a556e67b9da7184b59996bb2a229eadb5223aa256ee16008a800a367250", "1.3.1--h6a68c12_1": "sha256:42419497b64f33207342c04909feb5b879ad7322a1b433faf982fc70a66cc120"}, "docker": "quay.io/biocontainers/metaplatanus", "aliases": {"aggregateBinDepths.pl": "/usr/local/bin/aggregateBinDepths.pl", "aggregateContigOverlapsByBin.pl": "/usr/local/bin/aggregateContigOverlapsByBin.pl", "contigOverlaps": "/usr/local/bin/contigOverlaps", "file": "/usr/local/bin/file", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "jgi_summarize_bam_contig_depths": "/usr/local/bin/jgi_summarize_bam_contig_depths", "merge_depths.pl": "/usr/local/bin/merge_depths.pl", "metabat": "/usr/local/bin/metabat", "metabat1": "/usr/local/bin/metabat1", "metabat2": "/usr/local/bin/metabat2", "metaplatanus": "/usr/local/bin/metaplatanus", "runMetaBat.sh": "/usr/local/bin/runMetaBat.sh", "tgsgapcloser": "/usr/local/bin/tgsgapcloser", "tgsgapcloser_mod": "/usr/local/bin/tgsgapcloser_mod", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "megahit_core": "/usr/local/bin/megahit_core", "megahit_core_no_hw_accel": "/usr/local/bin/megahit_core_no_hw_accel", "megahit_core_popcnt": "/usr/local/bin/megahit_core_popcnt", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "megahit": "/usr/local/bin/megahit", "megahit_toolkit": "/usr/local/bin/megahit_toolkit", "seqkit": "/usr/local/bin/seqkit", "racon": "/usr/local/bin/racon", "rampler": "/usr/local/bin/rampler", "racon_wrapper": "/usr/local/bin/racon_wrapper", "sdust": "/usr/local/bin/sdust", "paftools.js": "/usr/local/bin/paftools.js", "minimap2": "/usr/local/bin/minimap2", "k8": "/usr/local/bin/k8", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa", "fasta-sanitize.pl": "/usr/local/bin/fasta-sanitize.pl", "plot-ampliconstats": "/usr/local/bin/plot-ampliconstats", "ace2sam": "/usr/local/bin/ace2sam", "blast2sam.pl": "/usr/local/bin/blast2sam.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metaplatanus.
singularity registry hpc automated addition for metaplatanus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metaplatanus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metaplatanus:1.3.1--h6a68c12_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metaplatanus/1.3.1--h6a68c12_1
$ module help quay.io/biocontainers/metaplatanus/1.3.1--h6a68c12_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metaplatanus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metaplatanus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metaplatanus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metaplatanus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metaplatanus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metaplatanus-inspect-deffile:

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


#### file

```bash
$ singularity exec <container> /usr/local/bin/file
$ podman run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/file   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gunzip

```bash
$ singularity exec <container> /usr/local/bin/gunzip
$ podman run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzexe

```bash
$ singularity exec <container> /usr/local/bin/gzexe
$ podman run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzexe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gzip

```bash
$ singularity exec <container> /usr/local/bin/gzip
$ podman run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### metaplatanus

```bash
$ singularity exec <container> /usr/local/bin/metaplatanus
$ podman run --it --rm --entrypoint /usr/local/bin/metaplatanus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metaplatanus   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runMetaBat.sh

```bash
$ singularity exec <container> /usr/local/bin/runMetaBat.sh
$ podman run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runMetaBat.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tgsgapcloser

```bash
$ singularity exec <container> /usr/local/bin/tgsgapcloser
$ podman run --it --rm --entrypoint /usr/local/bin/tgsgapcloser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tgsgapcloser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tgsgapcloser_mod

```bash
$ singularity exec <container> /usr/local/bin/tgsgapcloser_mod
$ podman run --it --rm --entrypoint /usr/local/bin/tgsgapcloser_mod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tgsgapcloser_mod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uncompress

```bash
$ singularity exec <container> /usr/local/bin/uncompress
$ podman run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uncompress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcat

```bash
$ singularity exec <container> /usr/local/bin/zcat
$ podman run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zcmp

```bash
$ singularity exec <container> /usr/local/bin/zcmp
$ podman run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zcmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zdiff

```bash
$ singularity exec <container> /usr/local/bin/zdiff
$ podman run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zegrep

```bash
$ singularity exec <container> /usr/local/bin/zegrep
$ podman run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zegrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zfgrep

```bash
$ singularity exec <container> /usr/local/bin/zfgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zfgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zforce

```bash
$ singularity exec <container> /usr/local/bin/zforce
$ podman run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zforce   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zgrep

```bash
$ singularity exec <container> /usr/local/bin/zgrep
$ podman run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zmore

```bash
$ singularity exec <container> /usr/local/bin/zmore
$ podman run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zmore   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### znew

```bash
$ singularity exec <container> /usr/local/bin/znew
$ podman run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/znew   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### megahit_core

```bash
$ singularity exec <container> /usr/local/bin/megahit_core
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_no_hw_accel

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_no_hw_accel
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_no_hw_accel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_core_popcnt

```bash
$ singularity exec <container> /usr/local/bin/megahit_core_popcnt
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_core_popcnt   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### megahit

```bash
$ singularity exec <container> /usr/local/bin/megahit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### megahit_toolkit

```bash
$ singularity exec <container> /usr/local/bin/megahit_toolkit
$ podman run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/megahit_toolkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon

```bash
$ singularity exec <container> /usr/local/bin/racon
$ podman run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rampler

```bash
$ singularity exec <container> /usr/local/bin/rampler
$ podman run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rampler   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### racon_wrapper

```bash
$ singularity exec <container> /usr/local/bin/racon_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/racon_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sdust

```bash
$ singularity exec <container> /usr/local/bin/sdust
$ podman run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paftools.js

```bash
$ singularity exec <container> /usr/local/bin/paftools.js
$ podman run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paftools.js   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minimap2

```bash
$ singularity exec <container> /usr/local/bin/minimap2
$ podman run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minimap2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fasta-sanitize.pl

```bash
$ singularity exec <container> /usr/local/bin/fasta-sanitize.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta-sanitize.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### plot-ampliconstats

```bash
$ singularity exec <container> /usr/local/bin/plot-ampliconstats
$ podman run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/plot-ampliconstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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