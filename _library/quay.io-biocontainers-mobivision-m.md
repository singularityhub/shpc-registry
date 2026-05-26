---
layout: container
name:  "quay.io/biocontainers/mobivision-m"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mobivision-m/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mobivision-m/container.yaml"
updated_at: "2026-05-26 21:53:58.248340"
latest: "1.3.2--py38hdfd78af_0"
container_url: "https://biocontainers.pro/tools/mobivision-m"
aliases:
 - "STAR-avx"
 - "STAR-avx2"
 - "STAR-plain"
 - "STAR-sse3"
 - "STAR-sse4.1"
 - "STAR-ssse3"
 - "STARlong-avx"
 - "STARlong-avx2"
 - "STARlong-plain"
 - "STARlong-sse3"
 - "STARlong-sse4.1"
 - "STARlong-ssse3"
 - "fetch_multihit"
 - "main_pre-process"
 - "mobivision-M"
 - "STAR"
 - "STARlong"
 - "fastp"
 - "mako-render"
 - "fastqc"
 - "cutadapt"
 - "cmpfillin"
 - "gpmetis"
 - "graphchk"
 - "m2gmetis"
 - "mpmetis"
 - "ndmetis"
 - "igraph"
 - "scanpy"
 - "h5tools_test_utils"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "h5fuse.sh"
 - "igzip"
 - "pigz"
 - "unpigz"
 - "jpackage"
 - "annot-tsv"
 - "natsort"
versions:
 - "1.3.2--py38hdfd78af_0"
