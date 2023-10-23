---
layout: container
name:  "quay.io/biocontainers/bioconductor-lfa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lfa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lfa/container.yaml"
updated_at: "2023-10-23 02:42:10.548929"
latest: "2.0.11--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lfa"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.28.0--r42hc0cfd56_0"
 - "1.24.0--r41hc0cfd56_2"
 - "1.22.0--r41hd029910_0"
 - "1.20.0--r40hd029910_1"
 - "1.18.0--r40h037d062_0"
 - "1.28.0--r42ha9d7317_1"
 - "2.0.11--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lfa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lfa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lfa", "latest": {"2.0.11--r43ha9d7317_0": "sha256:f5abcaaccccc8292fb54da54d6e1dcc89d118636e24b663c6eaed73560901745"}, "tags": {"1.8.0--r3.4.1_0": "sha256:cc3f599fcb740bdcac72567ade8fda293fffead73a4b81bcfcd8a4e6ff520223", "1.28.0--r42hc0cfd56_0": "sha256:f2bf92d7cb373346915ee0619043cf20e87518a07f133be7df1d8840a366fa8b", "1.24.0--r41hc0cfd56_2": "sha256:73bda9765cacf157fbc59bb91aa5964747144cfb5f1fc7e6de152860ea64d006", "1.22.0--r41hd029910_0": "sha256:041ccad90c4cc283580b7c690b5a9964ccf8288ecc25f3c1dabf3b0a87240427", "1.20.0--r40hd029910_1": "sha256:f0e970283ec4ee1eee329d309be8a312ae8017fb1ba593f3635b1614b6b77acf", "1.18.0--r40h037d062_0": "sha256:76e4eeea8f2c5b93da5c83bdf406e454659e7eba84c3ccc87c2ab33b443513a8", "1.28.0--r42ha9d7317_1": "sha256:3ac878dcc56e1cf96a52910158267da39a4b005e7f744188d92e081beb622125", "2.0.11--r43ha9d7317_0": "sha256:f5abcaaccccc8292fb54da54d6e1dcc89d118636e24b663c6eaed73560901745"}, "docker": "quay.io/biocontainers/bioconductor-lfa", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lfa.
shpc-registry automated BioContainers addition for bioconductor-lfa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lfa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lfa:2.0.11--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lfa/2.0.11--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-lfa/2.0.11--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lfa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lfa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lfa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lfa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lfa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lfa-inspect-deffile:

```bash
$ singularity inspect -d <container>
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