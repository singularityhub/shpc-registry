---
layout: container
name:  "quay.io/biocontainers/bioconductor-mofadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mofadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mofadata/container.yaml"
updated_at: "2025-10-22 04:02:04.031854"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mofadata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.13.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.1--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mofadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mofadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mofadata", "latest": {"1.22.0--r44hdfd78af_0": "sha256:3731742cf245eeea3a1f905303920150a0fae52a85f22ee2bb41cacfb6634ae3"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:ee0fde6cb04c21abe8b7527b6e758ee7e9b3dfc281c1ee9b44a3db568fe840cb", "1.13.0--r42hdfd78af_0": "sha256:879db8ee81a54e2035f0f367ec2e777c9724793c5c7e96e8030980987c77045a", "1.10.0--r41hdfd78af_1": "sha256:95f409dafa3ab7c8d08f2e21b2b2785c0e361446f130cdc142b91006d430b627", "1.16.1--r43hdfd78af_0": "sha256:561ddc545ff4c3f2bfccccbda0ab8eca7318268ad660fbac1993b30401e28720", "1.18.0--r43hdfd78af_0": "sha256:b3f87dc0f94e99577041568a75066ee41a2e3e8bdcb845c117d47bbc19224c01", "1.22.0--r44hdfd78af_0": "sha256:3731742cf245eeea3a1f905303920150a0fae52a85f22ee2bb41cacfb6634ae3"}, "docker": "quay.io/biocontainers/bioconductor-mofadata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mofadata.
shpc-registry automated BioContainers addition for bioconductor-mofadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mofadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mofadata:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mofadata/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mofadata/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mofadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mofadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mofadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mofadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mofadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mofadata-inspect-deffile:

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