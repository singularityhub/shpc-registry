---
layout: container
name:  "quay.io/biocontainers/bioconductor-adam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adam/container.yaml"
updated_at: "2025-04-06 03:35:31.583175"
latest: "1.22.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-adam"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.14.0--r42hc247a5b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hf17093f_1"
 - "1.16.0--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
 - "1.22.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-adam"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-adam", "latest": {"1.22.0--r44he5774e6_0": "sha256:2858d2167387a575be69973a72bd42d37605846d45b1b850c42af1f5526ca235"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:1e7125c4492d7327120b7195b6c99d99ff93d48733ede9f23d758ca745064a9b", "1.14.0--r42hc247a5b_0": "sha256:3777288f029b4e08eb45d9667f2a7dae818014e39e82e59236704b4e577f3ce7", "1.10.0--r41hc247a5b_2": "sha256:bf605d7e17c22c7d076a3bfb5d8c58a647f3893eeb8405e32ff200f4ab7502dd", "1.14.0--r42hf17093f_1": "sha256:39fc7dcc96e2c60d5089b01cd04da192661593f934178482e9385e4f3b8d1ccf", "1.16.0--r43hf17093f_0": "sha256:8a6c2ed35c2c52b71dcc7aa7efad13e091a1c04d4dacd49e33c92041afc0e13b", "1.18.0--r43hf17093f_0": "sha256:303df921fd4fe4c75a7cfb63f1427663f88bd79627346cd29adf24a9280ac654", "1.22.0--r44he5774e6_0": "sha256:2858d2167387a575be69973a72bd42d37605846d45b1b850c42af1f5526ca235"}, "docker": "quay.io/biocontainers/bioconductor-adam", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adam.
shpc-registry automated BioContainers addition for bioconductor-adam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adam:1.22.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adam/1.22.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-adam/1.22.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adam-inspect-deffile:

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