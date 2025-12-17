---
layout: container
name:  "quay.io/biocontainers/bioconductor-divergence"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-divergence/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-divergence/container.yaml"
updated_at: "2025-12-17 03:30:37.320655"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-divergence"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-divergence"
config: {"url": "https://biocontainers.pro/tools/bioconductor-divergence", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-divergence", "latest": {"1.22.0--r44hdfd78af_0": "sha256:73e655095178629effe6cc28f5bffdbcf0599f092d34cba357dd28a40171866b"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:b6eefa30bc8d3bfff867fc3f6da56af55c9d5f98fa5ddcdfd46f61f80be1a7e3", "1.14.0--r42hdfd78af_0": "sha256:2a3680641517a31d069d53debfdf20b66671747601ef9cb322f463f33d57550e", "1.10.0--r41hdfd78af_0": "sha256:c1c6660e2f8090c115a5b243bacff1bd3f74e4be543a541d0c73f7d8b8d810df", "1.16.0--r43hdfd78af_0": "sha256:ebc2fa451036057bf0f105652a390ab4ca58d12ba381baa488c0dfc791be3d88", "1.18.0--r43hdfd78af_0": "sha256:eced0ac31a1d3c18e68238eafed6007ecea56d2a93756fce0a95f3f00c1da167", "1.22.0--r44hdfd78af_0": "sha256:73e655095178629effe6cc28f5bffdbcf0599f092d34cba357dd28a40171866b"}, "docker": "quay.io/biocontainers/bioconductor-divergence", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-divergence.
shpc-registry automated BioContainers addition for bioconductor-divergence
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-divergence
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-divergence:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-divergence/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-divergence/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-divergence-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-divergence-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-divergence-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-divergence-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-divergence-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-divergence-inspect-deffile:

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