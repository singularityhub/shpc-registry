---
layout: container
name:  "quay.io/biocontainers/vqsr_cnn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vqsr_cnn/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/vqsr_cnn/container.yaml"
updated_at: "2022-10-29 05:44:48.703779"
latest: "0.0.194--py_0"
container_url: "https://biocontainers.pro/tools/vqsr_cnn"
aliases:
 - "2to3-3.6"
 - "ace2sam"
 - "assistant"
 - "bcftools"
 - "bgzip"
 - "blast2sam.pl"
 - "bowtie2sam.pl"
 - "color-chrs.pl"
 - "conv-template"
 - "dbus-cleanup-sockets"
versions:
 - "0.0.194--py_0"
description: "shpc-registry automated BioContainers addition for vqsr_cnn"
config: {"url": "https://biocontainers.pro/tools/vqsr_cnn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vqsr_cnn", "latest": {"0.0.194--py_0": "sha256:5bbec43d403410518acdf5cf831b39417f75c1f1daf332a078bbfc1fcea18cd5"}, "tags": {"0.0.194--py_0": "sha256:5bbec43d403410518acdf5cf831b39417f75c1f1daf332a078bbfc1fcea18cd5"}, "docker": "quay.io/biocontainers/vqsr_cnn", "aliases": {"2to3-3.6": "/usr/local/bin/2to3-3.6", "ace2sam": "/usr/local/bin/ace2sam", "assistant": "/usr/local/bin/assistant", "bcftools": "/usr/local/bin/bcftools", "bgzip": "/usr/local/bin/bgzip", "blast2sam.pl": "/usr/local/bin/blast2sam.pl", "bowtie2sam.pl": "/usr/local/bin/bowtie2sam.pl", "color-chrs.pl": "/usr/local/bin/color-chrs.pl", "conv-template": "/usr/local/bin/conv-template", "dbus-cleanup-sockets": "/usr/local/bin/dbus-cleanup-sockets"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vqsr_cnn.
shpc-registry automated BioContainers addition for vqsr_cnn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vqsr_cnn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vqsr_cnn:0.0.194--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vqsr_cnn/0.0.194--py_0
$ module help quay.io/biocontainers/vqsr_cnn/0.0.194--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vqsr_cnn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vqsr_cnn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vqsr_cnn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vqsr_cnn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vqsr_cnn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vqsr_cnn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ace2sam

```bash
$ singularity exec <container> /usr/local/bin/ace2sam
$ podman run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ace2sam   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### assistant

```bash
$ singularity exec <container> /usr/local/bin/assistant
$ podman run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/assistant   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bcftools

```bash
$ singularity exec <container> /usr/local/bin/bcftools
$ podman run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bcftools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### blast2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/blast2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/blast2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bowtie2sam.pl

```bash
$ singularity exec <container> /usr/local/bin/bowtie2sam.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bowtie2sam.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### color-chrs.pl

```bash
$ singularity exec <container> /usr/local/bin/color-chrs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/color-chrs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### conv-template

```bash
$ singularity exec <container> /usr/local/bin/conv-template
$ podman run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/conv-template   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbus-cleanup-sockets

```bash
$ singularity exec <container> /usr/local/bin/dbus-cleanup-sockets
$ podman run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbus-cleanup-sockets   -v ${PWD} -w ${PWD} <container> -c " $@"
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