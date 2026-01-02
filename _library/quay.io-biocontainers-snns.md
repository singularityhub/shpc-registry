---
layout: container
name:  "quay.io/biocontainers/snns"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snns/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snns/container.yaml"
updated_at: "2026-01-02 04:24:24.392961"
latest: "4.3--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/snns"
aliases:
 - "analyze"
 - "batchman"
 - "bison"
 - "convert2snns"
 - "feedback-gennet"
 - "ff_bignet"
 - "flex"
 - "flex++"
 - "isnns"
 - "linknets"
 - "m4"
 - "mkhead"
 - "mkout"
 - "mkpat"
 - "netlearn"
 - "netperf"
 - "pat_sel"
 - "pat_sel_simple"
 - "snns"
 - "snns2c"
 - "snnsbat"
 - "td_bignet"
 - "xgui"
 - "yacc"
versions:
 - "4.3--h9ee0642_3"
description: "shpc-registry automated BioContainers addition for snns"
config: {"url": "https://biocontainers.pro/tools/snns", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snns", "latest": {"4.3--h9ee0642_3": "sha256:6025b0da71a906f2c9f19ba70504e08f7cfbdd4584e5f239e75da9ee9fa2877c"}, "tags": {"4.3--h9ee0642_3": "sha256:6025b0da71a906f2c9f19ba70504e08f7cfbdd4584e5f239e75da9ee9fa2877c"}, "docker": "quay.io/biocontainers/snns", "aliases": {"analyze": "/usr/local/bin/analyze", "batchman": "/usr/local/bin/batchman", "bison": "/usr/local/bin/bison", "convert2snns": "/usr/local/bin/convert2snns", "feedback-gennet": "/usr/local/bin/feedback-gennet", "ff_bignet": "/usr/local/bin/ff_bignet", "flex": "/usr/local/bin/flex", "flex++": "/usr/local/bin/flex++", "isnns": "/usr/local/bin/isnns", "linknets": "/usr/local/bin/linknets", "m4": "/usr/local/bin/m4", "mkhead": "/usr/local/bin/mkhead", "mkout": "/usr/local/bin/mkout", "mkpat": "/usr/local/bin/mkpat", "netlearn": "/usr/local/bin/netlearn", "netperf": "/usr/local/bin/netperf", "pat_sel": "/usr/local/bin/pat_sel", "pat_sel_simple": "/usr/local/bin/pat_sel_simple", "snns": "/usr/local/bin/snns", "snns2c": "/usr/local/bin/snns2c", "snnsbat": "/usr/local/bin/snnsbat", "td_bignet": "/usr/local/bin/td_bignet", "xgui": "/usr/local/bin/xgui", "yacc": "/usr/local/bin/yacc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snns.
shpc-registry automated BioContainers addition for snns
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snns
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snns:4.3--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snns/4.3--h9ee0642_3
$ module help quay.io/biocontainers/snns/4.3--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snns-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snns-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snns-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snns-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snns-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snns-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### analyze

```bash
$ singularity exec <container> /usr/local/bin/analyze
$ podman run --it --rm --entrypoint /usr/local/bin/analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/analyze   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### batchman

```bash
$ singularity exec <container> /usr/local/bin/batchman
$ podman run --it --rm --entrypoint /usr/local/bin/batchman   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/batchman   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bison

```bash
$ singularity exec <container> /usr/local/bin/bison
$ podman run --it --rm --entrypoint /usr/local/bin/bison   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bison   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### convert2snns

```bash
$ singularity exec <container> /usr/local/bin/convert2snns
$ podman run --it --rm --entrypoint /usr/local/bin/convert2snns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/convert2snns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### feedback-gennet

```bash
$ singularity exec <container> /usr/local/bin/feedback-gennet
$ podman run --it --rm --entrypoint /usr/local/bin/feedback-gennet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/feedback-gennet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ff_bignet

```bash
$ singularity exec <container> /usr/local/bin/ff_bignet
$ podman run --it --rm --entrypoint /usr/local/bin/ff_bignet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ff_bignet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flex

```bash
$ singularity exec <container> /usr/local/bin/flex
$ podman run --it --rm --entrypoint /usr/local/bin/flex   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flex   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flex++

```bash
$ singularity exec <container> /usr/local/bin/flex++
$ podman run --it --rm --entrypoint /usr/local/bin/flex++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flex++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### isnns

```bash
$ singularity exec <container> /usr/local/bin/isnns
$ podman run --it --rm --entrypoint /usr/local/bin/isnns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isnns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### linknets

```bash
$ singularity exec <container> /usr/local/bin/linknets
$ podman run --it --rm --entrypoint /usr/local/bin/linknets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/linknets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m4

```bash
$ singularity exec <container> /usr/local/bin/m4
$ podman run --it --rm --entrypoint /usr/local/bin/m4   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m4   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkhead

```bash
$ singularity exec <container> /usr/local/bin/mkhead
$ podman run --it --rm --entrypoint /usr/local/bin/mkhead   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkhead   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkout

```bash
$ singularity exec <container> /usr/local/bin/mkout
$ podman run --it --rm --entrypoint /usr/local/bin/mkout   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkout   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mkpat

```bash
$ singularity exec <container> /usr/local/bin/mkpat
$ podman run --it --rm --entrypoint /usr/local/bin/mkpat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mkpat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### netlearn

```bash
$ singularity exec <container> /usr/local/bin/netlearn
$ podman run --it --rm --entrypoint /usr/local/bin/netlearn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/netlearn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### netperf

```bash
$ singularity exec <container> /usr/local/bin/netperf
$ podman run --it --rm --entrypoint /usr/local/bin/netperf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/netperf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pat_sel

```bash
$ singularity exec <container> /usr/local/bin/pat_sel
$ podman run --it --rm --entrypoint /usr/local/bin/pat_sel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pat_sel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pat_sel_simple

```bash
$ singularity exec <container> /usr/local/bin/pat_sel_simple
$ podman run --it --rm --entrypoint /usr/local/bin/pat_sel_simple   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pat_sel_simple   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snns

```bash
$ singularity exec <container> /usr/local/bin/snns
$ podman run --it --rm --entrypoint /usr/local/bin/snns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snns2c

```bash
$ singularity exec <container> /usr/local/bin/snns2c
$ podman run --it --rm --entrypoint /usr/local/bin/snns2c   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snns2c   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### snnsbat

```bash
$ singularity exec <container> /usr/local/bin/snnsbat
$ podman run --it --rm --entrypoint /usr/local/bin/snnsbat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/snnsbat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### td_bignet

```bash
$ singularity exec <container> /usr/local/bin/td_bignet
$ podman run --it --rm --entrypoint /usr/local/bin/td_bignet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/td_bignet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xgui

```bash
$ singularity exec <container> /usr/local/bin/xgui
$ podman run --it --rm --entrypoint /usr/local/bin/xgui   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xgui   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yacc

```bash
$ singularity exec <container> /usr/local/bin/yacc
$ podman run --it --rm --entrypoint /usr/local/bin/yacc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yacc   -v ${PWD} -w ${PWD} <container> -c " $@"
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