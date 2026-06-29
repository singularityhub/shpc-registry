---
layout: container
name:  "quay.io/biocontainers/ciri-as"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ciri-as/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ciri-as/container.yaml"
updated_at: "2026-06-29 07:09:15.040052"
latest: "1.2--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/ciri-as"
aliases:
 - "CIRI_AS.pl"
 - "qualfa2fq.pl"
 - "xa2multi.pl"
 - "bwa"
versions:
 - "1.2--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for ciri-as"
config: {"url": "https://biocontainers.pro/tools/ciri-as", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ciri-as", "latest": {"1.2--pl5321hdfd78af_0": "sha256:9ff725ff8fe043fa51808ad5ae5d578895222a7275d5611586c7f63b7bcc1d76"}, "tags": {"1.2--pl5321hdfd78af_0": "sha256:9ff725ff8fe043fa51808ad5ae5d578895222a7275d5611586c7f63b7bcc1d76"}, "docker": "quay.io/biocontainers/ciri-as", "aliases": {"CIRI_AS.pl": "/usr/local/bin/CIRI_AS.pl", "qualfa2fq.pl": "/usr/local/bin/qualfa2fq.pl", "xa2multi.pl": "/usr/local/bin/xa2multi.pl", "bwa": "/usr/local/bin/bwa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ciri-as.
singularity registry hpc automated addition for ciri-as
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ciri-as
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ciri-as:1.2--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ciri-as/1.2--pl5321hdfd78af_0
$ module help quay.io/biocontainers/ciri-as/1.2--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ciri-as-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ciri-as-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ciri-as-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ciri-as-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ciri-as-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ciri-as-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### CIRI_AS.pl

```bash
$ singularity exec <container> /usr/local/bin/CIRI_AS.pl
$ podman run --it --rm --entrypoint /usr/local/bin/CIRI_AS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/CIRI_AS.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### qualfa2fq.pl

```bash
$ singularity exec <container> /usr/local/bin/qualfa2fq.pl
$ podman run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/qualfa2fq.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xa2multi.pl

```bash
$ singularity exec <container> /usr/local/bin/xa2multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xa2multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bwa

```bash
$ singularity exec <container> /usr/local/bin/bwa
$ podman run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bwa   -v ${PWD} -w ${PWD} <container> -c " $@"
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