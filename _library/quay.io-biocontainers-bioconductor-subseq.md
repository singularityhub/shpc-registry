---
layout: container
name:  "quay.io/biocontainers/bioconductor-subseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-subseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-subseq/container.yaml"
updated_at: "2024-08-01 02:52:55.072947"
latest: "1.32.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-subseq"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hdfd78af_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.0--r40hdfd78af_1"
 - "1.18.0--r40_0"
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-subseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-subseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-subseq", "latest": {"1.32.0--r43hdfd78af_0": "sha256:91450c45904ab59bb40734721710949436559e6ea0e817615f3ec89a3b2480ef"}, "tags": {"1.8.0--r3.4.1_0": "sha256:2de11a06cef52b7ea2d7842fa2d38fb9af6aad0e154748099a2280f92f92b8d9", "1.28.0--r42hdfd78af_0": "sha256:ee380da417f154eafd3c273b1d5a081d74e53784986bd8985c899d83769fe290", "1.24.0--r41hdfd78af_0": "sha256:4b7dfb2c77ba627ddf2412ff44440714fe642176f147332f16d58df4503daa9e", "1.22.0--r41hdfd78af_0": "sha256:5a689104e89e582b9191c2163ffbc6ff0c1d5011520b73c39c0ecfd10e52ccbd", "1.20.0--r40hdfd78af_1": "sha256:10d1c72bc9b64bf15e2d36bfa35a11030df41693d233c75567b6c3f4787adc8a", "1.18.0--r40_0": "sha256:6f31a234b0d1357a13f79c0c5ff485cf39f80c1447b8b6556320af3b4905f5b1", "1.30.0--r43hdfd78af_0": "sha256:04abf1b1588778e22d15e6c6d8d8713f3532ef9e467aac9833115599ef8d5e55", "1.32.0--r43hdfd78af_0": "sha256:91450c45904ab59bb40734721710949436559e6ea0e817615f3ec89a3b2480ef"}, "docker": "quay.io/biocontainers/bioconductor-subseq", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-subseq.
shpc-registry automated BioContainers addition for bioconductor-subseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-subseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-subseq:1.32.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-subseq/1.32.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-subseq/1.32.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-subseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-subseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-subseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-subseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-subseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-subseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
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