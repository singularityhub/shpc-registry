---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedadipochip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedadipochip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedadipochip/container.yaml"
updated_at: "2025-10-14 03:26:39.210688"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedadipochip"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedadipochip"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedadipochip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedadipochip", "latest": {"1.22.0--r44hdfd78af_0": "sha256:be21146816c8e79e0a6749e5804c9c91717a15f1ed1722c8f909762b86951ba1"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:6b1ce9eccf017acdb6b74087bf6c9baf0af2c3572f8bbd8e88dd5689c7624747", "1.14.0--r42hdfd78af_0": "sha256:7e7bd3fbf9fe54e94462ecbf8430d515eda008eab835525cfc5b715bd51f9b93", "1.10.0--r41hdfd78af_1": "sha256:d7fb461fa92d48b3956fe0394552d9fa4dd216dda985616bacd2610eb4a651af", "1.16.0--r43hdfd78af_0": "sha256:2c0257414a38fcd61c8112f6bfda1e072e4259b61a20dd4ada4ce71e0f89dee4", "1.18.0--r43hdfd78af_0": "sha256:71bee759cf923e9607c68ec9fd4336dfadb1233d818257fbddc969c0a081de44", "1.22.0--r44hdfd78af_0": "sha256:be21146816c8e79e0a6749e5804c9c91717a15f1ed1722c8f909762b86951ba1"}, "docker": "quay.io/biocontainers/bioconductor-curatedadipochip", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedadipochip.
shpc-registry automated BioContainers addition for bioconductor-curatedadipochip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedadipochip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedadipochip:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedadipochip/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedadipochip/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedadipochip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedadipochip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedadipochip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedadipochip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedadipochip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedadipochip-inspect-deffile:

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