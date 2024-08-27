---
layout: container
name:  "quay.io/biocontainers/segalign-full"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/segalign-full/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/segalign-full/container.yaml"
updated_at: "2024-08-27 06:55:42.124317"
latest: "0.1.2.7--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/segalign-full"
aliases:
 - "lastz"
 - "lastz_32"
 - "lastz_D"
 - "run_segalign"
 - "run_segalign_repeat_masker"
 - "segalign"
 - "segalign_repeat_masker"
 - "egrep"
 - "fgrep"
 - "grep"
 - "faToTwoBit"
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
 - "df"
 - "dir"
versions:
 - "0.1.2--hdfd78af_1"
 - "0.1.2.1--hdfd78af_0"
 - "0.1.2.2--hdfd78af_0"
 - "0.1.2.7--hdfd78af_0"
 - "0.1.2.7--hdfd78af_1"
description: "singularity registry hpc automated addition for segalign-full"
config: {"url": "https://biocontainers.pro/tools/segalign-full", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for segalign-full", "latest": {"0.1.2.7--hdfd78af_1": "sha256:6991ddff6ff67259b06194a77c6394110a517be75df9ae5c7ac4e6520e5b299a"}, "tags": {"0.1.2--hdfd78af_1": "sha256:9dc369f7d2847366c58c1ec3460a6f31bd75216ef5c7e9201997fef44867b21d", "0.1.2.1--hdfd78af_0": "sha256:9ed4c344d030c38b5f14dea0227a77ac148b8d4468d51ba91a19405ca6380c31", "0.1.2.2--hdfd78af_0": "sha256:e62ac55a6f57359ae61e1394956170b7fa2f0a13d3dab7cef38ed7f02a019281", "0.1.2.7--hdfd78af_0": "sha256:958e12f10362e589fb1e983791e03cafe1504d944d0cbd5b968a124e8d6b09bc", "0.1.2.7--hdfd78af_1": "sha256:6991ddff6ff67259b06194a77c6394110a517be75df9ae5c7ac4e6520e5b299a"}, "docker": "quay.io/biocontainers/segalign-full", "aliases": {"lastz": "/usr/local/bin/lastz", "lastz_32": "/usr/local/bin/lastz_32", "lastz_D": "/usr/local/bin/lastz_D", "run_segalign": "/usr/local/bin/run_segalign", "run_segalign_repeat_masker": "/usr/local/bin/run_segalign_repeat_masker", "segalign": "/usr/local/bin/segalign", "segalign_repeat_masker": "/usr/local/bin/segalign_repeat_masker", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "faToTwoBit": "/usr/local/bin/faToTwoBit", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot", "cksum": "/usr/local/bin/cksum", "comm": "/usr/local/bin/comm", "cp": "/usr/local/bin/cp", "csplit": "/usr/local/bin/csplit", "cut": "/usr/local/bin/cut", "date": "/usr/local/bin/date", "dd": "/usr/local/bin/dd", "df": "/usr/local/bin/df", "dir": "/usr/local/bin/dir"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/segalign-full.
singularity registry hpc automated addition for segalign-full
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/segalign-full
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/segalign-full:0.1.2.7--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/segalign-full/0.1.2.7--hdfd78af_1
$ module help quay.io/biocontainers/segalign-full/0.1.2.7--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### segalign-full-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### segalign-full-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### segalign-full-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### segalign-full-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### segalign-full-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### segalign-full-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lastz

```bash
$ singularity exec <container> /usr/local/bin/lastz
$ podman run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lastz   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### run_segalign

```bash
$ singularity exec <container> /usr/local/bin/run_segalign
$ podman run --it --rm --entrypoint /usr/local/bin/run_segalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_segalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run_segalign_repeat_masker

```bash
$ singularity exec <container> /usr/local/bin/run_segalign_repeat_masker
$ podman run --it --rm --entrypoint /usr/local/bin/run_segalign_repeat_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run_segalign_repeat_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segalign

```bash
$ singularity exec <container> /usr/local/bin/segalign
$ podman run --it --rm --entrypoint /usr/local/bin/segalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segalign_repeat_masker

```bash
$ singularity exec <container> /usr/local/bin/segalign_repeat_masker
$ podman run --it --rm --entrypoint /usr/local/bin/segalign_repeat_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segalign_repeat_masker   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### faToTwoBit

```bash
$ singularity exec <container> /usr/local/bin/faToTwoBit
$ podman run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/faToTwoBit   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### df

```bash
$ singularity exec <container> /usr/local/bin/df
$ podman run --it --rm --entrypoint /usr/local/bin/df   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/df   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dir

```bash
$ singularity exec <container> /usr/local/bin/dir
$ podman run --it --rm --entrypoint /usr/local/bin/dir   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dir   -v ${PWD} -w ${PWD} <container> -c " $@"
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