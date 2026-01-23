---
layout: container
name:  "quay.io/biocontainers/ascat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ascat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ascat/container.yaml"
updated_at: "2026-01-23 04:08:18.126926"
latest: "3.2.0--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/ascat"

versions:
 - "3.0.0--r41hdfd78af_0"
 - "3.0.0--r42hdfd78af_1"
 - "3.1.1--r42hdfd78af_0"
 - "3.1.1--r43hdfd78af_1"
 - "3.2.0--r43hdfd78af_0"
 - "3.2.0--r44hdfd78af_1"
description: "shpc-registry automated BioContainers addition for ascat"
config: {"url": "https://biocontainers.pro/tools/ascat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ascat", "latest": {"3.2.0--r44hdfd78af_1": "sha256:18b9f99529bfd133658a02e70170746239ed8c062327d6820f47556f7ab78464"}, "tags": {"3.0.0--r41hdfd78af_0": "sha256:e2848d59330279ee11ca493300ec507dfeed5261cdb729d6719b857a0d855dd1", "3.0.0--r42hdfd78af_1": "sha256:f8c11375b1ac1b50d5b85196e35ff5af94ded8d45fd0a69a4657d02a21355e12", "3.1.1--r42hdfd78af_0": "sha256:d9fdf22f84f1af0c202a9d90336a7d49aea163d93b384455cd0f4662550bc9cf", "3.1.1--r43hdfd78af_1": "sha256:f831ea28459c358016eb38976b114c04274cc4a5d481d0b7418bbf00fa90a851", "3.2.0--r43hdfd78af_0": "sha256:e758fd7be9ce779b5e459a509d8ce919ca42742416ebef1ec16f15669195626c", "3.2.0--r44hdfd78af_1": "sha256:18b9f99529bfd133658a02e70170746239ed8c062327d6820f47556f7ab78464"}, "docker": "quay.io/biocontainers/ascat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/ascat.
shpc-registry automated BioContainers addition for ascat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ascat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ascat:3.2.0--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ascat/3.2.0--r44hdfd78af_1
$ module help quay.io/biocontainers/ascat/3.2.0--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ascat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ascat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ascat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ascat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ascat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ascat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### ascat

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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