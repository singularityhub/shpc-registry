---
layout: container
name:  "quay.io/biocontainers/hg-color"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hg-color/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hg-color/container.yaml"
updated_at: "2023-05-19 02:38:00.810295"
latest: "1.1.1--he1b5a44_1"
container_url: "https://biocontainers.pro/tools/hg-color"
aliases:
 - "HG-CoLoR"
 - "PgSAgen"
 - "PgSAtest"
 - "blasr"
 - "blasr-license"
 - "filterShortReads.py"
 - "formatLongReads.py"
 - "merge_mate_pairs"
 - "quorum"
 - "quorum_create_database"
 - "quorum_error_correct_reads"
 - "split.py"
 - "split_mate_pairs"
 - "trim.py"
 - "_aaindexextract"
 - "_abiview"
 - "_acdc"
 - "_acdpretty"
 - "_acdtable"
 - "_acdtrace"
 - "_acdvalid"
 - "_antigenic"
 - "_backtranambig"
 - "_backtranseq"
versions:
 - "1.1.1--he1b5a44_1"
description: "shpc-registry automated BioContainers addition for hg-color"
config: {"url": "https://biocontainers.pro/tools/hg-color", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hg-color", "latest": {"1.1.1--he1b5a44_1": "sha256:9faf64eab37610f50de2823bb1e0767ccd2625428395913eb257e07911330df7"}, "tags": {"1.1.1--he1b5a44_1": "sha256:9faf64eab37610f50de2823bb1e0767ccd2625428395913eb257e07911330df7"}, "docker": "quay.io/biocontainers/hg-color", "aliases": {"HG-CoLoR": "/usr/local/bin/HG-CoLoR", "PgSAgen": "/usr/local/bin/PgSAgen", "PgSAtest": "/usr/local/bin/PgSAtest", "blasr": "/usr/local/bin/blasr", "blasr-license": "/usr/local/bin/blasr-license", "filterShortReads.py": "/usr/local/bin/filterShortReads.py", "formatLongReads.py": "/usr/local/bin/formatLongReads.py", "merge_mate_pairs": "/usr/local/bin/merge_mate_pairs", "quorum": "/usr/local/bin/quorum", "quorum_create_database": "/usr/local/bin/quorum_create_database", "quorum_error_correct_reads": "/usr/local/bin/quorum_error_correct_reads", "split.py": "/usr/local/bin/split.py", "split_mate_pairs": "/usr/local/bin/split_mate_pairs", "trim.py": "/usr/local/bin/trim.py", "_aaindexextract": "/usr/local/bin/_aaindexextract", "_abiview": "/usr/local/bin/_abiview", "_acdc": "/usr/local/bin/_acdc", "_acdpretty": "/usr/local/bin/_acdpretty", "_acdtable": "/usr/local/bin/_acdtable", "_acdtrace": "/usr/local/bin/_acdtrace", "_acdvalid": "/usr/local/bin/_acdvalid", "_antigenic": "/usr/local/bin/_antigenic", "_backtranambig": "/usr/local/bin/_backtranambig", "_backtranseq": "/usr/local/bin/_backtranseq"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hg-color.
shpc-registry automated BioContainers addition for hg-color
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hg-color
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hg-color:1.1.1--he1b5a44_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hg-color/1.1.1--he1b5a44_1
$ module help quay.io/biocontainers/hg-color/1.1.1--he1b5a44_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hg-color-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hg-color-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hg-color-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hg-color-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hg-color-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hg-color-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### HG-CoLoR

```bash
$ singularity exec <container> /usr/local/bin/HG-CoLoR
$ podman run --it --rm --entrypoint /usr/local/bin/HG-CoLoR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/HG-CoLoR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PgSAgen

```bash
$ singularity exec <container> /usr/local/bin/PgSAgen
$ podman run --it --rm --entrypoint /usr/local/bin/PgSAgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PgSAgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PgSAtest

```bash
$ singularity exec <container> /usr/local/bin/PgSAtest
$ podman run --it --rm --entrypoint /usr/local/bin/PgSAtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PgSAtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blasr

```bash
$ singularity exec <container> /usr/local/bin/blasr
$ podman run --it --rm --entrypoint /usr/local/bin/blasr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blasr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blasr-license

```bash
$ singularity exec <container> /usr/local/bin/blasr-license
$ podman run --it --rm --entrypoint /usr/local/bin/blasr-license   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blasr-license   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filterShortReads.py

```bash
$ singularity exec <container> /usr/local/bin/filterShortReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/filterShortReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filterShortReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### formatLongReads.py

```bash
$ singularity exec <container> /usr/local/bin/formatLongReads.py
$ podman run --it --rm --entrypoint /usr/local/bin/formatLongReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/formatLongReads.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merge_mate_pairs

```bash
$ singularity exec <container> /usr/local/bin/merge_mate_pairs
$ podman run --it --rm --entrypoint /usr/local/bin/merge_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merge_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum

```bash
$ singularity exec <container> /usr/local/bin/quorum
$ podman run --it --rm --entrypoint /usr/local/bin/quorum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum_create_database

```bash
$ singularity exec <container> /usr/local/bin/quorum_create_database
$ podman run --it --rm --entrypoint /usr/local/bin/quorum_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum_create_database   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### quorum_error_correct_reads

```bash
$ singularity exec <container> /usr/local/bin/quorum_error_correct_reads
$ podman run --it --rm --entrypoint /usr/local/bin/quorum_error_correct_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/quorum_error_correct_reads   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split.py

```bash
$ singularity exec <container> /usr/local/bin/split.py
$ podman run --it --rm --entrypoint /usr/local/bin/split.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### split_mate_pairs

```bash
$ singularity exec <container> /usr/local/bin/split_mate_pairs
$ podman run --it --rm --entrypoint /usr/local/bin/split_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/split_mate_pairs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trim.py

```bash
$ singularity exec <container> /usr/local/bin/trim.py
$ podman run --it --rm --entrypoint /usr/local/bin/trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trim.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### _backtranseq

```bash
$ singularity exec <container> /usr/local/bin/_backtranseq
$ podman run --it --rm --entrypoint /usr/local/bin/_backtranseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/_backtranseq   -v ${PWD} -w ${PWD} <container> -c " $@"
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