---
layout: container
name:  "quay.io/biocontainers/bioconductor-ballgown"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ballgown/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ballgown/container.yaml"
updated_at: "2024-11-05 03:20:21.551832"
latest: "2.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-ballgown"
aliases:
 - "tclsh8.5"
 - "wish8.5"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "2.8.4--r3.4.1_0"
 - "2.26.0--r41hdfd78af_0"
 - "2.24.0--r41hdfd78af_0"
 - "2.22.0--r40hdfd78af_1"
 - "2.20.0--r40_0"
 - "2.18.0--r36_0"
 - "2.30.0--r42hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-ballgown"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ballgown", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ballgown", "latest": {"2.34.0--r43hdfd78af_0": "sha256:05bb9541e0a108795045a26754def602566681357961f66df0fa27541aabdf66"}, "tags": {"2.8.4--r3.4.1_0": "sha256:b3d3437aabc309ac730e820f527576a4edcdabc09d28367269e9cdea85a2bcc6", "2.26.0--r41hdfd78af_0": "sha256:df0843442cbc8fe0d54d3341ea22f21a69bdd0364abeb763b18e8ecb45736b26", "2.24.0--r41hdfd78af_0": "sha256:ef4ecc70d78f5b51e17156646aa37828ec04710d7cc9fb1d85d69b7aa379a6e8", "2.22.0--r40hdfd78af_1": "sha256:c1801ce273fe1229992ae0647abe6ab1959a26835e40bf602ece1626b3075f10", "2.20.0--r40_0": "sha256:cddae13de38f6e6c536b64fd467937362d639b02223f8b16e535dbbf926099dd", "2.18.0--r36_0": "sha256:cc84e8c751218fb976c2cfdea6f996267ef5f9aeb26e1fcf3b405e7f7f18bf96", "2.30.0--r42hdfd78af_0": "sha256:28290f311e348fda391a8d03c3d198a2936ab7d7c7ca54d7b7531996979e0b94", "2.32.0--r43hdfd78af_0": "sha256:468ff1604f13e1c660d822ad932bbecdf6306e424f5107ef660dab2281d3ea9d", "2.34.0--r43hdfd78af_0": "sha256:05bb9541e0a108795045a26754def602566681357961f66df0fa27541aabdf66"}, "docker": "quay.io/biocontainers/bioconductor-ballgown", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ballgown.
shpc-registry automated BioContainers addition for bioconductor-ballgown
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ballgown
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ballgown:2.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ballgown/2.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-ballgown/2.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ballgown-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ballgown-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ballgown-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ballgown-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ballgown-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ballgown-inspect-deffile:

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