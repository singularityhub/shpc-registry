---
layout: container
name:  "quay.io/biocontainers/revoluzer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/revoluzer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/revoluzer/container.yaml"
updated_at: "2024-02-23 02:34:05.651519"
latest: "0.1.2--h6f67891_0"
container_url: "https://biocontainers.pro/tools/revoluzer"
aliases:
 - "amgr"
 - "anamed"
 - "comgen"
 - "compress"
 - "construct_triples"
 - "crex"
 - "deldup"
 - "dupdet"
 - "enumall"
 - "evoluzer"
 - "gdiff"
 - "grappaResultParser"
 - "ichar"
 - "identifySorting"
 - "ilp-rrrmt"
 - "intervals"
 - "its"
 - "median"
 - "mgrResultParser"
 - "normalize"
 - "nrex"
 - "phy2nex"
 - "pqplot"
 - "pqresolve"
 - "pqsplits"
 - "pqstat"
 - "revoluzer"
 - "revolver"
 - "robfould"
 - "sortVsPreserve"
 - "tdlmedian"
 - "tmrloc"
 - "treedegree"
 - "trex"
 - "distmat"
 - "uniq"
 - "test"
 - "gc"
 - "glpsol"
versions:
 - "0.1.2--h6f67891_0"
description: "singularity registry hpc automated addition for revoluzer"
config: {"url": "https://biocontainers.pro/tools/revoluzer", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for revoluzer", "latest": {"0.1.2--h6f67891_0": "sha256:3803eeb5132059e0ecdb25c7953631cdef96f7cb1f6e02e240576e5c551719c9"}, "tags": {"0.1.2--h6f67891_0": "sha256:3803eeb5132059e0ecdb25c7953631cdef96f7cb1f6e02e240576e5c551719c9"}, "docker": "quay.io/biocontainers/revoluzer", "aliases": {"amgr": "/usr/local/bin/amgr", "anamed": "/usr/local/bin/anamed", "comgen": "/usr/local/bin/comgen", "compress": "/usr/local/bin/compress", "construct_triples": "/usr/local/bin/construct_triples", "crex": "/usr/local/bin/crex", "deldup": "/usr/local/bin/deldup", "dupdet": "/usr/local/bin/dupdet", "enumall": "/usr/local/bin/enumall", "evoluzer": "/usr/local/bin/evoluzer", "gdiff": "/usr/local/bin/gdiff", "grappaResultParser": "/usr/local/bin/grappaResultParser", "ichar": "/usr/local/bin/ichar", "identifySorting": "/usr/local/bin/identifySorting", "ilp-rrrmt": "/usr/local/bin/ilp-rrrmt", "intervals": "/usr/local/bin/intervals", "its": "/usr/local/bin/its", "median": "/usr/local/bin/median", "mgrResultParser": "/usr/local/bin/mgrResultParser", "normalize": "/usr/local/bin/normalize", "nrex": "/usr/local/bin/nrex", "phy2nex": "/usr/local/bin/phy2nex", "pqplot": "/usr/local/bin/pqplot", "pqresolve": "/usr/local/bin/pqresolve", "pqsplits": "/usr/local/bin/pqsplits", "pqstat": "/usr/local/bin/pqstat", "revoluzer": "/usr/local/bin/revoluzer", "revolver": "/usr/local/bin/revolver", "robfould": "/usr/local/bin/robfould", "sortVsPreserve": "/usr/local/bin/sortVsPreserve", "tdlmedian": "/usr/local/bin/tdlmedian", "tmrloc": "/usr/local/bin/tmrloc", "treedegree": "/usr/local/bin/treedegree", "trex": "/usr/local/bin/trex", "distmat": "/usr/local/bin/distmat", "uniq": "/usr/local/bin/uniq", "test": "/usr/local/bin/test", "gc": "/usr/local/bin/gc", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/revoluzer.
singularity registry hpc automated addition for revoluzer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/revoluzer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/revoluzer:0.1.2--h6f67891_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/revoluzer/0.1.2--h6f67891_0
$ module help quay.io/biocontainers/revoluzer/0.1.2--h6f67891_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### revoluzer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### revoluzer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### revoluzer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### revoluzer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### revoluzer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### revoluzer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### amgr

```bash
$ singularity exec <container> /usr/local/bin/amgr
$ podman run --it --rm --entrypoint /usr/local/bin/amgr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/amgr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### anamed

```bash
$ singularity exec <container> /usr/local/bin/anamed
$ podman run --it --rm --entrypoint /usr/local/bin/anamed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/anamed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comgen

```bash
$ singularity exec <container> /usr/local/bin/comgen
$ podman run --it --rm --entrypoint /usr/local/bin/comgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### compress

```bash
$ singularity exec <container> /usr/local/bin/compress
$ podman run --it --rm --entrypoint /usr/local/bin/compress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/compress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### construct_triples

```bash
$ singularity exec <container> /usr/local/bin/construct_triples
$ podman run --it --rm --entrypoint /usr/local/bin/construct_triples   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/construct_triples   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crex

```bash
$ singularity exec <container> /usr/local/bin/crex
$ podman run --it --rm --entrypoint /usr/local/bin/crex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### deldup

```bash
$ singularity exec <container> /usr/local/bin/deldup
$ podman run --it --rm --entrypoint /usr/local/bin/deldup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deldup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dupdet

```bash
$ singularity exec <container> /usr/local/bin/dupdet
$ podman run --it --rm --entrypoint /usr/local/bin/dupdet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dupdet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### enumall

```bash
$ singularity exec <container> /usr/local/bin/enumall
$ podman run --it --rm --entrypoint /usr/local/bin/enumall   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/enumall   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### evoluzer

```bash
$ singularity exec <container> /usr/local/bin/evoluzer
$ podman run --it --rm --entrypoint /usr/local/bin/evoluzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/evoluzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdiff

```bash
$ singularity exec <container> /usr/local/bin/gdiff
$ podman run --it --rm --entrypoint /usr/local/bin/gdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grappaResultParser

```bash
$ singularity exec <container> /usr/local/bin/grappaResultParser
$ podman run --it --rm --entrypoint /usr/local/bin/grappaResultParser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grappaResultParser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ichar

```bash
$ singularity exec <container> /usr/local/bin/ichar
$ podman run --it --rm --entrypoint /usr/local/bin/ichar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ichar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### identifySorting

```bash
$ singularity exec <container> /usr/local/bin/identifySorting
$ podman run --it --rm --entrypoint /usr/local/bin/identifySorting   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/identifySorting   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ilp-rrrmt

```bash
$ singularity exec <container> /usr/local/bin/ilp-rrrmt
$ podman run --it --rm --entrypoint /usr/local/bin/ilp-rrrmt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ilp-rrrmt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### intervals

```bash
$ singularity exec <container> /usr/local/bin/intervals
$ podman run --it --rm --entrypoint /usr/local/bin/intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/intervals   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### its

```bash
$ singularity exec <container> /usr/local/bin/its
$ podman run --it --rm --entrypoint /usr/local/bin/its   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/its   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### median

```bash
$ singularity exec <container> /usr/local/bin/median
$ podman run --it --rm --entrypoint /usr/local/bin/median   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/median   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mgrResultParser

```bash
$ singularity exec <container> /usr/local/bin/mgrResultParser
$ podman run --it --rm --entrypoint /usr/local/bin/mgrResultParser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mgrResultParser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalize

```bash
$ singularity exec <container> /usr/local/bin/normalize
$ podman run --it --rm --entrypoint /usr/local/bin/normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nrex

```bash
$ singularity exec <container> /usr/local/bin/nrex
$ podman run --it --rm --entrypoint /usr/local/bin/nrex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nrex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phy2nex

```bash
$ singularity exec <container> /usr/local/bin/phy2nex
$ podman run --it --rm --entrypoint /usr/local/bin/phy2nex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phy2nex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pqplot

```bash
$ singularity exec <container> /usr/local/bin/pqplot
$ podman run --it --rm --entrypoint /usr/local/bin/pqplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pqplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pqresolve

```bash
$ singularity exec <container> /usr/local/bin/pqresolve
$ podman run --it --rm --entrypoint /usr/local/bin/pqresolve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pqresolve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pqsplits

```bash
$ singularity exec <container> /usr/local/bin/pqsplits
$ podman run --it --rm --entrypoint /usr/local/bin/pqsplits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pqsplits   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pqstat

```bash
$ singularity exec <container> /usr/local/bin/pqstat
$ podman run --it --rm --entrypoint /usr/local/bin/pqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### revoluzer

```bash
$ singularity exec <container> /usr/local/bin/revoluzer
$ podman run --it --rm --entrypoint /usr/local/bin/revoluzer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/revoluzer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### revolver

```bash
$ singularity exec <container> /usr/local/bin/revolver
$ podman run --it --rm --entrypoint /usr/local/bin/revolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/revolver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### robfould

```bash
$ singularity exec <container> /usr/local/bin/robfould
$ podman run --it --rm --entrypoint /usr/local/bin/robfould   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/robfould   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortVsPreserve

```bash
$ singularity exec <container> /usr/local/bin/sortVsPreserve
$ podman run --it --rm --entrypoint /usr/local/bin/sortVsPreserve   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortVsPreserve   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tdlmedian

```bash
$ singularity exec <container> /usr/local/bin/tdlmedian
$ podman run --it --rm --entrypoint /usr/local/bin/tdlmedian   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tdlmedian   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tmrloc

```bash
$ singularity exec <container> /usr/local/bin/tmrloc
$ podman run --it --rm --entrypoint /usr/local/bin/tmrloc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tmrloc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treedegree

```bash
$ singularity exec <container> /usr/local/bin/treedegree
$ podman run --it --rm --entrypoint /usr/local/bin/treedegree   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treedegree   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trex

```bash
$ singularity exec <container> /usr/local/bin/trex
$ podman run --it --rm --entrypoint /usr/local/bin/trex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### distmat

```bash
$ singularity exec <container> /usr/local/bin/distmat
$ podman run --it --rm --entrypoint /usr/local/bin/distmat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/distmat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq

```bash
$ singularity exec <container> /usr/local/bin/uniq
$ podman run --it --rm --entrypoint /usr/local/bin/uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test

```bash
$ singularity exec <container> /usr/local/bin/test
$ podman run --it --rm --entrypoint /usr/local/bin/test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gc

```bash
$ singularity exec <container> /usr/local/bin/gc
$ podman run --it --rm --entrypoint /usr/local/bin/gc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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