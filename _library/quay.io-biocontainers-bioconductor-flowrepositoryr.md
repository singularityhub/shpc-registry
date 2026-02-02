---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowrepositoryr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowrepositoryr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowrepositoryr/container.yaml"
updated_at: "2026-02-02 05:19:35.811451"
latest: "1.23.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowrepositoryr"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.23.0--r41hdfd78af_0"
 - "1.22.0--r40hdfd78af_1"
 - "1.20.0--r40_0"
 - "1.18.0--r36_0"
 - "1.16.0--r361_1"
description: "shpc-registry automated BioContainers addition for bioconductor-flowrepositoryr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowrepositoryr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowrepositoryr", "latest": {"1.23.0--r41hdfd78af_0": "sha256:f974857442edb9b4110d9e0499ccbf381dc9cdf65abc6e05c99a5d27be923c23"}, "tags": {"1.8.0--r3.4.1_0": "sha256:e65fc9b4084b8a61ac3625f66d46b47fe1a3bb2acd0b5b7e76313f3996d10b08", "1.23.0--r41hdfd78af_0": "sha256:f974857442edb9b4110d9e0499ccbf381dc9cdf65abc6e05c99a5d27be923c23", "1.22.0--r40hdfd78af_1": "sha256:e4b306cbc0fb8230ddd1b41ada3af2dca9e84b356a632c2276f770f95270018b", "1.20.0--r40_0": "sha256:56c44c0fb3a057c3c722e26285f8e3fc1c347f51892d7d1802b6ac5b5b41cfd7", "1.18.0--r36_0": "sha256:c2b194c53118899cb5aac794bd959eb5052ddf4b0caa8919cce1f6b0b6bd5a1f", "1.16.0--r361_1": "sha256:8df1d01389996a8bcac0963993ca2eb57586af94df4e929de8145c8c5b41cba1"}, "docker": "quay.io/biocontainers/bioconductor-flowrepositoryr", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowrepositoryr.
shpc-registry automated BioContainers addition for bioconductor-flowrepositoryr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowrepositoryr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowrepositoryr:1.23.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowrepositoryr/1.23.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowrepositoryr/1.23.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowrepositoryr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowrepositoryr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowrepositoryr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowrepositoryr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowrepositoryr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowrepositoryr-inspect-deffile:

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