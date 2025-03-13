---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnaseqcomp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnaseqcomp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnaseqcomp/container.yaml"
updated_at: "2025-03-13 03:15:30.004408"
latest: "1.36.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnaseqcomp"
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
 - "1.32.0--r43hdfd78af_1"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnaseqcomp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnaseqcomp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnaseqcomp", "latest": {"1.36.0--r44hdfd78af_0": "sha256:c9bbc9cd1e3fd80b3f24ce694712616ed7b0cf8cfd73524b618d2f6841c6cab3"}, "tags": {"1.8.0--r3.4.1_0": "sha256:16404b2183ebc9bd8edecea6dbe81b9d6863f0912302d691a8c052a4a2bc4894", "1.28.0--r42hdfd78af_0": "sha256:de73ca508e5295ad7c0711e738967b64623792ab30a025b811371c43409cdbfe", "1.24.0--r41hdfd78af_0": "sha256:e68f4743581a1006004a5e9bf5778d5488a6118d0087a96aa3a1ad414745ac6d", "1.22.0--r41hdfd78af_0": "sha256:4a5a5a44752fa01205f4c4eec2447dfb6a741fd4ee84273135668ccb6b6644bd", "1.20.0--r40hdfd78af_1": "sha256:b48604a6c518923c430f460f68c012ae112313527728a99fc73c52b780da4e6f", "1.18.0--r40_0": "sha256:d9e2b8db2255ad6e678071065f46c5625b071c578e2dd223e5148935d98e8982", "1.30.0--r43hdfd78af_0": "sha256:26c18a523a6510e5d6f157eedb73856efe2ad24a7a3c4468434d7616c9d2d712", "1.32.0--r43hdfd78af_1": "sha256:06885cdddb258c6ad2b9ef86011fcf9d63963a74ef063d4af4f9f8acd6bf5d09", "1.36.0--r44hdfd78af_0": "sha256:c9bbc9cd1e3fd80b3f24ce694712616ed7b0cf8cfd73524b618d2f6841c6cab3"}, "docker": "quay.io/biocontainers/bioconductor-rnaseqcomp", "aliases": {"tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnaseqcomp.
shpc-registry automated BioContainers addition for bioconductor-rnaseqcomp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqcomp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnaseqcomp:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnaseqcomp/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnaseqcomp/1.36.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnaseqcomp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqcomp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnaseqcomp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnaseqcomp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnaseqcomp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnaseqcomp-inspect-deffile:

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