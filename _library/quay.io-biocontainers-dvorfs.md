---
layout: container
name:  "quay.io/biocontainers/dvorfs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dvorfs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/dvorfs/container.yaml"
updated_at: "2022-10-29 05:33:20.521352"
latest: "1.0.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/dvorfs"
aliases:
 - "dba"
 - "dnal"
 - "dvorfs"
 - "estwise"
 - "estwisedb"
 - "genewise"
 - "genewisedb"
 - "hmmalign2"
 - "hmmbuild2"
 - "hmmcalibrate2"
 - "hmmconvert2"
 - "hmmemit2"
 - "hmmfetch2"
 - "hmmindex2"
 - "hmmpfam2"
 - "hmmsearch2"
 - "process-genewise"
 - "promoterwise"
 - "psw"
 - "pswdb"
 - "scanwise"
 - "scanwise_server"
 - "2to3-3.9"
 - "_aaindexextract"
 - "_abiview"
 - "_acdc"
 - "_acdpretty"
 - "_acdtable"
 - "_acdtrace"
 - "_acdvalid"
 - "_antigenic"
 - "_backtranambig"
versions:
 - "1.0.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for dvorfs"
config: {"url": "https://biocontainers.pro/tools/dvorfs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dvorfs", "latest": {"1.0.1--pyhdfd78af_0": "sha256:32cd4ae9df453f3c687b7a9aa7bf9491752711c940fa60f2cb720399b529e37f"}, "tags": {"1.0.1--pyhdfd78af_0": "sha256:32cd4ae9df453f3c687b7a9aa7bf9491752711c940fa60f2cb720399b529e37f"}, "docker": "quay.io/biocontainers/dvorfs", "aliases": {"dba": "/usr/local/bin/dba", "dnal": "/usr/local/bin/dnal", "dvorfs": "/usr/local/bin/dvorfs", "estwise": "/usr/local/bin/estwise", "estwisedb": "/usr/local/bin/estwisedb", "genewise": "/usr/local/bin/genewise", "genewisedb": "/usr/local/bin/genewisedb", "hmmalign2": "/usr/local/bin/hmmalign2", "hmmbuild2": "/usr/local/bin/hmmbuild2", "hmmcalibrate2": "/usr/local/bin/hmmcalibrate2", "hmmconvert2": "/usr/local/bin/hmmconvert2", "hmmemit2": "/usr/local/bin/hmmemit2", "hmmfetch2": "/usr/local/bin/hmmfetch2", "hmmindex2": "/usr/local/bin/hmmindex2", "hmmpfam2": "/usr/local/bin/hmmpfam2", "hmmsearch2": "/usr/local/bin/hmmsearch2", "process-genewise": "/usr/local/bin/process-genewise", "promoterwise": "/usr/local/bin/promoterwise", "psw": "/usr/local/bin/psw", "pswdb": "/usr/local/bin/pswdb", "scanwise": "/usr/local/bin/scanwise", "scanwise_server": "/usr/local/bin/scanwise_server", "2to3-3.9": "/usr/local/bin/2to3-3.9", "_aaindexextract": "/usr/local/bin/_aaindexextract", "_abiview": "/usr/local/bin/_abiview", "_acdc": "/usr/local/bin/_acdc", "_acdpretty": "/usr/local/bin/_acdpretty", "_acdtable": "/usr/local/bin/_acdtable", "_acdtrace": "/usr/local/bin/_acdtrace", "_acdvalid": "/usr/local/bin/_acdvalid", "_antigenic": "/usr/local/bin/_antigenic", "_backtranambig": "/usr/local/bin/_backtranambig"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dvorfs.
shpc-registry automated BioContainers addition for dvorfs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dvorfs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dvorfs:1.0.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dvorfs/1.0.1--pyhdfd78af_0
$ module help quay.io/biocontainers/dvorfs/1.0.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dvorfs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dvorfs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dvorfs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dvorfs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dvorfs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dvorfs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dba

```bash
$ singularity exec <container> /usr/local/bin/dba
$ podman run --it --rm --entrypoint /usr/local/bin/dba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dnal

```bash
$ singularity exec <container> /usr/local/bin/dnal
$ podman run --it --rm --entrypoint /usr/local/bin/dnal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dnal   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dvorfs

```bash
$ singularity exec <container> /usr/local/bin/dvorfs
$ podman run --it --rm --entrypoint /usr/local/bin/dvorfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dvorfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estwise

```bash
$ singularity exec <container> /usr/local/bin/estwise
$ podman run --it --rm --entrypoint /usr/local/bin/estwise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estwise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### estwisedb

```bash
$ singularity exec <container> /usr/local/bin/estwisedb
$ podman run --it --rm --entrypoint /usr/local/bin/estwisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/estwisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genewise

```bash
$ singularity exec <container> /usr/local/bin/genewise
$ podman run --it --rm --entrypoint /usr/local/bin/genewise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genewise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genewisedb

```bash
$ singularity exec <container> /usr/local/bin/genewisedb
$ podman run --it --rm --entrypoint /usr/local/bin/genewisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genewisedb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmalign2

```bash
$ singularity exec <container> /usr/local/bin/hmmalign2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmalign2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmbuild2

```bash
$ singularity exec <container> /usr/local/bin/hmmbuild2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmbuild2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmcalibrate2

```bash
$ singularity exec <container> /usr/local/bin/hmmcalibrate2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmcalibrate2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert2

```bash
$ singularity exec <container> /usr/local/bin/hmmconvert2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmconvert2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit2

```bash
$ singularity exec <container> /usr/local/bin/hmmemit2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmemit2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmfetch2

```bash
$ singularity exec <container> /usr/local/bin/hmmfetch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmfetch2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmindex2

```bash
$ singularity exec <container> /usr/local/bin/hmmindex2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmindex2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpfam2

```bash
$ singularity exec <container> /usr/local/bin/hmmpfam2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpfam2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmsearch2

```bash
$ singularity exec <container> /usr/local/bin/hmmsearch2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmsearch2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### process-genewise

```bash
$ singularity exec <container> /usr/local/bin/process-genewise
$ podman run --it --rm --entrypoint /usr/local/bin/process-genewise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/process-genewise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### promoterwise

```bash
$ singularity exec <container> /usr/local/bin/promoterwise
$ podman run --it --rm --entrypoint /usr/local/bin/promoterwise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/promoterwise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### psw

```bash
$ singularity exec <container> /usr/local/bin/psw
$ podman run --it --rm --entrypoint /usr/local/bin/psw   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/psw   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pswdb

```bash
$ singularity exec <container> /usr/local/bin/pswdb
$ podman run --it --rm --entrypoint /usr/local/bin/pswdb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pswdb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanwise

```bash
$ singularity exec <container> /usr/local/bin/scanwise
$ podman run --it --rm --entrypoint /usr/local/bin/scanwise   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanwise   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanwise_server

```bash
$ singularity exec <container> /usr/local/bin/scanwise_server
$ podman run --it --rm --entrypoint /usr/local/bin/scanwise_server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanwise_server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _aaindexextract

```bash
$ singularity exec <container> /usr/local/bin/_aaindexextract
$ podman run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_aaindexextract   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _abiview

```bash
$ singularity exec <container> /usr/local/bin/_abiview
$ podman run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_abiview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdc

```bash
$ singularity exec <container> /usr/local/bin/_acdc
$ podman run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdpretty

```bash
$ singularity exec <container> /usr/local/bin/_acdpretty
$ podman run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdpretty   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtable

```bash
$ singularity exec <container> /usr/local/bin/_acdtable
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtable   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdtrace

```bash
$ singularity exec <container> /usr/local/bin/_acdtrace
$ podman run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _acdvalid

```bash
$ singularity exec <container> /usr/local/bin/_acdvalid
$ podman run --it --rm --entrypoint /usr/local/bin/_acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_acdvalid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _antigenic

```bash
$ singularity exec <container> /usr/local/bin/_antigenic
$ podman run --it --rm --entrypoint /usr/local/bin/_antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_antigenic   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### _backtranambig

```bash
$ singularity exec <container> /usr/local/bin/_backtranambig
$ podman run --it --rm --entrypoint /usr/local/bin/_backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_backtranambig   -v ${PWD} -w ${PWD} <container> -c " $@"
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