---
layout: container
name:  "quay.io/biocontainers/parallel-meta-suite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/parallel-meta-suite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/parallel-meta-suite/container.yaml"
updated_at: "2025-03-11 03:17:25.749822"
latest: "1.0--h9948957_5"
container_url: "https://biocontainers.pro/tools/parallel-meta-suite"
aliases:
 - "ExtractRNA.o"
 - "PM-comp-corr"
 - "PM-comp-func"
 - "PM-comp-taxa"
 - "PM-extract-rna"
 - "PM-format-seq"
 - "PM-install"
 - "PM-parallel-meta"
 - "PM-pipeline"
 - "PM-plot-taxa"
 - "PM-predict-func"
 - "PM-predict-func-contribute"
 - "PM-predict-func-nsti"
 - "PM-rand-rare"
 - "PM-rare-curv"
 - "PM-select-func"
 - "PM-select-taxa"
 - "PM-split-seq"
 - "PM-update-taxa"
 - "placeholder"
 - "vsearch"
 - "hmmpgmd_shard"
 - "easel"
 - "esl-mixdchlet"
 - "esl-alimanip"
 - "esl-alimap"
 - "esl-alimask"
 - "esl-alimerge"
 - "esl-alipid"
 - "esl-alirev"
versions:
 - "1.0--h9f5acd7_3"
 - "1.0--h4ac6f70_4"
 - "1.0--h9948957_5"
