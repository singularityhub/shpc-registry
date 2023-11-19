---
layout: container
name:  "quay.io/biocontainers/kmasker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/kmasker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/kmasker/container.yaml"
updated_at: "2023-11-19 03:00:32.667775"
latest: "1.1.1--py39pl5321r42h1f90b4d_6"
container_url: "https://biocontainers.pro/tools/kmasker"
aliases:
 - "Kmasker"
 - "cmasker"
 - "fastq-clipper"
 - "fastq-join"
 - "fastq-mcf"
 - "fastq-multx"
 - "fastq-stats"
 - "gffread"
 - "which"
 - "jemalloc-config"
 - "jeprof"
 - "jemalloc.sh"
 - "jellyfish"
 - "basenc"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
versions:
 - "1.1.1--py38pl5321r41h4a32c8e_4"
 - "1.1.1--py36pl5321r42h2ad2d48_5"
 - "1.1.1--py39pl5321r42h1f90b4d_6"
description: "shpc-registry automated BioContainers addition for kmasker"
config: {"url": "https://biocontainers.pro/tools/kmasker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for kmasker", "latest": {"1.1.1--py39pl5321r42h1f90b4d_6": "sha256:5c34dbf1868eb689a6693cef545c4ab27af2a484a0a690ff73a4481dcaff6121"}, "tags": {"1.1.1--py38pl5321r41h4a32c8e_4": "sha256:ede1044175023763cec1c569a63c7d1fa6e19d5cfb1110795f30f70bb297b0dc", "1.1.1--py36pl5321r42h2ad2d48_5": "sha256:2f8db110b6cfd86a522b46ea3398097be1cc0f203c99714f874d96e9f44df57c", "1.1.1--py39pl5321r42h1f90b4d_6": "sha256:5c34dbf1868eb689a6693cef545c4ab27af2a484a0a690ff73a4481dcaff6121"}, "docker": "quay.io/biocontainers/kmasker", "aliases": {"Kmasker": "/usr/local/bin/Kmasker", "cmasker": "/usr/local/bin/cmasker", "fastq-clipper": "/usr/local/bin/fastq-clipper", "fastq-join": "/usr/local/bin/fastq-join", "fastq-mcf": "/usr/local/bin/fastq-mcf", "fastq-multx": "/usr/local/bin/fastq-multx", "fastq-stats": "/usr/local/bin/fastq-stats", "gffread": "/usr/local/bin/gffread", "which": "/usr/local/bin/which", "jemalloc-config": "/usr/local/bin/jemalloc-config", "jeprof": "/usr/local/bin/jeprof", "jemalloc.sh": "/usr/local/bin/jemalloc.sh", "jellyfish": "/usr/local/bin/jellyfish", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/kmasker.
shpc-registry automated BioContainers addition for kmasker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/kmasker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/kmasker:1.1.1--py39pl5321r42h1f90b4d_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/kmasker/1.1.1--py39pl5321r42h1f90b4d_6
$ module help quay.io/biocontainers/kmasker/1.1.1--py39pl5321r42h1f90b4d_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### kmasker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### kmasker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### kmasker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### kmasker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### kmasker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### kmasker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### Kmasker

```bash
$ singularity exec <container> /usr/local/bin/Kmasker
$ podman run --it --rm --entrypoint /usr/local/bin/Kmasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/Kmasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cmasker

```bash
$ singularity exec <container> /usr/local/bin/cmasker
$ podman run --it --rm --entrypoint /usr/local/bin/cmasker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cmasker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-clipper

```bash
$ singularity exec <container> /usr/local/bin/fastq-clipper
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-clipper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-clipper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-join

```bash
$ singularity exec <container> /usr/local/bin/fastq-join
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-join   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-join   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-mcf

```bash
$ singularity exec <container> /usr/local/bin/fastq-mcf
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-mcf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-mcf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-multx

```bash
$ singularity exec <container> /usr/local/bin/fastq-multx
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-multx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-multx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq-stats

```bash
$ singularity exec <container> /usr/local/bin/fastq-stats
$ podman run --it --rm --entrypoint /usr/local/bin/fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq-stats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gffread

```bash
$ singularity exec <container> /usr/local/bin/gffread
$ podman run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffread   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### which

```bash
$ singularity exec <container> /usr/local/bin/which
$ podman run --it --rm --entrypoint /usr/local/bin/which   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/which   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc-config

```bash
$ singularity exec <container> /usr/local/bin/jemalloc-config
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jeprof

```bash
$ singularity exec <container> /usr/local/bin/jeprof
$ podman run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jeprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jemalloc.sh

```bash
$ singularity exec <container> /usr/local/bin/jemalloc.sh
$ podman run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jemalloc.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jellyfish

```bash
$ singularity exec <container> /usr/local/bin/jellyfish
$ podman run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jellyfish   -v ${PWD} -w ${PWD} <container> -c " $@"
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