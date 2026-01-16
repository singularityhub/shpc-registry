---
layout: container
name:  "quay.io/biocontainers/votuderep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/votuderep/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/votuderep/container.yaml"
updated_at: "2026-01-16 04:10:00.763918"
latest: "0.6.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/votuderep"
aliases:
 - "SeqCountHelper"
 - "byteshift"
 - "dadaist2-mergeseqs"
 - "fu-16Sregion"
 - "fu-cov"
 - "fu-homocomp"
 - "fu-index"
 - "fu-msa"
 - "fu-multirelabel"
 - "fu-nanotags"
 - "fu-orf"
 - "fu-pecheck"
 - "fu-primers"
 - "fu-readtope"
 - "fu-secheck"
 - "fu-shred"
 - "fu-split"
 - "fu-sw"
 - "fu-tabcheck"
 - "fu-virfilter"
 - "seqfu"
 - "votuderep"
 - "archive-nlmnlp"
 - "archive-pids"
 - "download-flatfile"
 - "ecollect"
 - "gbf2facds"
 - "gbf2tbl"
 - "gff-sort"
 - "gff2xml"
 - "pair-at-a-time"
 - "print-missing-subranges"
 - "sort-by-length"
 - "xcommon.sh"
 - "xfetch"
 - "xfetch.ini"
 - "xfilter"
 - "xinfo"
 - "xlink"
 - "xlink.ini"
 - "xsearch"
 - "pyfastx"
 - "rich-click"
 - "bsmp2info"
 - "fsa2xml"
 - "gbf2info"
 - "just-top-hits"
versions:
 - "0.6.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for votuderep"
