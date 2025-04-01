---
layout: container
name:  "quay.io/biocontainers/bioconductor-gigsea"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gigsea/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gigsea/container.yaml"
updated_at: "2025-04-01 03:34:31.373606"
latest: "1.24.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gigsea"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_1"
 - "1.24.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gigsea"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gigsea", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gigsea", "latest": {"1.24.0--r44hdfd78af_0": "sha256:5580d3a62c424e5501aa54291e3cbaf30606e1851ee0cb367f31994f64b7f7df"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:a0488f30cbb6b9b1eff220d1df52266f1634a15ec50c3ff047e5cc582dcdd53d", "1.16.0--r42hdfd78af_0": "sha256:78dfd271e7eac1ddd52b51c42f0926e25d302613c8818bcf092f9747d168cc26", "1.12.0--r41hdfd78af_0": "sha256:9e0e5e3e0b6af72ca1e22ff2b5d54d3d0256def16ad588daeb63709b9d95a770", "1.10.0--r41hdfd78af_0": "sha256:0456014688cd1e7253c18fbd5ec4124699edeac88d79635386b8b6ebc5934466", "1.18.0--r43hdfd78af_0": "sha256:61bc09ed1af0bb93f49803e2a0105568c7b6d0c5d1a3827a4ad243a7aae6872d", "1.20.0--r43hdfd78af_1": "sha256:fef975c6f7d5f2e2f2d35660ca9e0f3a968edae6f099a8a038c7a939dd38fe37", "1.24.0--r44hdfd78af_0": "sha256:5580d3a62c424e5501aa54291e3cbaf30606e1851ee0cb367f31994f64b7f7df"}, "docker": "quay.io/biocontainers/bioconductor-gigsea", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gigsea.
shpc-registry automated BioContainers addition for bioconductor-gigsea
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gigsea
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gigsea:1.24.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gigsea/1.24.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gigsea/1.24.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gigsea-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gigsea-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gigsea-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gigsea-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gigsea-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gigsea-inspect-deffile:

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