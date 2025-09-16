---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotationhubdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotationhubdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotationhubdata/container.yaml"
updated_at: "2025-09-16 04:26:52.805951"
latest: "1.36.0--r44hdfd78af_0"
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
 - "1.30.0--r43hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.36.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotationhubdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotationhubdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotationhubdata", "latest": {"1.36.0--r44hdfd78af_0": "sha256:bf5667ba709db2f008254e5267d15640df933eb4a8c0e1d85fafffefec93fa3f"}, "tags": {"1.8.0--r3.4.1_0": "sha256:4897aac2d49f1b3f5cb0536fe5c9553930be701240077a8fa593b3c7d1fa568f", "1.24.0--r41hdfd78af_0": "sha256:e3da2de3f97b49104d9f837fbe41cb44add5c1e481f5fd1ad49a4058935b3119", "1.22.0--r41hdfd78af_0": "sha256:c5c7c844a1aed70050d7c2ff12e980034dddd8af242711fc4789afa442056e9c", "1.20.1--r40hdfd78af_0": "sha256:1c598fd87c4b75c335c3df1e7b2b5a2a9c3b64423f4c9a7c291eafe44c56459f", "1.18.0--r40_0": "sha256:7270d2b6cb994cabdba8d28a7bcbed62cfc4e933c131455375541cb80ce9c753", "1.16.0--r36_0": "sha256:40ad40b7fa0930e6f7cce5ade37f224b303042dfc65e364dd338abe002d12664", "1.28.0--r42hdfd78af_0": "sha256:cbb4f0c55539c284e9c3487d4b5eac915efc2d03ca9b1b4d4bac7385a7df907c", "1.30.0--r43hdfd78af_0": "sha256:2de83c4a16333fff04f39dbec555899f99ca93a0d5055e1702a361d59a03e80e", "1.32.0--r43hdfd78af_0": "sha256:cafb3ee736385c6cfeb7bfac329cdca3424ab7ca55d529ac5c45af8026998f3d", "1.36.0--r44hdfd78af_0": "sha256:bf5667ba709db2f008254e5267d15640df933eb4a8c0e1d85fafffefec93fa3f"}, "docker": "quay.io/biocontainers/bioconductor-annotationhubdata", "aliases": {"wget": "/usr/local/bin/wget", "ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotationhubdata.
shpc-registry automated BioContainers addition for bioconductor-annotationhubdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationhubdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationhubdata:1.36.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotationhubdata/1.36.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotationhubdata/1.36.0--r44hdfd78af_0
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