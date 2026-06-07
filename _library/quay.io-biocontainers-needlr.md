---
layout: container
name:  "quay.io/biocontainers/needlr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/needlr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/needlr/container.yaml"
updated_at: "2026-06-07 07:22:53.082612"
latest: "4.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/needlr"
aliases:
 - "bwamempy"
 - "needLR"
 - "truvari"
 - "gff2gff"
 - "roh-viz"
 - "vrfs-variances"
 - "gawk-5.3.1"
 - "gff2gff.py"
 - "gawkbug"
 - "ref-cache"
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
 - "cksum"
 - "comm"
 - "cp"
 - "csplit"
 - "cut"
 - "date"
versions:
 - "4.0--hdfd78af_0"
description: "singularity registry hpc automated addition for needlr"
config: {"url": "https://biocontainers.pro/tools/needlr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for needlr", "latest": {"4.0--hdfd78af_0": "sha256:6fe9aa65fcaf372559fbf966f943c84f871daf54b4357f2feccbdca0405d3cb0"}, "tags": {"4.0--hdfd78af_0": "sha256:6fe9aa65fcaf372559fbf966f943c84f871daf54b4357f2feccbdca0405d3cb0"}, "docker": "quay.io/biocontainers/needlr", "aliases": {"bwamempy": "/usr/local/bin/bwamempy", "needLR": "/usr/local/bin/needLR", "truvari": "/usr/local/bin/truvari", "gff2gff": "/usr/local/bin/gff2gff", "roh-viz": "/usr/local/bin/roh-viz", "vrfs-variances": "/usr/local/bin/vrfs-variances", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "gff2gff.py": "/usr/local/bin/gff2gff.py", "gawkbug": "/usr/local/bin/gawkbug", "ref-cache": "/usr/local/bin/ref-cache", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot", "cksum": "/usr/local/bin/cksum", "comm": "/usr/local/bin/comm", "cp": "/usr/local/bin/cp", "csplit": "/usr/local/bin/csplit", "cut": "/usr/local/bin/cut", "date": "/usr/local/bin/date"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/needlr.
singularity registry hpc automated addition for needlr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/needlr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/needlr:4.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/needlr/4.0--hdfd78af_0
$ module help quay.io/biocontainers/needlr/4.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### needlr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### needlr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### needlr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### needlr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### needlr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### needlr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwamempy

```bash
$ singularity exec <container> /usr/local/bin/bwamempy
$ podman run --it --rm --entrypoint /usr/local/bin/bwamempy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwamempy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### needLR

```bash
$ singularity exec <container> /usr/local/bin/needLR
$ podman run --it --rm --entrypoint /usr/local/bin/needLR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/needLR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### truvari

```bash
$ singularity exec <container> /usr/local/bin/truvari
$ podman run --it --rm --entrypoint /usr/local/bin/truvari   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/truvari   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff

```bash
$ singularity exec <container> /usr/local/bin/gff2gff
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### roh-viz

```bash
$ singularity exec <container> /usr/local/bin/roh-viz
$ podman run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/roh-viz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vrfs-variances

```bash
$ singularity exec <container> /usr/local/bin/vrfs-variances
$ podman run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vrfs-variances   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### cksum

```bash
$ singularity exec <container> /usr/local/bin/cksum
$ podman run --it --rm --entrypoint /usr/local/bin/cksum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cksum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### comm

```bash
$ singularity exec <container> /usr/local/bin/comm
$ podman run --it --rm --entrypoint /usr/local/bin/comm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/comm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cp

```bash
$ singularity exec <container> /usr/local/bin/cp
$ podman run --it --rm --entrypoint /usr/local/bin/cp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### csplit

```bash
$ singularity exec <container> /usr/local/bin/csplit
$ podman run --it --rm --entrypoint /usr/local/bin/csplit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/csplit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cut

```bash
$ singularity exec <container> /usr/local/bin/cut
$ podman run --it --rm --entrypoint /usr/local/bin/cut   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cut   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### date

```bash
$ singularity exec <container> /usr/local/bin/date
$ podman run --it --rm --entrypoint /usr/local/bin/date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/date   -v ${PWD} -w ${PWD} <container> -c " $@"
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