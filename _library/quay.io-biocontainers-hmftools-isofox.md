---
layout: container
name:  "quay.io/biocontainers/hmftools-isofox"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hmftools-isofox/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/hmftools-isofox/container.yaml"
updated_at: "2022-10-27 00:21:42.680376"
latest: "1.5--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hmftools-isofox"
aliases:
 - "isofox"
versions:
 - "1.5--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for hmftools-isofox"
config: {"url": "https://biocontainers.pro/tools/hmftools-isofox", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hmftools-isofox", "latest": {"1.5--hdfd78af_0": "sha256:5d334f293ec92ff5472ee183df50b5bea22289fe2867baad9785af9229ebb6bf"}, "tags": {"1.5--hdfd78af_0": "sha256:5d334f293ec92ff5472ee183df50b5bea22289fe2867baad9785af9229ebb6bf"}, "docker": "quay.io/biocontainers/hmftools-isofox", "aliases": {"isofox": "/usr/local/bin/isofox"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hmftools-isofox.
shpc-registry automated BioContainers addition for hmftools-isofox
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hmftools-isofox
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hmftools-isofox:1.5--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hmftools-isofox/1.5--hdfd78af_0
$ module help quay.io/biocontainers/hmftools-isofox/1.5--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hmftools-isofox-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-isofox-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hmftools-isofox-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hmftools-isofox-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hmftools-isofox-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hmftools-isofox-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### isofox

```bash
$ singularity exec <container> /usr/local/bin/isofox
$ podman run --it --rm --entrypoint /usr/local/bin/isofox   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/isofox   -v ${PWD} -w ${PWD} <container> -c " $@"
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