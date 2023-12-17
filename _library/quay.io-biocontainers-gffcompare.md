---
layout: container
name:  "quay.io/biocontainers/gffcompare"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gffcompare/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gffcompare/container.yaml"
updated_at: "2023-12-17 02:54:34.976550"
latest: "0.12.6--h4ac6f70_2"
container_url: "https://biocontainers.pro/tools/gffcompare"
aliases:
 - "gffcompare"
 - "gtest"
 - "threads"
versions:
 - "0.9.8--0"
 - "0.11.2--h9f5acd7_3"
 - "0.10.6--h2d50403_0"
 - "0.12.6--h9f5acd7_0"
 - "0.12.6--h4ac6f70_2"
description: "shpc-registry automated BioContainers addition for gffcompare"
config: {"url": "https://biocontainers.pro/tools/gffcompare", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gffcompare", "latest": {"0.12.6--h4ac6f70_2": "sha256:efa1f3228c6df51473f9d2b16289fc4acb8f4355e3de5530fd149165212b85b7"}, "tags": {"0.9.8--0": "sha256:52eaf3065657c4105197fb8b5e62fd4211ec160c1004f9619c3e0bb2feb87749", "0.11.2--h9f5acd7_3": "sha256:ca2d1a6c3f3aee5e98f8f768bccba01fc84d94f3880d361ca1420f3a1845929b", "0.10.6--h2d50403_0": "sha256:9e3a7a0f3bd2a928b28ae9fc31cc1da028908b567c178e8d5a3197df0d91a729", "0.12.6--h9f5acd7_0": "sha256:2bfdd5acf41876fd3d26809c5af7a5e4bd704699c92508409db821c7441475e0", "0.12.6--h4ac6f70_2": "sha256:efa1f3228c6df51473f9d2b16289fc4acb8f4355e3de5530fd149165212b85b7"}, "docker": "quay.io/biocontainers/gffcompare", "aliases": {"gffcompare": "/usr/local/bin/gffcompare", "gtest": "/usr/local/bin/gtest", "threads": "/usr/local/bin/threads"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gffcompare.
shpc-registry automated BioContainers addition for gffcompare
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gffcompare
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gffcompare:0.12.6--h4ac6f70_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gffcompare/0.12.6--h4ac6f70_2
$ module help quay.io/biocontainers/gffcompare/0.12.6--h4ac6f70_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gffcompare-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gffcompare-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gffcompare-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gffcompare-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gffcompare-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gffcompare-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gffcompare

```bash
$ singularity exec <container> /usr/local/bin/gffcompare
$ podman run --it --rm --entrypoint /usr/local/bin/gffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffcompare   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gtest

```bash
$ singularity exec <container> /usr/local/bin/gtest
$ podman run --it --rm --entrypoint /usr/local/bin/gtest   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gtest   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### threads

```bash
$ singularity exec <container> /usr/local/bin/threads
$ podman run --it --rm --entrypoint /usr/local/bin/threads   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/threads   -v ${PWD} -w ${PWD} <container> -c " $@"
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