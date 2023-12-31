---
layout: container
name:  "quay.io/biocontainers/bioconductor-basecallqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-basecallqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-basecallqc/container.yaml"
updated_at: "2023-12-31 02:52:02.752862"
latest: "1.24.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-basecallqc"
aliases:
 - "pandoc-citeproc"
 - "pandoc"
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36_1"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.0--r40_0"
 - "1.10.0--r36_0"
 - "1.24.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-basecallqc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-basecallqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-basecallqc", "latest": {"1.24.0--r43hdfd78af_0": "sha256:fa2597fb5ffb25544da4261e414cf9c3b9c9bfb66ddeed504ad623ed0a441ec6"}, "tags": {"1.8.0--r36_1": "sha256:465adc6c16c4917ce702916b9cd73b453bc81b5da9637e9c8ca4170d666c9a14", "1.18.0--r41hdfd78af_0": "sha256:5d342cebbc171bcee550e794907986d73e7f78672b0752b31a8069c852b43d14", "1.16.0--r41hdfd78af_0": "sha256:b5c18e6e068dac50b6ddfff27ef833afa28c19e3f0f3cc7be83e97381305a3ba", "1.14.0--r40hdfd78af_1": "sha256:d342dfa759022018986178b92505281a38254cb4b3c0eb518268a7da0256f2b2", "1.12.0--r40_0": "sha256:6d143de0293b63a9b7a9d8f2784a485ef2aa83c2cf6c9d10b5603839dfbb9180", "1.10.0--r36_0": "sha256:b73f0cf89544e1b8a9774ba2aaef9c80b85fd315262f23ac3497b3feeb983077", "1.24.0--r43hdfd78af_0": "sha256:fa2597fb5ffb25544da4261e414cf9c3b9c9bfb66ddeed504ad623ed0a441ec6"}, "docker": "quay.io/biocontainers/bioconductor-basecallqc", "aliases": {"pandoc-citeproc": "/usr/local/bin/pandoc-citeproc", "pandoc": "/usr/local/bin/pandoc", "gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-basecallqc.
shpc-registry automated BioContainers addition for bioconductor-basecallqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-basecallqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-basecallqc:1.24.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-basecallqc/1.24.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-basecallqc/1.24.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-basecallqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basecallqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basecallqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-basecallqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-basecallqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-basecallqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-citeproc

```bash
$ singularity exec <container> /usr/local/bin/pandoc-citeproc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-citeproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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