config: {"url": "https://biocontainers.pro/tools/votuderep", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for votuderep", "latest": {"0.6.0--pyhdfd78af_0": "sha256:b852ebc1846d7c9642adce43d9bbb193f3d2cb3547e6d90b6a9e62f25e857ca2"}, "tags": {"0.6.0--pyhdfd78af_0": "sha256:b852ebc1846d7c9642adce43d9bbb193f3d2cb3547e6d90b6a9e62f25e857ca2"}, "docker": "quay.io/biocontainers/votuderep", "aliases": {"SeqCountHelper": "/usr/local/bin/SeqCountHelper", "byteshift": "/usr/local/bin/byteshift", "dadaist2-mergeseqs": "/usr/local/bin/dadaist2-mergeseqs", "fu-16Sregion": "/usr/local/bin/fu-16Sregion", "fu-cov": "/usr/local/bin/fu-cov", "fu-homocomp": "/usr/local/bin/fu-homocomp", "fu-index": "/usr/local/bin/fu-index", "fu-msa": "/usr/local/bin/fu-msa", "fu-multirelabel": "/usr/local/bin/fu-multirelabel", "fu-nanotags": "/usr/local/bin/fu-nanotags", "fu-orf": "/usr/local/bin/fu-orf", "fu-pecheck": "/usr/local/bin/fu-pecheck", "fu-primers": "/usr/local/bin/fu-primers", "fu-readtope": "/usr/local/bin/fu-readtope", "fu-secheck": "/usr/local/bin/fu-secheck", "fu-shred": "/usr/local/bin/fu-shred", "fu-split": "/usr/local/bin/fu-split", "fu-sw": "/usr/local/bin/fu-sw", "fu-tabcheck": "/usr/local/bin/fu-tabcheck", "fu-virfilter": "/usr/local/bin/fu-virfilter", "seqfu": "/usr/local/bin/seqfu", "votuderep": "/usr/local/bin/votuderep", "archive-nlmnlp": "/usr/local/bin/archive-nlmnlp", "archive-pids": "/usr/local/bin/archive-pids", "download-flatfile": "/usr/local/bin/download-flatfile", "ecollect": "/usr/local/bin/ecollect", "gbf2facds": "/usr/local/bin/gbf2facds", "gbf2tbl": "/usr/local/bin/gbf2tbl", "gff-sort": "/usr/local/bin/gff-sort", "gff2xml": "/usr/local/bin/gff2xml", "pair-at-a-time": "/usr/local/bin/pair-at-a-time", "print-missing-subranges": "/usr/local/bin/print-missing-subranges", "sort-by-length": "/usr/local/bin/sort-by-length", "xcommon.sh": "/usr/local/bin/xcommon.sh", "xfetch": "/usr/local/bin/xfetch", "xfetch.ini": "/usr/local/bin/xfetch.ini", "xfilter": "/usr/local/bin/xfilter", "xinfo": "/usr/local/bin/xinfo", "xlink": "/usr/local/bin/xlink", "xlink.ini": "/usr/local/bin/xlink.ini", "xsearch": "/usr/local/bin/xsearch", "pyfastx": "/usr/local/bin/pyfastx", "rich-click": "/usr/local/bin/rich-click", "bsmp2info": "/usr/local/bin/bsmp2info", "fsa2xml": "/usr/local/bin/fsa2xml", "gbf2info": "/usr/local/bin/gbf2info", "just-top-hits": "/usr/local/bin/just-top-hits"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/votuderep.
singularity registry hpc automated addition for votuderep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/votuderep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/votuderep:0.6.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/votuderep/0.6.0--pyhdfd78af_0
$ module help quay.io/biocontainers/votuderep/0.6.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### votuderep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### votuderep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### votuderep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### votuderep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### votuderep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### votuderep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SeqCountHelper

```bash
$ singularity exec <container> /usr/local/bin/SeqCountHelper
$ podman run --it --rm --entrypoint /usr/local/bin/SeqCountHelper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SeqCountHelper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### byteshift

```bash
$ singularity exec <container> /usr/local/bin/byteshift
$ podman run --it --rm --entrypoint /usr/local/bin/byteshift   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/byteshift   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dadaist2-mergeseqs

```bash
$ singularity exec <container> /usr/local/bin/dadaist2-mergeseqs
$ podman run --it --rm --entrypoint /usr/local/bin/dadaist2-mergeseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dadaist2-mergeseqs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-16Sregion

```bash
$ singularity exec <container> /usr/local/bin/fu-16Sregion
$ podman run --it --rm --entrypoint /usr/local/bin/fu-16Sregion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-16Sregion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-cov

```bash
$ singularity exec <container> /usr/local/bin/fu-cov
$ podman run --it --rm --entrypoint /usr/local/bin/fu-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-cov   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-homocomp

```bash
$ singularity exec <container> /usr/local/bin/fu-homocomp
$ podman run --it --rm --entrypoint /usr/local/bin/fu-homocomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-homocomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-index

```bash
$ singularity exec <container> /usr/local/bin/fu-index
$ podman run --it --rm --entrypoint /usr/local/bin/fu-index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-msa

```bash
$ singularity exec <container> /usr/local/bin/fu-msa
$ podman run --it --rm --entrypoint /usr/local/bin/fu-msa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-msa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-multirelabel

```bash
$ singularity exec <container> /usr/local/bin/fu-multirelabel
$ podman run --it --rm --entrypoint /usr/local/bin/fu-multirelabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-multirelabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-nanotags

```bash
$ singularity exec <container> /usr/local/bin/fu-nanotags
$ podman run --it --rm --entrypoint /usr/local/bin/fu-nanotags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-nanotags   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-orf

```bash
$ singularity exec <container> /usr/local/bin/fu-orf
$ podman run --it --rm --entrypoint /usr/local/bin/fu-orf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-orf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-pecheck

```bash
$ singularity exec <container> /usr/local/bin/fu-pecheck
$ podman run --it --rm --entrypoint /usr/local/bin/fu-pecheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-pecheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-primers

```bash
$ singularity exec <container> /usr/local/bin/fu-primers
$ podman run --it --rm --entrypoint /usr/local/bin/fu-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-primers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-readtope

```bash
$ singularity exec <container> /usr/local/bin/fu-readtope
$ podman run --it --rm --entrypoint /usr/local/bin/fu-readtope   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-readtope   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-secheck

```bash
$ singularity exec <container> /usr/local/bin/fu-secheck
$ podman run --it --rm --entrypoint /usr/local/bin/fu-secheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-secheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-shred

```bash
$ singularity exec <container> /usr/local/bin/fu-shred
$ podman run --it --rm --entrypoint /usr/local/bin/fu-shred   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-shred   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-split

```bash
$ singularity exec <container> /usr/local/bin/fu-split
$ podman run --it --rm --entrypoint /usr/local/bin/fu-split   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-split   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-sw

```bash
$ singularity exec <container> /usr/local/bin/fu-sw
$ podman run --it --rm --entrypoint /usr/local/bin/fu-sw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-sw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-tabcheck

```bash
$ singularity exec <container> /usr/local/bin/fu-tabcheck
$ podman run --it --rm --entrypoint /usr/local/bin/fu-tabcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-tabcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fu-virfilter

```bash
$ singularity exec <container> /usr/local/bin/fu-virfilter
$ podman run --it --rm --entrypoint /usr/local/bin/fu-virfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fu-virfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqfu

```bash
$ singularity exec <container> /usr/local/bin/seqfu
$ podman run --it --rm --entrypoint /usr/local/bin/seqfu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqfu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### votuderep

```bash
$ singularity exec <container> /usr/local/bin/votuderep
$ podman run --it --rm --entrypoint /usr/local/bin/votuderep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/votuderep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-nlmnlp

```bash
$ singularity exec <container> /usr/local/bin/archive-nlmnlp
$ podman run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-nlmnlp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### archive-pids

```bash
$ singularity exec <container> /usr/local/bin/archive-pids
$ podman run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/archive-pids   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### download-flatfile

```bash
$ singularity exec <container> /usr/local/bin/download-flatfile
$ podman run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/download-flatfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ecollect

```bash
$ singularity exec <container> /usr/local/bin/ecollect
$ podman run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ecollect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2facds

```bash
$ singularity exec <container> /usr/local/bin/gbf2facds
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2facds   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2tbl

```bash
$ singularity exec <container> /usr/local/bin/gbf2tbl
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2tbl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff-sort

```bash
$ singularity exec <container> /usr/local/bin/gff-sort
$ podman run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff-sort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2xml

```bash
$ singularity exec <container> /usr/local/bin/gff2xml
$ podman run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pair-at-a-time

```bash
$ singularity exec <container> /usr/local/bin/pair-at-a-time
$ podman run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pair-at-a-time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### print-missing-subranges

```bash
$ singularity exec <container> /usr/local/bin/print-missing-subranges
$ podman run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/print-missing-subranges   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sort-by-length

```bash
$ singularity exec <container> /usr/local/bin/sort-by-length
$ podman run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sort-by-length   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xcommon.sh

```bash
$ singularity exec <container> /usr/local/bin/xcommon.sh
$ podman run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xcommon.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch

```bash
$ singularity exec <container> /usr/local/bin/xfetch
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfetch.ini

```bash
$ singularity exec <container> /usr/local/bin/xfetch.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfetch.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xfilter

```bash
$ singularity exec <container> /usr/local/bin/xfilter
$ podman run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xfilter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xinfo

```bash
$ singularity exec <container> /usr/local/bin/xinfo
$ podman run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xinfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink

```bash
$ singularity exec <container> /usr/local/bin/xlink
$ podman run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xlink.ini

```bash
$ singularity exec <container> /usr/local/bin/xlink.ini
$ podman run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xlink.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsearch

```bash
$ singularity exec <container> /usr/local/bin/xsearch
$ podman run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyfastx

```bash
$ singularity exec <container> /usr/local/bin/pyfastx
$ podman run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyfastx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rich-click

```bash
$ singularity exec <container> /usr/local/bin/rich-click
$ podman run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rich-click   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsmp2info

```bash
$ singularity exec <container> /usr/local/bin/bsmp2info
$ podman run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsmp2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fsa2xml

```bash
$ singularity exec <container> /usr/local/bin/fsa2xml
$ podman run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fsa2xml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gbf2info

```bash
$ singularity exec <container> /usr/local/bin/gbf2info
$ podman run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gbf2info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### just-top-hits

```bash
$ singularity exec <container> /usr/local/bin/just-top-hits
$ podman run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/just-top-hits   -v ${PWD} -w ${PWD} <container> -c " $@"
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