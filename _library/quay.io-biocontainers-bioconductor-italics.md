---
layout: container
name:  "quay.io/biocontainers/bioconductor-italics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-italics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-italics/container.yaml"
updated_at: "2024-03-21 04:01:19.327519"
latest: "2.62.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-italics"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.52.0--r41hdfd78af_0"
 - "2.58.0--r42hdfd78af_0"
 - "2.60.0--r43hdfd78af_0"
 - "2.62.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-italics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-italics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-italics", "latest": {"2.62.0--r43hdfd78af_0": "sha256:4a8815c690a2bd4d4cb8ed6354f93df5a4899390376e650df78edb6698fd903c"}, "tags": {"2.52.0--r41hdfd78af_0": "sha256:18f6b53ce57c110bbcb6c515ba5943f1326151d3548e180480f1f15f34628468", "2.58.0--r42hdfd78af_0": "sha256:be1bd356f67f7fd98764de0f14d62248b2380e3f2d2042841979362dfd8a6569", "2.60.0--r43hdfd78af_0": "sha256:afec962cf1345ec448d9fb9dcd1caf0c55e0f105acac792ee9c4f5b1ff5493e0", "2.62.0--r43hdfd78af_0": "sha256:4a8815c690a2bd4d4cb8ed6354f93df5a4899390376e650df78edb6698fd903c"}, "docker": "quay.io/biocontainers/bioconductor-italics", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-italics.
shpc-registry automated BioContainers addition for bioconductor-italics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-italics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-italics:2.62.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-italics/2.62.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-italics/2.62.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-italics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-italics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-italics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-italics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-italics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-italics-inspect-deffile:

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