---
layout: container
name:  "quay.io/biocontainers/r-mcpcounter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-mcpcounter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-mcpcounter/container.yaml"
updated_at: "2025-11-21 03:20:03.729810"
latest: "1.1.0--r44hdfd78af_6"
container_url: "https://biocontainers.pro/tools/r-mcpcounter"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.1.0--r41hdfd78af_3"
 - "1.1.0--r42hdfd78af_4"
 - "1.1.0--r43hdfd78af_5"
 - "1.1.0--r44hdfd78af_6"
description: "shpc-registry automated BioContainers addition for r-mcpcounter"
config: {"url": "https://biocontainers.pro/tools/r-mcpcounter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-mcpcounter", "latest": {"1.1.0--r44hdfd78af_6": "sha256:23582eea8e1d9f36fdbee345f6755c9ef09b95053fc1e324be01187731b4f2c3"}, "tags": {"1.1.0--r41hdfd78af_3": "sha256:01586ea9b6d00f221e375e06b7e69cee655abf11ba9e0b377894a46c4ac8d265", "1.1.0--r42hdfd78af_4": "sha256:a7ed18852a933657e539598980080894e3facd7428172c54871a9e78e4394a8d", "1.1.0--r43hdfd78af_5": "sha256:5775e91573c329dd982e41abeae0e2efa01d87a2e73a7aab6af2eb5d3e10ae1b", "1.1.0--r44hdfd78af_6": "sha256:23582eea8e1d9f36fdbee345f6755c9ef09b95053fc1e324be01187731b4f2c3"}, "docker": "quay.io/biocontainers/r-mcpcounter", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-mcpcounter.
shpc-registry automated BioContainers addition for r-mcpcounter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-mcpcounter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-mcpcounter:1.1.0--r44hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-mcpcounter/1.1.0--r44hdfd78af_6
$ module help quay.io/biocontainers/r-mcpcounter/1.1.0--r44hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-mcpcounter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-mcpcounter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-mcpcounter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-mcpcounter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-mcpcounter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-mcpcounter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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