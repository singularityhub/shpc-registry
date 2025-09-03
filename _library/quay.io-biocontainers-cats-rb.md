---
layout: container
name:  "quay.io/biocontainers/cats-rb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cats-rb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cats-rb/container.yaml"
updated_at: "2025-09-03 03:26:20.029206"
latest: "1.0.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/cats-rb"
aliases:
 - "CATS_general_assembly_stats.R"
 - "CATS_rb_compare"
 - "CATS_rb_comparison.Rmd"
 - "CATS_rb_index"
 - "CATS_rb_map"
 - "canonical.pl"
 - "catchr.pl"
 - "clade.pl"
 - "eij2ild.pl"
 - "eij4mer.pl"
 - "eijnc.pl"
 - "makblk.pl"
 - "makdbs"
 - "make_eij.pl"
 - "make_ssp.pl"
 - "makeidx.pl"
 - "makmdm"
 - "sortgrcd"
 - "spaln"
 - "spspaln.pl"
 - "bash"
 - "bashbug"
 - "gawk-5.3.1"
 - "pandoc-lua"
 - "gawkbug"
 - "pandoc-server"
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
 - "dd"
versions:
 - "1.0.0--hdfd78af_0"
 - "1.0.1--hdfd78af_0"
description: "singularity registry hpc automated addition for cats-rb"
config: {"url": "https://biocontainers.pro/tools/cats-rb", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cats-rb", "latest": {"1.0.1--hdfd78af_0": "sha256:408d24b6a8fa7697a6d72b494dc717055d04703095a9f41a8a63162ba32e06ba"}, "tags": {"1.0.0--hdfd78af_0": "sha256:016d55a3b6911c5338a6c98b2b3e17913974307bf053ce3b2cf5e412f735e074", "1.0.1--hdfd78af_0": "sha256:408d24b6a8fa7697a6d72b494dc717055d04703095a9f41a8a63162ba32e06ba"}, "docker": "quay.io/biocontainers/cats-rb", "aliases": {"CATS_general_assembly_stats.R": "/usr/local/bin/CATS_general_assembly_stats.R", "CATS_rb_compare": "/usr/local/bin/CATS_rb_compare", "CATS_rb_comparison.Rmd": "/usr/local/bin/CATS_rb_comparison.Rmd", "CATS_rb_index": "/usr/local/bin/CATS_rb_index", "CATS_rb_map": "/usr/local/bin/CATS_rb_map", "canonical.pl": "/usr/local/bin/canonical.pl", "catchr.pl": "/usr/local/bin/catchr.pl", "clade.pl": "/usr/local/bin/clade.pl", "eij2ild.pl": "/usr/local/bin/eij2ild.pl", "eij4mer.pl": "/usr/local/bin/eij4mer.pl", "eijnc.pl": "/usr/local/bin/eijnc.pl", "makblk.pl": "/usr/local/bin/makblk.pl", "makdbs": "/usr/local/bin/makdbs", "make_eij.pl": "/usr/local/bin/make_eij.pl", "make_ssp.pl": "/usr/local/bin/make_ssp.pl", "makeidx.pl": "/usr/local/bin/makeidx.pl", "makmdm": "/usr/local/bin/makmdm", "sortgrcd": "/usr/local/bin/sortgrcd", "spaln": "/usr/local/bin/spaln", "spspaln.pl": "/usr/local/bin/spspaln.pl", "bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "pandoc-lua": "/usr/local/bin/pandoc-lua", "gawkbug": "/usr/local/bin/gawkbug", "pandoc-server": "/usr/local/bin/pandoc-server", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot", "cksum": "/usr/local/bin/cksum", "comm": "/usr/local/bin/comm", "cp": "/usr/local/bin/cp", "csplit": "/usr/local/bin/csplit", "cut": "/usr/local/bin/cut", "date": "/usr/local/bin/date", "dd": "/usr/local/bin/dd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cats-rb.
singularity registry hpc automated addition for cats-rb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cats-rb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cats-rb:1.0.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cats-rb/1.0.1--hdfd78af_0
$ module help quay.io/biocontainers/cats-rb/1.0.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cats-rb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cats-rb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cats-rb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cats-rb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cats-rb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cats-rb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CATS_general_assembly_stats.R

```bash
$ singularity exec <container> /usr/local/bin/CATS_general_assembly_stats.R
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_general_assembly_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_general_assembly_stats.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rb_compare

```bash
$ singularity exec <container> /usr/local/bin/CATS_rb_compare
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rb_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rb_compare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rb_comparison.Rmd

```bash
$ singularity exec <container> /usr/local/bin/CATS_rb_comparison.Rmd
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rb_comparison.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rb_comparison.Rmd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rb_index

```bash
$ singularity exec <container> /usr/local/bin/CATS_rb_index
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rb_index   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rb_index   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### CATS_rb_map

```bash
$ singularity exec <container> /usr/local/bin/CATS_rb_map
$ podman run --it --rm --entrypoint /usr/local/bin/CATS_rb_map   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CATS_rb_map   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### canonical.pl

```bash
$ singularity exec <container> /usr/local/bin/canonical.pl
$ podman run --it --rm --entrypoint /usr/local/bin/canonical.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canonical.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### catchr.pl

```bash
$ singularity exec <container> /usr/local/bin/catchr.pl
$ podman run --it --rm --entrypoint /usr/local/bin/catchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/catchr.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### clade.pl

```bash
$ singularity exec <container> /usr/local/bin/clade.pl
$ podman run --it --rm --entrypoint /usr/local/bin/clade.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clade.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eij2ild.pl

```bash
$ singularity exec <container> /usr/local/bin/eij2ild.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eij2ild.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eij2ild.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eij4mer.pl

```bash
$ singularity exec <container> /usr/local/bin/eij4mer.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eij4mer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eij4mer.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eijnc.pl

```bash
$ singularity exec <container> /usr/local/bin/eijnc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/eijnc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eijnc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makblk.pl

```bash
$ singularity exec <container> /usr/local/bin/makblk.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makblk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makblk.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makdbs

```bash
$ singularity exec <container> /usr/local/bin/makdbs
$ podman run --it --rm --entrypoint /usr/local/bin/makdbs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makdbs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_eij.pl

```bash
$ singularity exec <container> /usr/local/bin/make_eij.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_eij.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_eij.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_ssp.pl

```bash
$ singularity exec <container> /usr/local/bin/make_ssp.pl
$ podman run --it --rm --entrypoint /usr/local/bin/make_ssp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_ssp.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makeidx.pl

```bash
$ singularity exec <container> /usr/local/bin/makeidx.pl
$ podman run --it --rm --entrypoint /usr/local/bin/makeidx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makeidx.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makmdm

```bash
$ singularity exec <container> /usr/local/bin/makmdm
$ podman run --it --rm --entrypoint /usr/local/bin/makmdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makmdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sortgrcd

```bash
$ singularity exec <container> /usr/local/bin/sortgrcd
$ podman run --it --rm --entrypoint /usr/local/bin/sortgrcd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sortgrcd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spaln

```bash
$ singularity exec <container> /usr/local/bin/spaln
$ podman run --it --rm --entrypoint /usr/local/bin/spaln   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spaln   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spspaln.pl

```bash
$ singularity exec <container> /usr/local/bin/spspaln.pl
$ podman run --it --rm --entrypoint /usr/local/bin/spspaln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spspaln.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bash

```bash
$ singularity exec <container> /usr/local/bin/bash
$ podman run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bash   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bashbug

```bash
$ singularity exec <container> /usr/local/bin/bashbug
$ podman run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bashbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-lua

```bash
$ singularity exec <container> /usr/local/bin/pandoc-lua
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### dd

```bash
$ singularity exec <container> /usr/local/bin/dd
$ podman run --it --rm --entrypoint /usr/local/bin/dd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dd   -v ${PWD} -w ${PWD} <container> -c " $@"
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