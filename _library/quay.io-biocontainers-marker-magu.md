---
layout: container
name:  "quay.io/biocontainers/marker-magu"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/marker-magu/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/marker-magu/container.yaml"
updated_at: "2025-02-27 03:42:26.288962"
latest: "0.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/marker-magu"
aliases:
 - "bwa-mem2"
 - "bwa-mem2.avx"
 - "bwa-mem2.avx2"
 - "bwa-mem2.avx512bw"
 - "bwa-mem2.sse41"
 - "bwa-mem2.sse42"
 - "coverm"
 - "dashing"
 - "markermagu"
 - "remove_minimap2_duplicated_headers"
 - "starcode"
 - "fastANI"
 - "seqkit"
 - "fastp"
 - "igzip"
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
versions:
 - "0.4.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for marker-magu"
config: {"url": "https://biocontainers.pro/tools/marker-magu", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for marker-magu", "latest": {"0.4.0--pyhdfd78af_0": "sha256:6fe592fa89def299c3c0cfc83f68f73ae4a240cdb61f536737aa873797359086"}, "tags": {"0.4.0--pyhdfd78af_0": "sha256:6fe592fa89def299c3c0cfc83f68f73ae4a240cdb61f536737aa873797359086"}, "docker": "quay.io/biocontainers/marker-magu", "aliases": {"bwa-mem2": "/usr/local/bin/bwa-mem2", "bwa-mem2.avx": "/usr/local/bin/bwa-mem2.avx", "bwa-mem2.avx2": "/usr/local/bin/bwa-mem2.avx2", "bwa-mem2.avx512bw": "/usr/local/bin/bwa-mem2.avx512bw", "bwa-mem2.sse41": "/usr/local/bin/bwa-mem2.sse41", "bwa-mem2.sse42": "/usr/local/bin/bwa-mem2.sse42", "coverm": "/usr/local/bin/coverm", "dashing": "/usr/local/bin/dashing", "markermagu": "/usr/local/bin/markermagu", "remove_minimap2_duplicated_headers": "/usr/local/bin/remove_minimap2_duplicated_headers", "starcode": "/usr/local/bin/starcode", "fastANI": "/usr/local/bin/fastANI", "seqkit": "/usr/local/bin/seqkit", "fastp": "/usr/local/bin/fastp", "igzip": "/usr/local/bin/igzip", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "ls": "/usr/local/bin/ls", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown", "chroot": "/usr/local/bin/chroot", "cksum": "/usr/local/bin/cksum", "comm": "/usr/local/bin/comm", "cp": "/usr/local/bin/cp", "csplit": "/usr/local/bin/csplit", "cut": "/usr/local/bin/cut", "date": "/usr/local/bin/date", "dd": "/usr/local/bin/dd", "df": "/usr/local/bin/df"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/marker-magu.
singularity registry hpc automated addition for marker-magu
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/marker-magu
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/marker-magu:0.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/marker-magu/0.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/marker-magu/0.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### marker-magu-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### marker-magu-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### marker-magu-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### marker-magu-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### marker-magu-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### marker-magu-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bwa-mem2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx2

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx2
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.avx512bw

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.avx512bw
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.avx512bw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse41

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse41
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse41   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa-mem2.sse42

```bash
$ singularity exec <container> /usr/local/bin/bwa-mem2.sse42
$ podman run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa-mem2.sse42   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coverm

```bash
$ singularity exec <container> /usr/local/bin/coverm
$ podman run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coverm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dashing

```bash
$ singularity exec <container> /usr/local/bin/dashing
$ podman run --it --rm --entrypoint /usr/local/bin/dashing   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dashing   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### markermagu

```bash
$ singularity exec <container> /usr/local/bin/markermagu
$ podman run --it --rm --entrypoint /usr/local/bin/markermagu   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/markermagu   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### remove_minimap2_duplicated_headers

```bash
$ singularity exec <container> /usr/local/bin/remove_minimap2_duplicated_headers
$ podman run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/remove_minimap2_duplicated_headers   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastANI

```bash
$ singularity exec <container> /usr/local/bin/fastANI
$ podman run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastANI   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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