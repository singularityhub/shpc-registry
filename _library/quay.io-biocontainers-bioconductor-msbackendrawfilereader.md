---
layout: container
name:  "quay.io/biocontainers/bioconductor-msbackendrawfilereader"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msbackendrawfilereader/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msbackendrawfilereader/container.yaml"
updated_at: "2022-10-27 00:51:25.922312"
latest: "1.0.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msbackendrawfilereader"
aliases:
 - "aprofutil"
 - "mono-hang-watchdog"
versions:
 - "1.0.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msbackendrawfilereader"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msbackendrawfilereader", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msbackendrawfilereader", "latest": {"1.0.0--r41hdfd78af_0": "sha256:d1bbbeb560b39ae1bd1e4b705db5cc7a7d0b960c9b961460eaf2525bd2599448"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:d1bbbeb560b39ae1bd1e4b705db5cc7a7d0b960c9b961460eaf2525bd2599448"}, "docker": "quay.io/biocontainers/bioconductor-msbackendrawfilereader", "aliases": {"aprofutil": "/usr/local/bin/aprofutil", "mono-hang-watchdog": "/usr/local/bin/mono-hang-watchdog"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msbackendrawfilereader.
shpc-registry automated BioContainers addition for bioconductor-msbackendrawfilereader
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendrawfilereader
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msbackendrawfilereader:1.0.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msbackendrawfilereader/1.0.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msbackendrawfilereader/1.0.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msbackendrawfilereader-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendrawfilereader-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msbackendrawfilereader-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msbackendrawfilereader-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msbackendrawfilereader-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msbackendrawfilereader-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aprofutil

```bash
$ singularity exec <container> /usr/local/bin/aprofutil
$ podman run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aprofutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mono-hang-watchdog

```bash
$ singularity exec <container> /usr/local/bin/mono-hang-watchdog
$ podman run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mono-hang-watchdog   -v ${PWD} -w ${PWD} <container> -c " $@"
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