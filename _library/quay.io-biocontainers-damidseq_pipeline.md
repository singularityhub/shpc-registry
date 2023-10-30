---
layout: container
name:  "quay.io/biocontainers/damidseq_pipeline"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/damidseq_pipeline/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/damidseq_pipeline/container.yaml"
updated_at: "2023-10-30 03:42:51.432598"
latest: "1.5.3--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/damidseq_pipeline"
aliases:
 - "damidseq_pipeline"
 - "gatc.track.maker.pl"
 - "gff2tdf.pl"
 - "igvtools"
 - "varfilter.py"
 - "bowtie2"
 - "bowtie2-align-l"
 - "bowtie2-align-s"
 - "bowtie2-build"
 - "bowtie2-build-l"
 - "bowtie2-build-s"
 - "bowtie2-inspect"
 - "bowtie2-inspect-l"
 - "bowtie2-inspect-s"
 - "jaotc"
versions:
 - "1.4--pl5321hdfd78af_5"
 - "1.5.3--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for damidseq_pipeline"
config: {"url": "https://biocontainers.pro/tools/damidseq_pipeline", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for damidseq_pipeline", "latest": {"1.5.3--pl5321hdfd78af_0": "sha256:74d6aa3665ab09cf628a2a159b509b0ebba889189c8733e40c784dd1a779de65"}, "tags": {"1.4--pl5321hdfd78af_5": "sha256:9d79de14d9026b53a3b7b7b586bc4324967c5a0466dbf625d0e6e5e30186444f", "1.5.3--pl5321hdfd78af_0": "sha256:74d6aa3665ab09cf628a2a159b509b0ebba889189c8733e40c784dd1a779de65"}, "docker": "quay.io/biocontainers/damidseq_pipeline", "aliases": {"damidseq_pipeline": "/usr/local/bin/damidseq_pipeline", "gatc.track.maker.pl": "/usr/local/bin/gatc.track.maker.pl", "gff2tdf.pl": "/usr/local/bin/gff2tdf.pl", "igvtools": "/usr/local/bin/igvtools", "varfilter.py": "/usr/local/bin/varfilter.py", "bowtie2": "/usr/local/bin/bowtie2", "bowtie2-align-l": "/usr/local/bin/bowtie2-align-l", "bowtie2-align-s": "/usr/local/bin/bowtie2-align-s", "bowtie2-build": "/usr/local/bin/bowtie2-build", "bowtie2-build-l": "/usr/local/bin/bowtie2-build-l", "bowtie2-build-s": "/usr/local/bin/bowtie2-build-s", "bowtie2-inspect": "/usr/local/bin/bowtie2-inspect", "bowtie2-inspect-l": "/usr/local/bin/bowtie2-inspect-l", "bowtie2-inspect-s": "/usr/local/bin/bowtie2-inspect-s", "jaotc": "/usr/local/bin/jaotc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/damidseq_pipeline.
shpc-registry automated BioContainers addition for damidseq_pipeline
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/damidseq_pipeline
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/damidseq_pipeline:1.5.3--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/damidseq_pipeline/1.5.3--pl5321hdfd78af_0
$ module help quay.io/biocontainers/damidseq_pipeline/1.5.3--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### damidseq_pipeline-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### damidseq_pipeline-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### damidseq_pipeline-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### damidseq_pipeline-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### damidseq_pipeline-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### damidseq_pipeline-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### damidseq_pipeline

```bash
$ singularity exec <container> /usr/local/bin/damidseq_pipeline
$ podman run --it --rm --entrypoint /usr/local/bin/damidseq_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/damidseq_pipeline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gatc.track.maker.pl

```bash
$ singularity exec <container> /usr/local/bin/gatc.track.maker.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gatc.track.maker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gatc.track.maker.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2tdf.pl

```bash
$ singularity exec <container> /usr/local/bin/gff2tdf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff2tdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2tdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### igvtools

```bash
$ singularity exec <container> /usr/local/bin/igvtools
$ podman run --it --rm --entrypoint /usr/local/bin/igvtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/igvtools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### varfilter.py

```bash
$ singularity exec <container> /usr/local/bin/varfilter.py
$ podman run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfilter.py   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### jaotc

```bash
$ singularity exec <container> /usr/local/bin/jaotc
$ podman run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jaotc   -v ${PWD} -w ${PWD} <container> -c " $@"
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