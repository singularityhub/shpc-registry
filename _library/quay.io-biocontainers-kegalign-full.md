---
layout: container
name:  "quay.io/biocontainers/kegalign-full"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kegalign-full/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kegalign-full/container.yaml"
updated_at: "2025-04-17 04:46:46.633239"
latest: "0.1.2.7--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/kegalign-full"
aliases:
 - "bash"
 - "bashbug"
 - "diagonal_partition.py"
 - "kegalign"
 - "lastz"
 - "lastz-cmd.ini"
 - "lastz_32"
 - "lastz_D"
 - "mbuffer"
 - "package_output.py"
 - "run_kegalign"
 - "run_lastz_tarball.py"
 - "runner.py"
 - "time"
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
 - "egrep"
 - "fgrep"
 - "grep"
 - "gawk-5.3.0"
 - "gawkbug"
 - "faToTwoBit"
 - "annot-tsv"
 - "basenc"
 - "b2sum"
 - "ls"
 - "base32"
versions:
 - "0.1.2.7--hdfd78af_0"
description: "singularity registry hpc automated addition for kegalign-full"
config: {"url": "https://biocontainers.pro/tools/kegalign-full", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for kegalign-full", "latest": {"0.1.2.7--hdfd78af_0": "sha256:03841face06e71cea03fb1b63b5e72b352798a4bb188cf4f81d22d0374809cc8"}, "tags": {"0.1.2.7--hdfd78af_0": "sha256:03841face06e71cea03fb1b63b5e72b352798a4bb188cf4f81d22d0374809cc8"}, "docker": "quay.io/biocontainers/kegalign-full", "aliases": {"bash": "/usr/local/bin/bash", "bashbug": "/usr/local/bin/bashbug", "diagonal_partition.py": "/usr/local/bin/diagonal_partition.py", "kegalign": "/usr/local/bin/kegalign", "lastz": "/usr/local/bin/lastz", "lastz-cmd.ini": "/usr/local/bin/lastz-cmd.ini", "lastz_32": "/usr/local/bin/lastz_32", "lastz_D": "/usr/local/bin/lastz_D", "mbuffer": "/usr/local/bin/mbuffer", "package_output.py": "/usr/local/bin/package_output.py", "run_kegalign": "/usr/local/bin/run_kegalign", "run_lastz_tarball.py": "/usr/local/bin/run_lastz_tarball.py", "runner.py": "/usr/local/bin/runner.py", "time": "/usr/local/bin/time", "gunzip": "/usr/local/bin/gunzip", "gzexe": "/usr/local/bin/gzexe", "gzip": "/usr/local/bin/gzip", "uncompress": "/usr/local/bin/uncompress", "zcat": "/usr/local/bin/zcat", "zcmp": "/usr/local/bin/zcmp", "zdiff": "/usr/local/bin/zdiff", "zegrep": "/usr/local/bin/zegrep", "zfgrep": "/usr/local/bin/zfgrep", "zforce": "/usr/local/bin/zforce", "zgrep": "/usr/local/bin/zgrep", "zmore": "/usr/local/bin/zmore", "znew": "/usr/local/bin/znew", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "gawk-5.3.0": "/usr/local/bin/gawk-5.3.0", "gawkbug": "/usr/local/bin/gawkbug", "faToTwoBit": "/usr/local/bin/faToTwoBit", "annot-tsv": "/usr/local/bin/annot-tsv", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kegalign-full.
singularity registry hpc automated addition for kegalign-full
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kegalign-full
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kegalign-full:0.1.2.7--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kegalign-full/0.1.2.7--hdfd78af_0
$ module help quay.io/biocontainers/kegalign-full/0.1.2.7--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kegalign-full-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kegalign-full-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kegalign-full-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kegalign-full-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kegalign-full-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kegalign-full-inspect-deffile:

```bash
$ singularity inspect -d <container>
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


#### diagonal_partition.py

```bash
$ singularity exec <container> /usr/local/bin/diagonal_partition.py
$ podman run --it --rm --entrypoint /usr/local/bin/diagonal_partition.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/diagonal_partition.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kegalign

```bash
$ singularity exec <container> /usr/local/bin/kegalign
$ podman run --it --rm --entrypoint /usr/local/bin/kegalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kegalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz

```bash
$ singularity exec <container> /usr/local/bin/lastz
$ podman run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz-cmd.ini

```bash
$ singularity exec <container> /usr/local/bin/lastz-cmd.ini
$ podman run --it --rm --entrypoint /usr/local/bin/lastz-cmd.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz-cmd.ini   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_32

```bash
$ singularity exec <container> /usr/local/bin/lastz_32
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lastz_D

```bash
$ singularity exec <container> /usr/local/bin/lastz_D
$ podman run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz_D   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mbuffer

```bash
$ singularity exec <container> /usr/local/bin/mbuffer
$ podman run --it --rm --entrypoint /usr/local/bin/mbuffer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mbuffer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### package_output.py

```bash
$ singularity exec <container> /usr/local/bin/package_output.py
$ podman run --it --rm --entrypoint /usr/local/bin/package_output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/package_output.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_kegalign

```bash
$ singularity exec <container> /usr/local/bin/run_kegalign
$ podman run --it --rm --entrypoint /usr/local/bin/run_kegalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_kegalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_lastz_tarball.py

```bash
$ singularity exec <container> /usr/local/bin/run_lastz_tarball.py
$ podman run --it --rm --entrypoint /usr/local/bin/run_lastz_tarball.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_lastz_tarball.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### runner.py

```bash
$ singularity exec <container> /usr/local/bin/runner.py
$ podman run --it --rm --entrypoint /usr/local/bin/runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/runner.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time

```bash
$ singularity exec <container> /usr/local/bin/time
$ podman run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gawk-5.3.0

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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