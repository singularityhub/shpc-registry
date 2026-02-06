---
layout: container
name:  "quay.io/biocontainers/themis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/themis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/themis/container.yaml"
updated_at: "2026-02-06 04:56:28.452835"
latest: "0.1.0--py314h0cb7dc8_0"
container_url: "https://biocontainers.pro/tools/themis"
aliases:
 - "cmp"
 - "diff"
 - "diff3"
 - "find"
 - "ganon"
 - "ganon-build"
 - "ganon-classify"
 - "ganon-get-seq-info.sh"
 - "ganon-report"
 - "genome_updater.sh"
 - "ggcat"
 - "locate"
 - "raptor"
 - "raptor_avx2"
 - "raptor_avx512"
 - "raptor_none"
 - "raptor_sse2"
 - "raptor_sse4.2"
 - "sdiff"
 - "themis"
 - "updatedb"
 - "xargs"
 - "bc"
 - "dc"
 - "egrep"
 - "fgrep"
 - "grep"
 - "fastp"
 - "idle3.14"
 - "pydoc3.14"
 - "python3.14"
 - "python3.14-config"
 - "gawk-5.3.1"
 - "tar"
 - "gawkbug"
 - "basenc"
 - "b2sum"
 - "ls"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
 - "chown"
 - "chroot"
versions:
 - "0.1.0--py314h0cb7dc8_0"
description: "singularity registry hpc automated addition for themis"
config: {"url": "https://biocontainers.pro/tools/themis", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for themis", "latest": {"0.1.0--py314h0cb7dc8_0": "sha256:674ee540661f79dfd1da035581882cd1f00fc1380684a3c2081dea57e65a7da4"}, "tags": {"0.1.0--py314h0cb7dc8_0": "sha256:674ee540661f79dfd1da035581882cd1f00fc1380684a3c2081dea57e65a7da4"}, "docker": "quay.io/biocontainers/themis", "aliases": {"cmp": "/usr/local/bin/cmp", "diff": "/usr/local/bin/diff", "diff3": "/usr/local/bin/diff3", "find": "/usr/local/bin/find", "ganon": "/usr/local/bin/ganon", "ganon-build": "/usr/local/bin/ganon-build", "ganon-classify": "/usr/local/bin/ganon-classify", "ganon-get-seq-info.sh": "/usr/local/bin/ganon-get-seq-info.sh", "ganon-report": "/usr/local/bin/ganon-report", "genome_updater.sh": "/usr/local/bin/genome_updater.sh", "ggcat": "/usr/local/bin/ggcat", "locate": "/usr/local/bin/locate", "raptor": "/usr/local/bin/raptor", "raptor_avx2": "/usr/local/bin/raptor_avx2", "raptor_avx512": "/usr/local/bin/raptor_avx512", "raptor_none": "/usr/local/bin/raptor_none", "raptor_sse2": "/usr/local/bin/raptor_sse2", "raptor_sse4.2": "/usr/local/bin/raptor_sse4.2", "sdiff": "/usr/local/bin/sdiff", "themis": "/usr/local/bin/themis", "updatedb": "/usr/local/bin/updatedb", "xargs": "/usr/local/bin/xargs", "bc": "/usr/local/bin/bc", "dc": "/usr/local/bin/dc", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "fastp": "/usr/local/bin/fastp", "idle3.14": "/usr/local/bin/idle3.14", "pydoc3.14": "/usr/local/bin/pydoc3.14", "python3.14": "/usr/local/bin/python3.14", "python3.14-config": "/usr/local/bin/python3.14-config", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "tar": "/usr/local/bin/tar", "gawkbug": "/usr/local/bin/gawkbug", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/themis.
singularity registry hpc automated addition for themis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/themis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/themis:0.1.0--py314h0cb7dc8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/themis/0.1.0--py314h0cb7dc8_0
$ module help quay.io/biocontainers/themis/0.1.0--py314h0cb7dc8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### themis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### themis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### themis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### themis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### themis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### themis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cmp

```bash
$ singularity exec <container> /usr/local/bin/cmp
$ podman run --it --rm --entrypoint /usr/local/bin/cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diff

```bash
$ singularity exec <container> /usr/local/bin/diff
$ podman run --it --rm --entrypoint /usr/local/bin/diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### diff3

```bash
$ singularity exec <container> /usr/local/bin/diff3
$ podman run --it --rm --entrypoint /usr/local/bin/diff3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diff3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### find

```bash
$ singularity exec <container> /usr/local/bin/find
$ podman run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/find   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon

```bash
$ singularity exec <container> /usr/local/bin/ganon
$ podman run --it --rm --entrypoint /usr/local/bin/ganon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-build

```bash
$ singularity exec <container> /usr/local/bin/ganon-build
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-classify

```bash
$ singularity exec <container> /usr/local/bin/ganon-classify
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-classify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-classify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-get-seq-info.sh

```bash
$ singularity exec <container> /usr/local/bin/ganon-get-seq-info.sh
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-get-seq-info.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-get-seq-info.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ganon-report

```bash
$ singularity exec <container> /usr/local/bin/ganon-report
$ podman run --it --rm --entrypoint /usr/local/bin/ganon-report   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ganon-report   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genome_updater.sh

```bash
$ singularity exec <container> /usr/local/bin/genome_updater.sh
$ podman run --it --rm --entrypoint /usr/local/bin/genome_updater.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genome_updater.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ggcat

```bash
$ singularity exec <container> /usr/local/bin/ggcat
$ podman run --it --rm --entrypoint /usr/local/bin/ggcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ggcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### locate

```bash
$ singularity exec <container> /usr/local/bin/locate
$ podman run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/locate   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### sdiff

```bash
$ singularity exec <container> /usr/local/bin/sdiff
$ podman run --it --rm --entrypoint /usr/local/bin/sdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### themis

```bash
$ singularity exec <container> /usr/local/bin/themis
$ podman run --it --rm --entrypoint /usr/local/bin/themis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/themis   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.14

```bash
$ singularity exec <container> /usr/local/bin/idle3.14
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.14

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.14
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14

```bash
$ singularity exec <container> /usr/local/bin/python3.14
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.14-config

```bash
$ singularity exec <container> /usr/local/bin/python3.14-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.14-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tar

```bash
$ singularity exec <container> /usr/local/bin/tar
$ podman run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### chgrp

```bash
$ singularity exec <container> /usr/local/bin/chgrp
$ podman run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmod

```bash
$ singularity exec <container> /usr/local/bin/chmod
$ podman run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chown

```bash
$ singularity exec <container> /usr/local/bin/chown
$ podman run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chroot

```bash
$ singularity exec <container> /usr/local/bin/chroot
$ podman run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chroot   -v ${PWD} -w ${PWD} <container> -c " $@"
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