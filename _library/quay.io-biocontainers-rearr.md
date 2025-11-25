---
layout: container
name:  "quay.io/biocontainers/rearr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rearr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rearr/container.yaml"
updated_at: "2025-11-25 03:36:34.262670"
latest: "1.0.3--h9948957_0"
container_url: "https://biocontainers.pro/tools/rearr"
aliases:
 - "getSxCsvFileTarget.pl"
 - "getSxRefFile.pl"
 - "rearrangement"
 - "gawk-5.3.1"
 - "cutadapt"
 - "gawkbug"
 - "pbunzip2"
 - "pbzcat"
 - "pbzip2"
 - "igzip"
 - "annot-tsv"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
 - "awk"
 - "gawk"
 - "pigz"
 - "unpigz"
 - "numpy-config"
 - "shiftBed"
 - "annotateBed"
 - "bamToBed"
versions:
 - "1.0.0--h9948957_0"
 - "1.0.1--h9948957_0"
 - "1.0.3--h9948957_0"
description: "singularity registry hpc automated addition for rearr"
config: {"url": "https://biocontainers.pro/tools/rearr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for rearr", "latest": {"1.0.3--h9948957_0": "sha256:79f983ef0a6dd82e0ff1dbf6da9884c0f65cebbdb4d4231274dc3e21a6dc6767"}, "tags": {"1.0.0--h9948957_0": "sha256:e3328abb7bb1e1eadd7c562c865d9389b0c8664b77c2834fbee3e4abda842867", "1.0.1--h9948957_0": "sha256:6226569326216c25733d53f7211f93053c0335ff0a9c5891e216a83fea9a69e7", "1.0.3--h9948957_0": "sha256:79f983ef0a6dd82e0ff1dbf6da9884c0f65cebbdb4d4231274dc3e21a6dc6767"}, "docker": "quay.io/biocontainers/rearr", "aliases": {"getSxCsvFileTarget.pl": "/usr/local/bin/getSxCsvFileTarget.pl", "getSxRefFile.pl": "/usr/local/bin/getSxRefFile.pl", "rearrangement": "/usr/local/bin/rearrangement", "gawk-5.3.1": "/usr/local/bin/gawk-5.3.1", "cutadapt": "/usr/local/bin/cutadapt", "gawkbug": "/usr/local/bin/gawkbug", "pbunzip2": "/usr/local/bin/pbunzip2", "pbzcat": "/usr/local/bin/pbzcat", "pbzip2": "/usr/local/bin/pbzip2", "igzip": "/usr/local/bin/igzip", "annot-tsv": "/usr/local/bin/annot-tsv", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s", "awk": "/usr/local/bin/awk", "gawk": "/usr/local/bin/gawk", "pigz": "/usr/local/bin/pigz", "unpigz": "/usr/local/bin/unpigz", "numpy-config": "/usr/local/bin/numpy-config", "shiftBed": "/usr/local/bin/shiftBed", "annotateBed": "/usr/local/bin/annotateBed", "bamToBed": "/usr/local/bin/bamToBed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rearr.
singularity registry hpc automated addition for rearr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rearr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rearr:1.0.3--h9948957_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rearr/1.0.3--h9948957_0
$ module help quay.io/biocontainers/rearr/1.0.3--h9948957_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rearr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rearr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rearr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rearr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rearr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rearr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### getSxCsvFileTarget.pl

```bash
$ singularity exec <container> /usr/local/bin/getSxCsvFileTarget.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getSxCsvFileTarget.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getSxCsvFileTarget.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getSxRefFile.pl

```bash
$ singularity exec <container> /usr/local/bin/getSxRefFile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/getSxRefFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getSxRefFile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rearrangement

```bash
$ singularity exec <container> /usr/local/bin/rearrangement
$ podman run --it --rm --entrypoint /usr/local/bin/rearrangement   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rearrangement   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk-5.3.1

```bash
$ singularity exec <container> /usr/local/bin/gawk-5.3.1
$ podman run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk-5.3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cutadapt

```bash
$ singularity exec <container> /usr/local/bin/cutadapt
$ podman run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cutadapt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawkbug

```bash
$ singularity exec <container> /usr/local/bin/gawkbug
$ podman run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawkbug   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### igzip

```bash
$ singularity exec <container> /usr/local/bin/igzip
$ podman run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annot-tsv

```bash
$ singularity exec <container> /usr/local/bin/annot-tsv
$ podman run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annot-tsv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2

```bash
$ singularity exec <container> /usr/local/bin/bowtie2
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie2-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### awk

```bash
$ singularity exec <container> /usr/local/bin/awk
$ podman run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/awk   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gawk

```bash
$ singularity exec <container> /usr/local/bin/gawk
$ podman run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shiftBed

```bash
$ singularity exec <container> /usr/local/bin/shiftBed
$ podman run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shiftBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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