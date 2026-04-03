---
layout: container
name:  "quay.io/biocontainers/aakomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/aakomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/aakomp/container.yaml"
updated_at: "2026-04-03 04:37:00.483171"
latest: "1.0.0--py312r45hf426362_0"
container_url: "https://biocontainers.pro/tools/aakomp"
aliases:
 - "aakomp"
 - "aakomp_plot.R"
 - "libsequenceConfig"
 - "lrz"
 - "make_mibf"
 - "mi_bf_generate"
 - "randseq"
 - "run-aakomp"
 - "indexlr"
 - "lrunzip"
 - "lrzcat"
 - "lrzip"
 - "lrztar"
 - "lrzuntar"
 - "hmmc2"
 - "hmmerfm-exactmatch"
 - "mamba"
 - "mamba-package"
 - "conda2solv"
 - "dumpsolv"
 - "installcheck"
 - "mergesolv"
 - "repo2solv"
 - "testsolv"
 - "bsdunzip"
 - "ref-cache"
 - "bsdcat"
 - "bsdcpio"
 - "bsdtar"
 - "annot-tsv"
 - "alimask"
 - "hmmconvert"
 - "hmmemit"
versions:
 - "1.0.0--py312r45hf426362_0"
description: "singularity registry hpc automated addition for aakomp"
config: {"url": "https://biocontainers.pro/tools/aakomp", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for aakomp", "latest": {"1.0.0--py312r45hf426362_0": "sha256:0e05c6678e93bc747d0ff2b60614a23f72952645e222e09324f662263e9bf0e0"}, "tags": {"1.0.0--py312r45hf426362_0": "sha256:0e05c6678e93bc747d0ff2b60614a23f72952645e222e09324f662263e9bf0e0"}, "docker": "quay.io/biocontainers/aakomp", "aliases": {"aakomp": "/usr/local/bin/aakomp", "aakomp_plot.R": "/usr/local/bin/aakomp_plot.R", "libsequenceConfig": "/usr/local/bin/libsequenceConfig", "lrz": "/usr/local/bin/lrz", "make_mibf": "/usr/local/bin/make_mibf", "mi_bf_generate": "/usr/local/bin/mi_bf_generate", "randseq": "/usr/local/bin/randseq", "run-aakomp": "/usr/local/bin/run-aakomp", "indexlr": "/usr/local/bin/indexlr", "lrunzip": "/usr/local/bin/lrunzip", "lrzcat": "/usr/local/bin/lrzcat", "lrzip": "/usr/local/bin/lrzip", "lrztar": "/usr/local/bin/lrztar", "lrzuntar": "/usr/local/bin/lrzuntar", "hmmc2": "/usr/local/bin/hmmc2", "hmmerfm-exactmatch": "/usr/local/bin/hmmerfm-exactmatch", "mamba": "/usr/local/bin/mamba", "mamba-package": "/usr/local/bin/mamba-package", "conda2solv": "/usr/local/bin/conda2solv", "dumpsolv": "/usr/local/bin/dumpsolv", "installcheck": "/usr/local/bin/installcheck", "mergesolv": "/usr/local/bin/mergesolv", "repo2solv": "/usr/local/bin/repo2solv", "testsolv": "/usr/local/bin/testsolv", "bsdunzip": "/usr/local/bin/bsdunzip", "ref-cache": "/usr/local/bin/ref-cache", "bsdcat": "/usr/local/bin/bsdcat", "bsdcpio": "/usr/local/bin/bsdcpio", "bsdtar": "/usr/local/bin/bsdtar", "annot-tsv": "/usr/local/bin/annot-tsv", "alimask": "/usr/local/bin/alimask", "hmmconvert": "/usr/local/bin/hmmconvert", "hmmemit": "/usr/local/bin/hmmemit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/aakomp.
singularity registry hpc automated addition for aakomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/aakomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/aakomp:1.0.0--py312r45hf426362_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/aakomp/1.0.0--py312r45hf426362_0
$ module help quay.io/biocontainers/aakomp/1.0.0--py312r45hf426362_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aakomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aakomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aakomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aakomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aakomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aakomp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aakomp

```bash
$ singularity exec <container> /usr/local/bin/aakomp
$ podman run --it --rm --entrypoint /usr/local/bin/aakomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aakomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aakomp_plot.R

```bash
$ singularity exec <container> /usr/local/bin/aakomp_plot.R
$ podman run --it --rm --entrypoint /usr/local/bin/aakomp_plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aakomp_plot.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### libsequenceConfig

```bash
$ singularity exec <container> /usr/local/bin/libsequenceConfig
$ podman run --it --rm --entrypoint /usr/local/bin/libsequenceConfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/libsequenceConfig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrz

```bash
$ singularity exec <container> /usr/local/bin/lrz
$ podman run --it --rm --entrypoint /usr/local/bin/lrz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### make_mibf

```bash
$ singularity exec <container> /usr/local/bin/make_mibf
$ podman run --it --rm --entrypoint /usr/local/bin/make_mibf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/make_mibf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mi_bf_generate

```bash
$ singularity exec <container> /usr/local/bin/mi_bf_generate
$ podman run --it --rm --entrypoint /usr/local/bin/mi_bf_generate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mi_bf_generate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### randseq

```bash
$ singularity exec <container> /usr/local/bin/randseq
$ podman run --it --rm --entrypoint /usr/local/bin/randseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/randseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### run-aakomp

```bash
$ singularity exec <container> /usr/local/bin/run-aakomp
$ podman run --it --rm --entrypoint /usr/local/bin/run-aakomp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/run-aakomp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### indexlr

```bash
$ singularity exec <container> /usr/local/bin/indexlr
$ podman run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/indexlr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrunzip

```bash
$ singularity exec <container> /usr/local/bin/lrunzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzcat

```bash
$ singularity exec <container> /usr/local/bin/lrzcat
$ podman run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzip

```bash
$ singularity exec <container> /usr/local/bin/lrzip
$ podman run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrztar

```bash
$ singularity exec <container> /usr/local/bin/lrztar
$ podman run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrztar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lrzuntar

```bash
$ singularity exec <container> /usr/local/bin/lrzuntar
$ podman run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lrzuntar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmc2

```bash
$ singularity exec <container> /usr/local/bin/hmmc2
$ podman run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmc2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmerfm-exactmatch

```bash
$ singularity exec <container> /usr/local/bin/hmmerfm-exactmatch
$ podman run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmerfm-exactmatch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba

```bash
$ singularity exec <container> /usr/local/bin/mamba
$ podman run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conda2solv

```bash
$ singularity exec <container> /usr/local/bin/conda2solv
$ podman run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conda2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dumpsolv

```bash
$ singularity exec <container> /usr/local/bin/dumpsolv
$ podman run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumpsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### installcheck

```bash
$ singularity exec <container> /usr/local/bin/installcheck
$ podman run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/installcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mergesolv

```bash
$ singularity exec <container> /usr/local/bin/mergesolv
$ podman run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mergesolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### repo2solv

```bash
$ singularity exec <container> /usr/local/bin/repo2solv
$ podman run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/repo2solv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testsolv

```bash
$ singularity exec <container> /usr/local/bin/testsolv
$ podman run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testsolv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdunzip

```bash
$ singularity exec <container> /usr/local/bin/bsdunzip
$ podman run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdunzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ref-cache

```bash
$ singularity exec <container> /usr/local/bin/ref-cache
$ podman run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ref-cache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcat

```bash
$ singularity exec <container> /usr/local/bin/bsdcat
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdcpio

```bash
$ singularity exec <container> /usr/local/bin/bsdcpio
$ podman run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdcpio   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bsdtar

```bash
$ singularity exec <container> /usr/local/bin/bsdtar
$ podman run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bsdtar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### alimask

```bash
$ singularity exec <container> /usr/local/bin/alimask
$ podman run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alimask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmconvert

```bash
$ singularity exec <container> /usr/local/bin/hmmconvert
$ podman run --it --rm --entrypoint /usr/local/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmconvert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hmmemit

```bash
$ singularity exec <container> /usr/local/bin/hmmemit
$ podman run --it --rm --entrypoint /usr/local/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hmmemit   -v ${PWD} -w ${PWD} <container> -c " $@"
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