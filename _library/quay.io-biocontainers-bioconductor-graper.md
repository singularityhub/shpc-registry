---
layout: container
name:  "quay.io/biocontainers/bioconductor-graper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-graper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-graper/container.yaml"
updated_at: "2024-08-19 03:45:12.085972"
latest: "1.18.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-graper"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41h399db7b_0"
 - "1.10.0--r41hc247a5b_2"
 - "1.14.0--r42hc247a5b_0"
 - "1.14.0--r42hf17093f_1"
 - "1.16.1--r43hf17093f_0"
 - "1.18.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-graper"
config: {"url": "https://biocontainers.pro/tools/bioconductor-graper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-graper", "latest": {"1.18.0--r43hf17093f_0": "sha256:0010f1429550ab2fb448959b28eae8f48d08919f69bc421b43392bca1fb60967"}, "tags": {"1.8.0--r41h399db7b_0": "sha256:9129dad9604cb638c68329dd5e1b938970375678548910a62e2e42006d5f2823", "1.10.0--r41hc247a5b_2": "sha256:252e9059b19175b8ca5971766cd0396f2ffb6c1337310a840ad1d9297a769167", "1.14.0--r42hc247a5b_0": "sha256:f2669970d62caf530bc2542e963cd6d0bbfd02d383cec95bcf7dbe014a3f79e7", "1.14.0--r42hf17093f_1": "sha256:00bb57c437f0f8c079f0817ac4daab16956307069fb3b11053c0e8371056f333", "1.16.1--r43hf17093f_0": "sha256:08569e50567e1d7735da6009b9224b2fe3ffda3e6b3c6a6455a20ae4facf901b", "1.18.0--r43hf17093f_0": "sha256:0010f1429550ab2fb448959b28eae8f48d08919f69bc421b43392bca1fb60967"}, "docker": "quay.io/biocontainers/bioconductor-graper", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-graper.
shpc-registry automated BioContainers addition for bioconductor-graper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-graper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-graper:1.18.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-graper/1.18.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-graper/1.18.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-graper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-graper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-graper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-graper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-graper-inspect-deffile:

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