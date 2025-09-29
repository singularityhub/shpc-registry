---
layout: container
name:  "quay.io/biocontainers/fastq-screen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fastq-screen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fastq-screen/container.yaml"
updated_at: "2025-09-29 03:32:58.874628"
latest: "0.16.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/fastq-screen"
aliases:
 - "bdf2gdfont.PLS"
 - "cvtbdf.pl"
 - "fastq_screen"
 - "bowtie-align-l"
 - "bowtie-align-s"
 - "bowtie-build-l"
 - "bowtie-build-s"
 - "bowtie-inspect-l"
 - "bowtie-inspect-s"
 - "bowtie"
 - "bowtie-build"
 - "bowtie-inspect"
 - "gdlib-config"
versions:
 - "0.5.2--1"
 - "0.15.2--pl5321hdfd78af_0"
 - "0.14.0--pl5321hdfd78af_2"
 - "0.13.0--pl526_1"
 - "0.11.3--pl526_1"
 - "0.15.3--pl5321hdfd78af_0"
 - "0.16.0--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for fastq-screen"
config: {"url": "https://biocontainers.pro/tools/fastq-screen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fastq-screen", "latest": {"0.16.0--pl5321hdfd78af_0": "sha256:e1a5ab44938cdc826de5ede890068ad486797948ce985375802b302971fa888d"}, "tags": {"0.5.2--1": "sha256:bcb19ad7f43add5a4692cb10488647c884b2ca1ef1a3dd8e090ffeb0a343e2fb", "0.15.2--pl5321hdfd78af_0": "sha256:fc249e00f46e3392826fad5260344158c972dc47e9c193cbb6a12adacf5bbfe7", "0.14.0--pl5321hdfd78af_2": "sha256:1d02412b07bc9291c0bcedd763474bfaade5439a64df439e3c8306631171f6ca", "0.13.0--pl526_1": "sha256:6b47425690a57c14f9258217e206933635eb0b16988cb09fca2c809d04584649", "0.11.3--pl526_1": "sha256:af07c97c4a9ec981db54d5f847b3585e578c4b21d41e591cc7345a7c54116b71", "0.15.3--pl5321hdfd78af_0": "sha256:b1c48bcdd2aa5ae15f8b9c5522c1118a5b2a20c32a7110683aa348b909480975", "0.16.0--pl5321hdfd78af_0": "sha256:e1a5ab44938cdc826de5ede890068ad486797948ce985375802b302971fa888d"}, "docker": "quay.io/biocontainers/fastq-screen", "aliases": {"bdf2gdfont.PLS": "/usr/local/bin/bdf2gdfont.PLS", "cvtbdf.pl": "/usr/local/bin/cvtbdf.pl", "fastq_screen": "/usr/local/bin/fastq_screen", "bowtie-align-l": "/usr/local/bin/bowtie-align-l", "bowtie-align-s": "/usr/local/bin/bowtie-align-s", "bowtie-build-l": "/usr/local/bin/bowtie-build-l", "bowtie-build-s": "/usr/local/bin/bowtie-build-s", "bowtie-inspect-l": "/usr/local/bin/bowtie-inspect-l", "bowtie-inspect-s": "/usr/local/bin/bowtie-inspect-s", "bowtie": "/usr/local/bin/bowtie", "bowtie-build": "/usr/local/bin/bowtie-build", "bowtie-inspect": "/usr/local/bin/bowtie-inspect", "gdlib-config": "/usr/local/bin/gdlib-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fastq-screen.
shpc-registry automated BioContainers addition for fastq-screen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fastq-screen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fastq-screen:0.16.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fastq-screen/0.16.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/fastq-screen/0.16.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fastq-screen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fastq-screen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fastq-screen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fastq-screen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fastq-screen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fastq-screen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bdf2gdfont.PLS

```bash
$ singularity exec <container> /usr/local/bin/bdf2gdfont.PLS
$ podman run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bdf2gdfont.PLS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cvtbdf.pl

```bash
$ singularity exec <container> /usr/local/bin/cvtbdf.pl
$ podman run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cvtbdf.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastq_screen

```bash
$ singularity exec <container> /usr/local/bin/fastq_screen
$ podman run --it --rm --entrypoint /usr/local/bin/fastq_screen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastq_screen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-align-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-align-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-align-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-l

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-l
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-l   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect-s

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect-s
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect-s   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie

```bash
$ singularity exec <container> /usr/local/bin/bowtie
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-build

```bash
$ singularity exec <container> /usr/local/bin/bowtie-build
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-build   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie-inspect

```bash
$ singularity exec <container> /usr/local/bin/bowtie-inspect
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie-inspect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdlib-config

```bash
$ singularity exec <container> /usr/local/bin/gdlib-config
$ podman run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdlib-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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