description: "singularity registry hpc automated addition for mobivision-m"
config: {"url": "https://biocontainers.pro/tools/mobivision-m", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for mobivision-m", "latest": {"1.3.2--py38hdfd78af_0": "sha256:bb12584c253a1fa33c5f4ffd5bb07adebfce84c7a1ce166b3abd472ec4b856da"}, "tags": {"1.3.2--py38hdfd78af_0": "sha256:bb12584c253a1fa33c5f4ffd5bb07adebfce84c7a1ce166b3abd472ec4b856da"}, "docker": "quay.io/biocontainers/mobivision-m", "aliases": {"STAR-avx": "/usr/local/bin/STAR-avx", "STAR-avx2": "/usr/local/bin/STAR-avx2", "STAR-plain": "/usr/local/bin/STAR-plain", "STAR-sse3": "/usr/local/bin/STAR-sse3", "STAR-sse4.1": "/usr/local/bin/STAR-sse4.1", "STAR-ssse3": "/usr/local/bin/STAR-ssse3", "STARlong-avx": "/usr/local/bin/STARlong-avx", "STARlong-avx2": "/usr/local/bin/STARlong-avx2", "STARlong-plain": "/usr/local/bin/STARlong-plain", "STARlong-sse3": "/usr/local/bin/STARlong-sse3", "STARlong-sse4.1": "/usr/local/bin/STARlong-sse4.1", "STARlong-ssse3": "/usr/local/bin/STARlong-ssse3", "fetch_multihit": "/usr/local/bin/fetch_multihit", "main_pre-process": "/usr/local/bin/main_pre-process", "mobivision-M": "/usr/local/bin/mobivision-M", "STAR": "/usr/local/bin/STAR", "STARlong": "/usr/local/bin/STARlong", "fastp": "/usr/local/bin/fastp", "mako-render": "/usr/local/bin/mako-render", "fastqc": "/usr/local/bin/fastqc", "cutadapt": "/usr/local/bin/cutadapt", "cmpfillin": "/usr/local/bin/cmpfillin", "gpmetis": "/usr/local/bin/gpmetis", "graphchk": "/usr/local/bin/graphchk", "m2gmetis": "/usr/local/bin/m2gmetis", "mpmetis": "/usr/local/bin/mpmetis", "ndmetis": "/usr/local/bin/ndmetis", "igraph": "/usr/local/bin/igraph", "scanpy": "/usr/local/bin/scanpy", "h5tools_test_utils": "/usr/local/bin/h5tools_test_utils", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "h5fuse.sh": "/usr/local/bin/h5fuse.sh", "igzip": "/usr/local/bin/igzip", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "jpackage": "/usr/local/bin/jpackage", "annot-tsv": "/usr/local/bin/annot-tsv", "natsort": "/usr/local/bin/natsort"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mobivision-m.
singularity registry hpc automated addition for mobivision-m
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mobivision-m
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mobivision-m:1.3.2--py38hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mobivision-m/1.3.2--py38hdfd78af_0
$ module help quay.io/biocontainers/mobivision-m/1.3.2--py38hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mobivision-m-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mobivision-m-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mobivision-m-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mobivision-m-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mobivision-m-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mobivision-m-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### STAR-avx

```bash
$ singularity exec <container> /usr/local/bin/STAR-avx
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-avx2

```bash
$ singularity exec <container> /usr/local/bin/STAR-avx2
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-plain

```bash
$ singularity exec <container> /usr/local/bin/STAR-plain
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-sse3

```bash
$ singularity exec <container> /usr/local/bin/STAR-sse3
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-sse4.1

```bash
$ singularity exec <container> /usr/local/bin/STAR-sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR-ssse3

```bash
$ singularity exec <container> /usr/local/bin/STAR-ssse3
$ podman run --it --rm --entrypoint /usr/local/bin/STAR-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-avx

```bash
$ singularity exec <container> /usr/local/bin/STARlong-avx
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-avx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-avx2

```bash
$ singularity exec <container> /usr/local/bin/STARlong-avx2
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-avx2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-plain

```bash
$ singularity exec <container> /usr/local/bin/STARlong-plain
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-plain   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-sse3

```bash
$ singularity exec <container> /usr/local/bin/STARlong-sse3
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-sse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-sse4.1

```bash
$ singularity exec <container> /usr/local/bin/STARlong-sse4.1
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-sse4.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong-ssse3

```bash
$ singularity exec <container> /usr/local/bin/STARlong-ssse3
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong-ssse3   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fetch_multihit

```bash
$ singularity exec <container> /usr/local/bin/fetch_multihit
$ podman run --it --rm --entrypoint /usr/local/bin/fetch_multihit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fetch_multihit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### main_pre-process

```bash
$ singularity exec <container> /usr/local/bin/main_pre-process
$ podman run --it --rm --entrypoint /usr/local/bin/main_pre-process   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/main_pre-process   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mobivision-M

```bash
$ singularity exec <container> /usr/local/bin/mobivision-M
$ podman run --it --rm --entrypoint /usr/local/bin/mobivision-M   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mobivision-M   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STAR

```bash
$ singularity exec <container> /usr/local/bin/STAR
$ podman run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STAR   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### STARlong

```bash
$ singularity exec <container> /usr/local/bin/STARlong
$ podman run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/STARlong   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastp

```bash
$ singularity exec <container> /usr/local/bin/fastp
$ podman run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mako-render

```bash
$ singularity exec <container> /usr/local/bin/mako-render
$ podman run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mako-render   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastqc

```bash
$ singularity exec <container> /usr/local/bin/fastqc
$ podman run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmpfillin

```bash
$ singularity exec <container> /usr/local/bin/cmpfillin
$ podman run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmpfillin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gpmetis

```bash
$ singularity exec <container> /usr/local/bin/gpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### graphchk

```bash
$ singularity exec <container> /usr/local/bin/graphchk
$ podman run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/graphchk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### m2gmetis

```bash
$ singularity exec <container> /usr/local/bin/m2gmetis
$ podman run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/m2gmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpmetis

```bash
$ singularity exec <container> /usr/local/bin/mpmetis
$ podman run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ndmetis

```bash
$ singularity exec <container> /usr/local/bin/ndmetis
$ podman run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ndmetis   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igraph

```bash
$ singularity exec <container> /usr/local/bin/igraph
$ podman run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igraph   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scanpy

```bash
$ singularity exec <container> /usr/local/bin/scanpy
$ podman run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scanpy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5tools_test_utils

```bash
$ singularity exec <container> /usr/local/bin/h5tools_test_utils
$ podman run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5tools_test_utils   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbunzip2

```bash
$ singularity exec <container> /usr/local/bin/pbunzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbunzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzcat

```bash
$ singularity exec <container> /usr/local/bin/pbzcat
$ podman run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzcat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbzip2

```bash
$ singularity exec <container> /usr/local/bin/pbzip2
$ podman run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbzip2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5fuse.sh

```bash
$ singularity exec <container> /usr/local/bin/h5fuse.sh
$ podman run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5fuse.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pigz

```bash
$ singularity exec <container> /usr/local/bin/pigz
$ podman run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### unpigz

```bash
$ singularity exec <container> /usr/local/bin/unpigz
$ podman run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/unpigz   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### natsort

```bash
$ singularity exec <container> /usr/local/bin/natsort
$ podman run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/natsort   -v ${PWD} -w ${PWD} <container> -c " $@"
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