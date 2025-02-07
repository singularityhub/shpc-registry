---
layout: container
name:  "quay.io/biocontainers/clinod"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/clinod/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/clinod/container.yaml"
updated_at: "2025-02-07 03:37:13.662757"
latest: "1.3--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/clinod"
aliases:
 - "analyze"
 - "batchman"
 - "bison"
 - "clinod"
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
 - "jfr"
 - "jaotc"
 - "aserver"
 - "jdeprscan"
 - "jhsdb"
 - "jimage"
 - "jlink"
 - "jmod"
 - "jshell"
 - "jjs"
versions:
 - "1.3--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for clinod"
config: {"url": "https://biocontainers.pro/tools/clinod", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for clinod", "latest": {"1.3--hdfd78af_4": "sha256:d9acb2d2b6a77ffde77c594589d96bb90e35beafed1459865fb1cba0fdaa563e"}, "tags": {"1.3--hdfd78af_4": "sha256:d9acb2d2b6a77ffde77c594589d96bb90e35beafed1459865fb1cba0fdaa563e"}, "docker": "quay.io/biocontainers/clinod", "aliases": {"analyze": "/usr/local/bin/analyze", "batchman": "/usr/local/bin/batchman", "bison": "/usr/local/bin/bison", "clinod": "/usr/local/bin/clinod", "convert2snns": "/usr/local/bin/convert2snns", "feedback-gennet": "/usr/local/bin/feedback-gennet", "ff_bignet": "/usr/local/bin/ff_bignet", "flex": "/usr/local/bin/flex", "flex++": "/usr/local/bin/flex++", "isnns": "/usr/local/bin/isnns", "linknets": "/usr/local/bin/linknets", "m4": "/usr/local/bin/m4", "mkhead": "/usr/local/bin/mkhead", "mkout": "/usr/local/bin/mkout", "mkpat": "/usr/local/bin/mkpat", "netlearn": "/usr/local/bin/netlearn", "netperf": "/usr/local/bin/netperf", "pat_sel": "/usr/local/bin/pat_sel", "pat_sel_simple": "/usr/local/bin/pat_sel_simple", "snns": "/usr/local/bin/snns", "snns2c": "/usr/local/bin/snns2c", "snnsbat": "/usr/local/bin/snnsbat", "td_bignet": "/usr/local/bin/td_bignet", "xgui": "/usr/local/bin/xgui", "yacc": "/usr/local/bin/yacc", "jfr": "/usr/local/bin/jfr", "jaotc": "/usr/local/bin/jaotc", "aserver": "/usr/local/bin/aserver", "jdeprscan": "/usr/local/bin/jdeprscan", "jhsdb": "/usr/local/bin/jhsdb", "jimage": "/usr/local/bin/jimage", "jlink": "/usr/local/bin/jlink", "jmod": "/usr/local/bin/jmod", "jshell": "/usr/local/bin/jshell", "jjs": "/usr/local/bin/jjs"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/clinod.
shpc-registry automated BioContainers addition for clinod
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/clinod
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/clinod:1.3--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/clinod/1.3--hdfd78af_4
$ module help quay.io/biocontainers/clinod/1.3--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### clinod-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### clinod-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### clinod-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### clinod-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### clinod-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### clinod-inspect-deffile:

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


#### clinod

```bash
$ singularity exec <container> /usr/local/bin/clinod
$ podman run --it --rm --entrypoint /usr/local/bin/clinod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/clinod   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jfr

```bash
$ singularity exec <container> /usr/local/bin/jfr
$ podman run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jfr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aserver

```bash
$ singularity exec <container> /usr/local/bin/aserver
$ podman run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jdeprscan

```bash
$ singularity exec <container> /usr/local/bin/jdeprscan
$ podman run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jdeprscan   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jhsdb

```bash
$ singularity exec <container> /usr/local/bin/jhsdb
$ podman run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jhsdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jimage

```bash
$ singularity exec <container> /usr/local/bin/jimage
$ podman run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jimage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jlink

```bash
$ singularity exec <container> /usr/local/bin/jlink
$ podman run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jmod

```bash
$ singularity exec <container> /usr/local/bin/jmod
$ podman run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jmod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jshell

```bash
$ singularity exec <container> /usr/local/bin/jshell
$ podman run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jshell   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jjs

```bash
$ singularity exec <container> /usr/local/bin/jjs
$ podman run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jjs   -v ${PWD} -w ${PWD} <container> -c " $@"
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