description: "shpc-registry automated BioContainers addition for parallel-meta-suite"
config: {"url": "https://biocontainers.pro/tools/parallel-meta-suite", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for parallel-meta-suite", "latest": {"1.0--h9948957_5": "sha256:92f4d0b075f867fdf291b85bd2b6d71882cd9c7be677284b0aac490dd83e90bb"}, "tags": {"1.0--h9f5acd7_3": "sha256:d0fc64986df3702c3be1e878aa91d59b174f779fc285d711c48ed8b6823395ec", "1.0--h4ac6f70_4": "sha256:57c3eae5fdec2ed4d80d986cd5c37fdfd6c7a1d9ffe1e3584d0eb9f342ba9c80", "1.0--h9948957_5": "sha256:92f4d0b075f867fdf291b85bd2b6d71882cd9c7be677284b0aac490dd83e90bb"}, "docker": "quay.io/biocontainers/parallel-meta-suite", "aliases": {"ExtractRNA.o": "/usr/local/bin/ExtractRNA.o", "PM-comp-corr": "/usr/local/bin/PM-comp-corr", "PM-comp-func": "/usr/local/bin/PM-comp-func", "PM-comp-taxa": "/usr/local/bin/PM-comp-taxa", "PM-extract-rna": "/usr/local/bin/PM-extract-rna", "PM-format-seq": "/usr/local/bin/PM-format-seq", "PM-install": "/usr/local/bin/PM-install", "PM-parallel-meta": "/usr/local/bin/PM-parallel-meta", "PM-pipeline": "/usr/local/bin/PM-pipeline", "PM-plot-taxa": "/usr/local/bin/PM-plot-taxa", "PM-predict-func": "/usr/local/bin/PM-predict-func", "PM-predict-func-contribute": "/usr/local/bin/PM-predict-func-contribute", "PM-predict-func-nsti": "/usr/local/bin/PM-predict-func-nsti", "PM-rand-rare": "/usr/local/bin/PM-rand-rare", "PM-rare-curv": "/usr/local/bin/PM-rare-curv", "PM-select-func": "/usr/local/bin/PM-select-func", "PM-select-taxa": "/usr/local/bin/PM-select-taxa", "PM-split-seq": "/usr/local/bin/PM-split-seq", "PM-update-taxa": "/usr/local/bin/PM-update-taxa", "placeholder": "/usr/local/bin/placeholder", "vsearch": "/usr/local/bin/vsearch", "hmmpgmd_shard": "/usr/local/bin/hmmpgmd_shard", "easel": "/usr/local/bin/easel", "esl-mixdchlet": "/usr/local/bin/esl-mixdchlet", "esl-alimanip": "/usr/local/bin/esl-alimanip", "esl-alimap": "/usr/local/bin/esl-alimap", "esl-alimask": "/usr/local/bin/esl-alimask", "esl-alimerge": "/usr/local/bin/esl-alimerge", "esl-alipid": "/usr/local/bin/esl-alipid", "esl-alirev": "/usr/local/bin/esl-alirev"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/parallel-meta-suite.
shpc-registry automated BioContainers addition for parallel-meta-suite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/parallel-meta-suite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/parallel-meta-suite:1.0--h9948957_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/parallel-meta-suite/1.0--h9948957_5
$ module help quay.io/biocontainers/parallel-meta-suite/1.0--h9948957_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### parallel-meta-suite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### parallel-meta-suite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### parallel-meta-suite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### parallel-meta-suite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### parallel-meta-suite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### parallel-meta-suite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ExtractRNA.o

```bash
$ singularity exec <container> /usr/local/bin/ExtractRNA.o
$ podman run --it --rm --entrypoint /usr/local/bin/ExtractRNA.o   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ExtractRNA.o   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-comp-corr

```bash
$ singularity exec <container> /usr/local/bin/PM-comp-corr
$ podman run --it --rm --entrypoint /usr/local/bin/PM-comp-corr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-comp-corr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-comp-func

```bash
$ singularity exec <container> /usr/local/bin/PM-comp-func
$ podman run --it --rm --entrypoint /usr/local/bin/PM-comp-func   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-comp-func   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-comp-taxa

```bash
$ singularity exec <container> /usr/local/bin/PM-comp-taxa
$ podman run --it --rm --entrypoint /usr/local/bin/PM-comp-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-comp-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-extract-rna

```bash
$ singularity exec <container> /usr/local/bin/PM-extract-rna
$ podman run --it --rm --entrypoint /usr/local/bin/PM-extract-rna   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-extract-rna   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-format-seq

```bash
$ singularity exec <container> /usr/local/bin/PM-format-seq
$ podman run --it --rm --entrypoint /usr/local/bin/PM-format-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-format-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-install

```bash
$ singularity exec <container> /usr/local/bin/PM-install
$ podman run --it --rm --entrypoint /usr/local/bin/PM-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-parallel-meta

```bash
$ singularity exec <container> /usr/local/bin/PM-parallel-meta
$ podman run --it --rm --entrypoint /usr/local/bin/PM-parallel-meta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-parallel-meta   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-pipeline

```bash
$ singularity exec <container> /usr/local/bin/PM-pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/PM-pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-plot-taxa

```bash
$ singularity exec <container> /usr/local/bin/PM-plot-taxa
$ podman run --it --rm --entrypoint /usr/local/bin/PM-plot-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-plot-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-predict-func

```bash
$ singularity exec <container> /usr/local/bin/PM-predict-func
$ podman run --it --rm --entrypoint /usr/local/bin/PM-predict-func   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-predict-func   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-predict-func-contribute

```bash
$ singularity exec <container> /usr/local/bin/PM-predict-func-contribute
$ podman run --it --rm --entrypoint /usr/local/bin/PM-predict-func-contribute   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-predict-func-contribute   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-predict-func-nsti

```bash
$ singularity exec <container> /usr/local/bin/PM-predict-func-nsti
$ podman run --it --rm --entrypoint /usr/local/bin/PM-predict-func-nsti   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-predict-func-nsti   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-rand-rare

```bash
$ singularity exec <container> /usr/local/bin/PM-rand-rare
$ podman run --it --rm --entrypoint /usr/local/bin/PM-rand-rare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-rand-rare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-rare-curv

```bash
$ singularity exec <container> /usr/local/bin/PM-rare-curv
$ podman run --it --rm --entrypoint /usr/local/bin/PM-rare-curv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-rare-curv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-select-func

```bash
$ singularity exec <container> /usr/local/bin/PM-select-func
$ podman run --it --rm --entrypoint /usr/local/bin/PM-select-func   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-select-func   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-select-taxa

```bash
$ singularity exec <container> /usr/local/bin/PM-select-taxa
$ podman run --it --rm --entrypoint /usr/local/bin/PM-select-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-select-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-split-seq

```bash
$ singularity exec <container> /usr/local/bin/PM-split-seq
$ podman run --it --rm --entrypoint /usr/local/bin/PM-split-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-split-seq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### PM-update-taxa

```bash
$ singularity exec <container> /usr/local/bin/PM-update-taxa
$ podman run --it --rm --entrypoint /usr/local/bin/PM-update-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/PM-update-taxa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### placeholder

```bash
$ singularity exec <container> /usr/local/bin/placeholder
$ podman run --it --rm --entrypoint /usr/local/bin/placeholder   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/placeholder   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vsearch

```bash
$ singularity exec <container> /usr/local/bin/vsearch
$ podman run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vsearch   -v ${PWD} -w ${PWD} <container> -c " $@"
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