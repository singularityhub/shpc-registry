---
layout: container
name:  "quay.io/biocontainers/bioconductor-pepstat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pepstat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pepstat/container.yaml"
updated_at: "2025-02-03 03:45:41.388966"
latest: "1.40.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pepstat"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.40.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pepstat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pepstat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pepstat", "latest": {"1.40.0--r44hdfd78af_0": "sha256:0b292a6d3186949f63056c9c25f935679090df63d2a86d4be564befc398eb23c"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:a78c5111a2a6d01c557a86af2a17251c0afaca6e0cf1714e078981e75fb88ae1", "1.32.0--r42hdfd78af_0": "sha256:04c2afe31d342ba8dfec49b912c4ec0cb5ac78d9f595d35c09cb257d0730df7d", "1.34.0--r43hdfd78af_0": "sha256:27a5b22d8903cf5a99af985d070a6a13d11419c72a1636233bed739d6755ac8d", "1.36.0--r43hdfd78af_0": "sha256:97a91c55b99cf8fa2887a6a4f5093ae2c5d20acdd20289728ae8e69342734f1d", "1.40.0--r44hdfd78af_0": "sha256:0b292a6d3186949f63056c9c25f935679090df63d2a86d4be564befc398eb23c"}, "docker": "quay.io/biocontainers/bioconductor-pepstat"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pepstat.
shpc-registry automated BioContainers addition for bioconductor-pepstat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pepstat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pepstat:1.40.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pepstat/1.40.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pepstat/1.40.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pepstat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepstat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pepstat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pepstat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pepstat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pepstat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pepstat

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