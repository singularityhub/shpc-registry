---
layout: container
name:  "quay.io/biocontainers/psmc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/psmc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/psmc/container.yaml"
updated_at: "2025-09-04 03:22:22.607110"
latest: "0.6.5--h5ca1c30_4"
container_url: "https://biocontainers.pro/tools/psmc"
aliases:
 - "Makefile"
 - "avg.pl"
 - "calD"
 - "calD.c"
 - "calD.o"
 - "cntcpg"
 - "cntcpg.c"
 - "cntcpg.o"
 - "ctime_plot.pl"
 - "dec2ctime.pl"
 - "decode2bed.pl"
 - "fq2psmcfa"
 - "fq2psmcfa.c"
 - "fq2psmcfa.o"
 - "history2ms.pl"
 - "khash.h"
 - "ms2psmcfa.pl"
 - "mutDiff"
 - "mutDiff.c"
 - "mutDiff.o"
 - "pcnt_bezier.lua"
 - "psmc"
 - "psmc2history.pl"
 - "psmc_plot.pl"
 - "psmc_trunc.pl"
 - "splitfa"
 - "splitfa.c"
 - "splitfa.o"
versions:
 - "0.6.5--h5b5514e_0"
 - "0.6.5--h43eeafb_2"
 - "0.6.5--h43eeafb_3"
 - "0.6.5--h5ca1c30_4"
