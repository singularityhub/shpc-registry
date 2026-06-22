---
layout: container
name:  "quay.io/biocontainers/pantax-dbg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pantax-dbg/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pantax-dbg/container.yaml"
updated_at: "2026-06-22 01:56:24.586649"
latest: "0.1.0--py312hc5ce804_0"
container_url: "https://biocontainers.pro/tools/pantax-dbg"
aliases:
 - "find"
 - "ganon-get-seq-info.sh"
 - "genome_updater.sh"
 - "locate"
 - "pantax-dbg"
 - "raptor"
 - "raptor_avx2"
 - "raptor_avx512"
 - "raptor_none"
 - "raptor_sse2"
 - "raptor_sse4.2"
 - "updatedb"
 - "xargs"
 - "gawk-5.4.0"
 - "zless"
 - "bc"
 - "dc"
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
 - "fastp"
 - "tar"
 - "basenc"
 - "b2sum"
 - "gawkbug"
 - "ls"
 - "base32"
 - "base64"
versions:
 - "0.1.0--py312hc5ce804_0"
description: "singularity registry hpc automated addition for pantax-dbg"
config: {"url": "https://biocontainers.pro/tools/pantax-dbg", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pantax-dbg", "latest": {"0.1.0--py312hc5ce804_0": "sha256:1ea37bcaf43a2f6baf2094aabdd8e4e01b5b90435d87b09c878bb2ef5d14f0a8"}, "tags": {"0.1.0--py312hc5ce804_0": "sha256:1ea37bcaf43a2f6baf2094aabdd8e4e01b5b90435d87b09c878bb2ef5d14f0a8"}, "docker": "quay.io/biocontainers/pantax-dbg", "aliases": {"find": "/usr/local/bin/find", "ganon-get-seq-info.sh": "/usr/local/bin/ganon-get-seq-info.sh", "genome_updater.sh": "/usr/local/bin/genome_updater.sh", "locate": "/usr/local/bin/locate", "pantax-dbg": "/usr/local/bin/pantax-dbg", "raptor": "/usr/local/bin/raptor", "raptor_avx2": "/usr/local/bin/raptor_avx2", "raptor_avx512": "/usr/local/bin/raptor_avx512", "raptor_none": "/usr/local/bin/raptor_none", "raptor_sse2": "/usr/local/bin/raptor_sse2", "raptor_sse4.2": "/usr/local/bin/raptor_sse4.2", "updatedb": "/usr/local/bin/updatedb", "xargs": "/usr/local/bin/xargs", "gawk-5.4.0": "/usr/local/bin/gawk-5.4.0", "zless": "/usr/local/bin/zless", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "fastp": "/usr/local/bin/fastp", "tar": "/usr/local/bin/tar", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "gawkbug": "/usr/local/bin/gawkbug", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pantax-dbg.
singularity registry hpc automated addition for pantax-dbg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pantax-dbg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pantax-dbg:0.1.0--py312hc5ce804_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pantax-dbg/0.1.0--py312hc5ce804_0
$ module help quay.io/biocontainers/pantax-dbg/0.1.0--py312hc5ce804_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pantax-dbg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pantax-dbg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pantax-dbg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pantax-dbg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pantax-dbg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pantax-dbg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### find

```bash
$ singularity exec <container> /usr/local/bin/find
$ podman run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-get-seq-info.sh

```bash
$ singularity exec <container> /usr/local/bin/ganon-get-seq-info.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-get-seq-info.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-get-seq-info.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_updater.sh

```bash
$ singularity exec <container> /usr/local/bin/genome_updater.sh
$ podman run --it --rm --entrypoint /usr/local/bin/genome_updater.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_updater.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locate

```bash
$ singularity exec <container> /usr/local/bin/locate
$ podman run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pantax-dbg

```bash
$ singularity exec <container> /usr/local/bin/pantax-dbg
$ podman run --it --rm --entrypoint /usr/local/bin/pantax-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pantax-dbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raptor

```bash
$ singularity exec <container> /usr/local/bin/raptor
$ podman run --it --rm --entrypoint /usr/local/bin/raptor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raptor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raptor_avx2

```bash
$ singularity exec <container> /usr/local/bin/raptor_avx2
$ podman run --it --rm --entrypoint /usr/local/bin/raptor_avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raptor_avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raptor_avx512

```bash
$ singularity exec <container> /usr/local/bin/raptor_avx512
$ podman run --it --rm --entrypoint /usr/local/bin/raptor_avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raptor_avx512   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raptor_none

```bash
$ singularity exec <container> /usr/local/bin/raptor_none
$ podman run --it --rm --entrypoint /usr/local/bin/raptor_none   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raptor_none   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raptor_sse2

```bash
$ singularity exec <container> /usr/local/bin/raptor_sse2
$ podman run --it --rm --entrypoint /usr/local/bin/raptor_sse2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raptor_sse2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### raptor_sse4.2

```bash
$ singularity exec <container> /usr/local/bin/raptor_sse4.2
$ podman run --it --rm --entrypoint /usr/local/bin/raptor_sse4.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/raptor_sse4.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### updatedb

```bash
$ singularity exec <container> /usr/local/bin/updatedb
$ podman run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/updatedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xargs

```bash
$ singularity exec <container> /usr/local/bin/xargs
$ podman run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xargs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.4.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.4.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.4.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### zless

```bash
$ singularity exec <container> /usr/local/bin/zless
$ podman run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/zless   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bc

```bash
$ singularity exec <container> /usr/local/bin/bc
$ podman run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dc

```bash
$ singularity exec <container> /usr/local/bin/dc
$ podman run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dc   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ls

```bash
$ singularity exec <container> /usr/local/bin/ls
$ podman run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ls   -v ${PWD} -w ${PWD} <container> -c " $@"
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