---
layout: container
name:  "quay.io/biocontainers/bioconductor-xbseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-xbseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-xbseq/container.yaml"
updated_at: "2025-04-03 03:42:15.255381"
latest: "1.22.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-xbseq"
aliases:
 - "wget"
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.22.0--r40hdfd78af_1"
 - "1.20.0--r40_0"
 - "1.18.0--r36_0"
 - "1.16.0--r36_1"
 - "1.14.0--r351_0"
description: "shpc-registry automated BioContainers addition for bioconductor-xbseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-xbseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-xbseq", "latest": {"1.22.0--r40hdfd78af_1": "sha256:ef9cd4650c945966287fb14e2ea4f069b77181b587a962327122c9a57b5a4d3b"}, "tags": {"1.8.0--r3.4.1_0": "sha256:af1ecbc6202971d012f08b74d4a84cacff4a5c0abe55b799e44cd53071bddb77", "1.22.0--r40hdfd78af_1": "sha256:ef9cd4650c945966287fb14e2ea4f069b77181b587a962327122c9a57b5a4d3b", "1.20.0--r40_0": "sha256:64161f9e78cdde38d857c53948305c6f3014dd528477bfe5bd3dce573f6a427f", "1.18.0--r36_0": "sha256:e63cbd261a6bee76cb71ab7cb811ee5ac457222d8a0b4fbc82bb1836a4277080", "1.16.0--r36_1": "sha256:005afcb4f960da80c486323baaf94770bc874ee6ed22903c4df0bd42b1e9f5d3", "1.14.0--r351_0": "sha256:aa463182f0b85424ea77164ebe2dfae8f02c551c4a087461f7363e8ca4d3a6f3"}, "docker": "quay.io/biocontainers/bioconductor-xbseq", "aliases": {"wget": "/usr/local/bin/wget", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-xbseq.
shpc-registry automated BioContainers addition for bioconductor-xbseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-xbseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-xbseq:1.22.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-xbseq/1.22.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-xbseq/1.22.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-xbseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xbseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-xbseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-xbseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-xbseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-xbseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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