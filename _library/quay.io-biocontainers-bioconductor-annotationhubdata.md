---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotationhubdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotationhubdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotationhubdata/container.yaml"
updated_at: "2023-07-10 03:50:33.976327"
latest: "1.28.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotationhubdata"
aliases:
 - "wget"
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r3.4.1_0"
 - "1.24.0--r41hdfd78af_0"
 - "1.22.0--r41hdfd78af_0"
 - "1.20.1--r40hdfd78af_0"
 - "1.18.0--r40_0"
 - "1.16.0--r36_0"
 - "1.28.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotationhubdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotationhubdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotationhubdata", "latest": {"1.28.0--r42hdfd78af_0": "sha256:cbb4f0c55539c284e9c3487d4b5eac915efc2d03ca9b1b4d4bac7385a7df907c"}, "tags": {"1.8.0--r3.4.1_0": "sha256:d1d90553bc03e39751e4084529355c327a822318fc8aaf2eb4c184fcd622ff57", "1.24.0--r41hdfd78af_0": "sha256:e3da2de3f97b49104d9f837fbe41cb44add5c1e481f5fd1ad49a4058935b3119", "1.22.0--r41hdfd78af_0": "sha256:c5c7c844a1aed70050d7c2ff12e980034dddd8af242711fc4789afa442056e9c", "1.20.1--r40hdfd78af_0": "sha256:1c598fd87c4b75c335c3df1e7b2b5a2a9c3b64423f4c9a7c291eafe44c56459f", "1.18.0--r40_0": "sha256:7270d2b6cb994cabdba8d28a7bcbed62cfc4e933c131455375541cb80ce9c753", "1.16.0--r36_0": "sha256:0db8b3be8b8f0a5171374bb409645152e2466d5174aed4b9a17ae361cfe96511", "1.28.0--r42hdfd78af_0": "sha256:cbb4f0c55539c284e9c3487d4b5eac915efc2d03ca9b1b4d4bac7385a7df907c"}, "docker": "quay.io/biocontainers/bioconductor-annotationhubdata", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotationhubdata.
shpc-registry automated BioContainers addition for bioconductor-annotationhubdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationhubdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationhubdata:1.28.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotationhubdata/1.28.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotationhubdata/1.28.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotationhubdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationhubdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationhubdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotationhubdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotationhubdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotationhubdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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