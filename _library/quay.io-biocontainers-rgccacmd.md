---
layout: container
name:  "quay.io/biocontainers/rgccacmd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rgccacmd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rgccacmd/container.yaml"
updated_at: "2025-10-07 03:40:26.619366"
latest: "3.0.3--r44hdfd78af_2"
container_url: "https://biocontainers.pro/tools/rgccacmd"
aliases:
 - "idn2"
 - "wget"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "3.0.2--r41h9ee0642_0"
 - "3.0.3--r42hdfd78af_0"
 - "3.0.3--r44hdfd78af_2"
description: "shpc-registry automated BioContainers addition for rgccacmd"
config: {"url": "https://biocontainers.pro/tools/rgccacmd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rgccacmd", "latest": {"3.0.3--r44hdfd78af_2": "sha256:f56960a1d8eba1e46ee2eb7bb9bb56bf4de7b600fd7deaaea87b78f402578cba"}, "tags": {"3.0.2--r41h9ee0642_0": "sha256:6e0d898b03646248d98bb981a8af5ce9c95107e4985f494e722960bf1306fb38", "3.0.3--r42hdfd78af_0": "sha256:26dad6d52266edc3f6d7f3e5bcaaca4f3527588684e96a2e31573fd981e029d0", "3.0.3--r44hdfd78af_2": "sha256:f56960a1d8eba1e46ee2eb7bb9bb56bf4de7b600fd7deaaea87b78f402578cba"}, "docker": "quay.io/biocontainers/rgccacmd", "aliases": {"idn2": "/usr/local/bin/idn2", "wget": "/usr/local/bin/wget", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rgccacmd.
shpc-registry automated BioContainers addition for rgccacmd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rgccacmd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rgccacmd:3.0.3--r44hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rgccacmd/3.0.3--r44hdfd78af_2
$ module help quay.io/biocontainers/rgccacmd/3.0.3--r44hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rgccacmd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rgccacmd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rgccacmd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rgccacmd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rgccacmd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rgccacmd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### idn2

```bash
$ singularity exec <container> /usr/local/bin/idn2
$ podman run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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