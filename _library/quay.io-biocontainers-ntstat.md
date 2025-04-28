---
layout: container
name:  "quay.io/biocontainers/ntstat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ntstat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ntstat/container.yaml"
updated_at: "2025-04-28 04:25:33.719813"
latest: "1.0.1--py311he264feb_2"
container_url: "https://biocontainers.pro/tools/ntstat"
aliases:
 - "indexlr"
 - "lrunzip"
 - "lrz"
 - "lrzcat"
 - "lrzip"
 - "lrztar"
 - "lrzuntar"
 - "mi_bf_generate"
 - "ntcard"
 - "nthll"
 - "ntstat"
 - "randseq"
 - "zipcloak"
 - "zipnote"
 - "zipsplit"
 - "zip"
 - "gunzip"
 - "gzexe"
 - "gzip"
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
 - "qconvex"
 - "qdelaunay"
 - "qhalf"
 - "qhull"
 - "qvoronoi"
 - "rbox"
 - "annot-tsv"
 - "tar"
 - "numpy-config"
 - "pigz"
 - "unpigz"
versions:
 - "1.0.0--py310h84f13bb_0"
 - "1.0.1--py38h2123bcc_0"
 - "1.0.1--py312h28adbb1_1"
 - "1.0.1--py311he264feb_2"
description: "singularity registry hpc automated addition for ntstat"
config: {"url": "https://biocontainers.pro/tools/ntstat", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ntstat", "latest": {"1.0.1--py311he264feb_2": "sha256:8d96390724d19e5d837721c1b8f27c5cdf24e5dfd81804fa9b0ce487933502ea"}, "tags": {"1.0.0--py310h84f13bb_0": "sha256:3629833d95d90af321b182bf2e861e935025bb2172a7eb32397e5244cc2c275c", "1.0.1--py38h2123bcc_0": "sha256:f0a0437e6aa72480d97ad250f684d4f83edb8928e9ef370b8be63cd1d7e71476", "1.0.1--py312h28adbb1_1": "sha256:bcf5b0075a9e8088c0ccf1d82e516c96fd66c29eaacd5f77d876417da8c4c367", "1.0.1--py311he264feb_2": "sha256:8d96390724d19e5d837721c1b8f27c5cdf24e5dfd81804fa9b0ce487933502ea"}, "docker": "quay.io/biocontainers/ntstat", "aliases": {"indexlr": "/usr/local/bin/indexlr", "lrunzip": "/usr/local/bin/lrunzip", "lrz": "/usr/local/bin/lrz", "lrzcat": "/usr/local/bin/lrzcat", "lrzip": "/usr/local/bin/lrzip", "lrztar": "/usr/local/bin/lrztar", "lrzuntar": "/usr/local/bin/lrzuntar", "mi_bf_generate": "/usr/local/bin/mi_bf_generate", "ntcard": "/usr/local/bin/ntcard", "nthll": "/usr/local/bin/nthll", "ntstat": "/usr/local/bin/ntstat", "randseq": "/usr/local/bin/randseq", "zipcloak": "/usr/local/bin/zipcloak", "zipnote": "/usr/local/bin/zipnote", "zipsplit": "/usr/local/bin/zipsplit", "zip": "/usr/local/bin/zip", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "qconvex": "/usr/local/bin/qconvex", "qdelaunay": "/usr/local/bin/qdelaunay", "qhalf": "/usr/local/bin/qhalf", "qhull": "/usr/local/bin/qhull", "qvoronoi": "/usr/local/bin/qvoronoi", "rbox": "/usr/local/bin/rbox", "annot-tsv": "/usr/local/bin/annot-tsv", "tar": "/usr/local/bin/tar", "numpy-config": "/usr/local/bin/numpy-config", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ntstat.
singularity registry hpc automated addition for ntstat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ntstat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ntstat:1.0.1--py311he264feb_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ntstat/1.0.1--py311he264feb_2
$ module help quay.io/biocontainers/ntstat/1.0.1--py311he264feb_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ntstat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ntstat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ntstat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ntstat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ntstat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ntstat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### indexlr

```bash
$ singularity exec <container> /usr/local/bin/indexlr
$ podman run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrunzip

```bash
$ singularity exec <container> /usr/local/bin/lrunzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrz

```bash
$ singularity exec <container> /usr/local/bin/lrz
$ podman run --it --rm --entrypoint /usr/local/bin/lrz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzcat

```bash
$ singularity exec <container> /usr/local/bin/lrzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzip

```bash
$ singularity exec <container> /usr/local/bin/lrzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrztar

```bash
$ singularity exec <container> /usr/local/bin/lrztar
$ podman run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzuntar

```bash
$ singularity exec <container> /usr/local/bin/lrzuntar
$ podman run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mi_bf_generate

```bash
$ singularity exec <container> /usr/local/bin/mi_bf_generate
$ podman run --it --rm --entrypoint /usr/local/bin/mi_bf_generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mi_bf_generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntcard

```bash
$ singularity exec <container> /usr/local/bin/ntcard
$ podman run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntcard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nthll

```bash
$ singularity exec <container> /usr/local/bin/nthll
$ podman run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nthll   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ntstat

```bash
$ singularity exec <container> /usr/local/bin/ntstat
$ podman run --it --rm --entrypoint /usr/local/bin/ntstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ntstat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randseq

```bash
$ singularity exec <container> /usr/local/bin/randseq
$ podman run --it --rm --entrypoint /usr/local/bin/randseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipcloak

```bash
$ singularity exec <container> /usr/local/bin/zipcloak
$ podman run --it --rm --entrypoint /usr/local/bin/zipcloak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipcloak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipnote

```bash
$ singularity exec <container> /usr/local/bin/zipnote
$ podman run --it --rm --entrypoint /usr/local/bin/zipnote   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipnote   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zipsplit

```bash
$ singularity exec <container> /usr/local/bin/zipsplit
$ podman run --it --rm --entrypoint /usr/local/bin/zipsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zipsplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zip

```bash
$ singularity exec <container> /usr/local/bin/zip
$ podman run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zip   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### qconvex

```bash
$ singularity exec <container> /usr/local/bin/qconvex
$ podman run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qconvex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qdelaunay

```bash
$ singularity exec <container> /usr/local/bin/qdelaunay
$ podman run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qdelaunay   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhalf

```bash
$ singularity exec <container> /usr/local/bin/qhalf
$ podman run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhalf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qhull

```bash
$ singularity exec <container> /usr/local/bin/qhull
$ podman run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qhull   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qvoronoi

```bash
$ singularity exec <container> /usr/local/bin/qvoronoi
$ podman run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qvoronoi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rbox

```bash
$ singularity exec <container> /usr/local/bin/rbox
$ podman run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbox   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
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