description: "singularity registry hpc automated addition for psmc"
config: {"url": "https://biocontainers.pro/tools/psmc", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for psmc", "latest": {"0.6.5--h5ca1c30_4": "sha256:688be5ba94944c4241f8fdff2bac31331aab72693df8ce91687fd948aff2c46e"}, "tags": {"0.6.5--h5b5514e_0": "sha256:0969906a912c973a0ff9d7db26cd7f7ac97361ed8f220a1ada1576f7629af0e2", "0.6.5--h43eeafb_2": "sha256:7e182e57bf5eb74f0250daff84de814c832f3503e79dda82adb506bb73c0ea0b", "0.6.5--h43eeafb_3": "sha256:39b2f0ee21d1f7960690b71bec83e812ff3fe82e3eea421715477e956d2e32a2", "0.6.5--h5ca1c30_4": "sha256:688be5ba94944c4241f8fdff2bac31331aab72693df8ce91687fd948aff2c46e"}, "docker": "quay.io/biocontainers/psmc", "aliases": {"Makefile": "/usr/local/bin/Makefile", "avg.pl": "/usr/local/bin/avg.pl", "calD": "/usr/local/bin/calD", "calD.c": "/usr/local/bin/calD.c", "calD.o": "/usr/local/bin/calD.o", "cntcpg": "/usr/local/bin/cntcpg", "cntcpg.c": "/usr/local/bin/cntcpg.c", "cntcpg.o": "/usr/local/bin/cntcpg.o", "ctime_plot.pl": "/usr/local/bin/ctime_plot.pl", "dec2ctime.pl": "/usr/local/bin/dec2ctime.pl", "decode2bed.pl": "/usr/local/bin/decode2bed.pl", "fq2psmcfa": "/usr/local/bin/fq2psmcfa", "fq2psmcfa.c": "/usr/local/bin/fq2psmcfa.c", "fq2psmcfa.o": "/usr/local/bin/fq2psmcfa.o", "history2ms.pl": "/usr/local/bin/history2ms.pl", "khash.h": "/usr/local/bin/khash.h", "ms2psmcfa.pl": "/usr/local/bin/ms2psmcfa.pl", "mutDiff": "/usr/local/bin/mutDiff", "mutDiff.c": "/usr/local/bin/mutDiff.c", "mutDiff.o": "/usr/local/bin/mutDiff.o", "pcnt_bezier.lua": "/usr/local/bin/pcnt_bezier.lua", "psmc": "/usr/local/bin/psmc", "psmc2history.pl": "/usr/local/bin/psmc2history.pl", "psmc_plot.pl": "/usr/local/bin/psmc_plot.pl", "psmc_trunc.pl": "/usr/local/bin/psmc_trunc.pl", "splitfa": "/usr/local/bin/splitfa", "splitfa.c": "/usr/local/bin/splitfa.c", "splitfa.o": "/usr/local/bin/splitfa.o"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/psmc.
singularity registry hpc automated addition for psmc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/psmc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/psmc:0.6.5--h5ca1c30_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/psmc/0.6.5--h5ca1c30_4
$ module help quay.io/biocontainers/psmc/0.6.5--h5ca1c30_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### psmc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### psmc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### psmc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### psmc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### psmc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### psmc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Makefile

```bash
$ singularity exec <container> /usr/local/bin/Makefile
$ podman run --it --rm --entrypoint /usr/local/bin/Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Makefile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### avg.pl

```bash
$ singularity exec <container> /usr/local/bin/avg.pl
$ podman run --it --rm --entrypoint /usr/local/bin/avg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/avg.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calD

```bash
$ singularity exec <container> /usr/local/bin/calD
$ podman run --it --rm --entrypoint /usr/local/bin/calD   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calD   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calD.c

```bash
$ singularity exec <container> /usr/local/bin/calD.c
$ podman run --it --rm --entrypoint /usr/local/bin/calD.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calD.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### calD.o

```bash
$ singularity exec <container> /usr/local/bin/calD.o
$ podman run --it --rm --entrypoint /usr/local/bin/calD.o   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calD.o   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cntcpg

```bash
$ singularity exec <container> /usr/local/bin/cntcpg
$ podman run --it --rm --entrypoint /usr/local/bin/cntcpg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cntcpg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cntcpg.c

```bash
$ singularity exec <container> /usr/local/bin/cntcpg.c
$ podman run --it --rm --entrypoint /usr/local/bin/cntcpg.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cntcpg.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cntcpg.o

```bash
$ singularity exec <container> /usr/local/bin/cntcpg.o
$ podman run --it --rm --entrypoint /usr/local/bin/cntcpg.o   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cntcpg.o   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ctime_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/ctime_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ctime_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ctime_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dec2ctime.pl

```bash
$ singularity exec <container> /usr/local/bin/dec2ctime.pl
$ podman run --it --rm --entrypoint /usr/local/bin/dec2ctime.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dec2ctime.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### decode2bed.pl

```bash
$ singularity exec <container> /usr/local/bin/decode2bed.pl
$ podman run --it --rm --entrypoint /usr/local/bin/decode2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/decode2bed.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fq2psmcfa

```bash
$ singularity exec <container> /usr/local/bin/fq2psmcfa
$ podman run --it --rm --entrypoint /usr/local/bin/fq2psmcfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fq2psmcfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fq2psmcfa.c

```bash
$ singularity exec <container> /usr/local/bin/fq2psmcfa.c
$ podman run --it --rm --entrypoint /usr/local/bin/fq2psmcfa.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fq2psmcfa.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fq2psmcfa.o

```bash
$ singularity exec <container> /usr/local/bin/fq2psmcfa.o
$ podman run --it --rm --entrypoint /usr/local/bin/fq2psmcfa.o   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fq2psmcfa.o   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### history2ms.pl

```bash
$ singularity exec <container> /usr/local/bin/history2ms.pl
$ podman run --it --rm --entrypoint /usr/local/bin/history2ms.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/history2ms.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### khash.h

```bash
$ singularity exec <container> /usr/local/bin/khash.h
$ podman run --it --rm --entrypoint /usr/local/bin/khash.h   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/khash.h   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ms2psmcfa.pl

```bash
$ singularity exec <container> /usr/local/bin/ms2psmcfa.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ms2psmcfa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ms2psmcfa.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutDiff

```bash
$ singularity exec <container> /usr/local/bin/mutDiff
$ podman run --it --rm --entrypoint /usr/local/bin/mutDiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutDiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutDiff.c

```bash
$ singularity exec <container> /usr/local/bin/mutDiff.c
$ podman run --it --rm --entrypoint /usr/local/bin/mutDiff.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutDiff.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mutDiff.o

```bash
$ singularity exec <container> /usr/local/bin/mutDiff.o
$ podman run --it --rm --entrypoint /usr/local/bin/mutDiff.o   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mutDiff.o   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pcnt_bezier.lua

```bash
$ singularity exec <container> /usr/local/bin/pcnt_bezier.lua
$ podman run --it --rm --entrypoint /usr/local/bin/pcnt_bezier.lua   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pcnt_bezier.lua   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psmc

```bash
$ singularity exec <container> /usr/local/bin/psmc
$ podman run --it --rm --entrypoint /usr/local/bin/psmc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psmc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psmc2history.pl

```bash
$ singularity exec <container> /usr/local/bin/psmc2history.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psmc2history.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psmc2history.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psmc_plot.pl

```bash
$ singularity exec <container> /usr/local/bin/psmc_plot.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psmc_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psmc_plot.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psmc_trunc.pl

```bash
$ singularity exec <container> /usr/local/bin/psmc_trunc.pl
$ podman run --it --rm --entrypoint /usr/local/bin/psmc_trunc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psmc_trunc.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitfa

```bash
$ singularity exec <container> /usr/local/bin/splitfa
$ podman run --it --rm --entrypoint /usr/local/bin/splitfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitfa.c

```bash
$ singularity exec <container> /usr/local/bin/splitfa.c
$ podman run --it --rm --entrypoint /usr/local/bin/splitfa.c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitfa.c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitfa.o

```bash
$ singularity exec <container> /usr/local/bin/splitfa.o
$ podman run --it --rm --entrypoint /usr/local/bin/splitfa.o   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitfa.o   -v ${PWD} -w ${PWD} <container> -c " $@"
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