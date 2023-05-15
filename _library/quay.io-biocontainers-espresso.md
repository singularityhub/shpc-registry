---
layout: container
name:  "quay.io/biocontainers/espresso"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/espresso/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/espresso/container.yaml"
updated_at: "2023-05-15 03:30:02.320005"
latest: "1.3.2--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/espresso"
aliases:
 - "ESPRESSO_C.pl"
 - "ESPRESSO_Q.pl"
 - "ESPRESSO_Q_Thread.pm"
 - "ESPRESSO_S.pl"
 - "ESPRESSO_Version.pm"
 - "test_pcre"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
 - "edirect.py"
 - "filter-columns"
 - "fuse-segments"
 - "gene2range"
 - "tbl2prod"
 - "uniq-table"
 - "esl-alimanip"
 - "esl-alimap"
 - "esl-alimask"
 - "esl-alimerge"
 - "esl-alipid"
 - "esl-alirev"
 - "esl-alistat"
 - "esl-compalign"
 - "esl-compstruct"
 - "esl-construct"
 - "esl-histplot"
 - "esl-mask"
 - "esl-selectn"
 - "esl-seqrange"
 - "esl-seqstat"
versions:
 - "1.3.2--hdfd78af_0"
description: "singularity registry hpc automated addition for espresso"
config: {"url": "https://biocontainers.pro/tools/espresso", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for espresso", "latest": {"1.3.2--hdfd78af_0": "sha256:4126f39e6222756ec536e6d39beee6427500d32ae32ff6ee48e6385c2dfc3754"}, "tags": {"1.3.2--hdfd78af_0": "sha256:4126f39e6222756ec536e6d39beee6427500d32ae32ff6ee48e6385c2dfc3754"}, "docker": "quay.io/biocontainers/espresso", "aliases": {"ESPRESSO_C.pl": "/usr/local/bin/ESPRESSO_C.pl", "ESPRESSO_Q.pl": "/usr/local/bin/ESPRESSO_Q.pl", "ESPRESSO_Q_Thread.pm": "/usr/local/bin/ESPRESSO_Q_Thread.pm", "ESPRESSO_S.pl": "/usr/local/bin/ESPRESSO_S.pl", "ESPRESSO_Version.pm": "/usr/local/bin/ESPRESSO_Version.pm", "test_pcre": "/usr/local/bin/test_pcre", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "edirect.py": "/usr/local/bin/edirect.py", "filter-columns": "/usr/local/bin/filter-columns", "fuse-segments": "/usr/local/bin/fuse-segments", "gene2range": "/usr/local/bin/gene2range", "tbl2prod": "/usr/local/bin/tbl2prod", "uniq-table": "/usr/local/bin/uniq-table", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev", "esl-alistat": "/usr/local/bin/esl-alistat", "esl-compalign": "/usr/local/bin/esl-compalign", "esl-compstruct": "/usr/local/bin/esl-compstruct", "esl-construct": "/usr/local/bin/esl-construct", "esl-histplot": "/usr/local/bin/esl-histplot", "esl-mask": "/usr/local/bin/esl-mask", "esl-selectn": "/usr/local/bin/esl-selectn", "esl-seqrange": "/usr/local/bin/esl-seqrange", "esl-seqstat": "/usr/local/bin/esl-seqstat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/espresso.
singularity registry hpc automated addition for espresso
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/espresso
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/espresso:1.3.2--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/espresso/1.3.2--hdfd78af_0
$ module help quay.io/biocontainers/espresso/1.3.2--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### espresso-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### espresso-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### espresso-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### espresso-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### espresso-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### espresso-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ESPRESSO_C.pl

```bash
$ singularity exec <container> /usr/local/bin/ESPRESSO_C.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ESPRESSO_C.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESPRESSO_C.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESPRESSO_Q.pl

```bash
$ singularity exec <container> /usr/local/bin/ESPRESSO_Q.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ESPRESSO_Q.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESPRESSO_Q.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESPRESSO_Q_Thread.pm

```bash
$ singularity exec <container> /usr/local/bin/ESPRESSO_Q_Thread.pm
$ podman run --it --rm --entrypoint /usr/local/bin/ESPRESSO_Q_Thread.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESPRESSO_Q_Thread.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESPRESSO_S.pl

```bash
$ singularity exec <container> /usr/local/bin/ESPRESSO_S.pl
$ podman run --it --rm --entrypoint /usr/local/bin/ESPRESSO_S.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESPRESSO_S.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ESPRESSO_Version.pm

```bash
$ singularity exec <container> /usr/local/bin/ESPRESSO_Version.pm
$ podman run --it --rm --entrypoint /usr/local/bin/ESPRESSO_Version.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ESPRESSO_Version.pm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### test_pcre

```bash
$ singularity exec <container> /usr/local/bin/test_pcre
$ podman run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/test_pcre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmpgmd_shard

```bash
$ singularity exec <container> /usr/local/bin/hmmpgmd_shard
$ podman run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmpgmd_shard   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easel

```bash
$ singularity exec <container> /usr/local/bin/easel
$ podman run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mixdchlet

```bash
$ singularity exec <container> /usr/local/bin/esl-mixdchlet
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mixdchlet   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### edirect.py

```bash
$ singularity exec <container> /usr/local/bin/edirect.py
$ podman run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edirect.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### filter-columns

```bash
$ singularity exec <container> /usr/local/bin/filter-columns
$ podman run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/filter-columns   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fuse-segments

```bash
$ singularity exec <container> /usr/local/bin/fuse-segments
$ podman run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fuse-segments   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gene2range

```bash
$ singularity exec <container> /usr/local/bin/gene2range
$ podman run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene2range   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tbl2prod

```bash
$ singularity exec <container> /usr/local/bin/tbl2prod
$ podman run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tbl2prod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### uniq-table

```bash
$ singularity exec <container> /usr/local/bin/uniq-table
$ podman run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uniq-table   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimanip

```bash
$ singularity exec <container> /usr/local/bin/esl-alimanip
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimanip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimap

```bash
$ singularity exec <container> /usr/local/bin/esl-alimap
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimap   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimask

```bash
$ singularity exec <container> /usr/local/bin/esl-alimask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alimerge

```bash
$ singularity exec <container> /usr/local/bin/esl-alimerge
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alimerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alipid

```bash
$ singularity exec <container> /usr/local/bin/esl-alipid
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alipid   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alirev

```bash
$ singularity exec <container> /usr/local/bin/esl-alirev
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alirev   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-alistat

```bash
$ singularity exec <container> /usr/local/bin/esl-alistat
$ podman run --it --rm --entrypoint /usr/local/bin/esl-alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-alistat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-compalign

```bash
$ singularity exec <container> /usr/local/bin/esl-compalign
$ podman run --it --rm --entrypoint /usr/local/bin/esl-compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-compalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-compstruct

```bash
$ singularity exec <container> /usr/local/bin/esl-compstruct
$ podman run --it --rm --entrypoint /usr/local/bin/esl-compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-compstruct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-construct

```bash
$ singularity exec <container> /usr/local/bin/esl-construct
$ podman run --it --rm --entrypoint /usr/local/bin/esl-construct   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-construct   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-histplot

```bash
$ singularity exec <container> /usr/local/bin/esl-histplot
$ podman run --it --rm --entrypoint /usr/local/bin/esl-histplot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-histplot   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-mask

```bash
$ singularity exec <container> /usr/local/bin/esl-mask
$ podman run --it --rm --entrypoint /usr/local/bin/esl-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-mask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-selectn

```bash
$ singularity exec <container> /usr/local/bin/esl-selectn
$ podman run --it --rm --entrypoint /usr/local/bin/esl-selectn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-selectn   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-seqrange

```bash
$ singularity exec <container> /usr/local/bin/esl-seqrange
$ podman run --it --rm --entrypoint /usr/local/bin/esl-seqrange   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-seqrange   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### esl-seqstat

```bash
$ singularity exec <container> /usr/local/bin/esl-seqstat
$ podman run --it --rm --entrypoint /usr/local/bin/esl-seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/esl-seqstat   -v ${PWD} -w ${PWD} <container> -c " $@"
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