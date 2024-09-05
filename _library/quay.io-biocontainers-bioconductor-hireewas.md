---
layout: container
name:  "quay.io/biocontainers/bioconductor-hireewas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hireewas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hireewas/container.yaml"
updated_at: "2024-09-05 03:10:53.527817"
latest: "1.20.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hireewas"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hd029910_1"
 - "1.16.0--r42hc0cfd56_0"
 - "1.12.0--r41hc0cfd56_2"
 - "1.10.0--r41hd029910_0"
 - "1.16.0--r42ha9d7317_2"
 - "1.18.0--r43ha9d7317_0"
 - "1.20.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hireewas"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hireewas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hireewas", "latest": {"1.20.0--r43ha9d7317_0": "sha256:00f04431491a3bdeb9b7e3fcf643408207051b485ddb0fd24b121215123cb5c5"}, "tags": {"1.8.0--r40hd029910_1": "sha256:829d658685d172fe57d70ca2eac430c1553e0b3cb6f57f75dc16cc0aaff9b017", "1.16.0--r42hc0cfd56_0": "sha256:424b926cf66a6f4fd6982fc00dc27bc03910d99162dda9e3c1d96a386e4439b2", "1.12.0--r41hc0cfd56_2": "sha256:136602e13761162e39ba060f0e7bf31569658752fe5b57b27f59115ce55710ce", "1.10.0--r41hd029910_0": "sha256:6736da342d7131f12cf1feb6af75efe127f68470527dba84d1a9dec6cebd0c07", "1.16.0--r42ha9d7317_2": "sha256:53c831cab02043ca68aabd342a28fb65bc4e65023f932d5019f47693e9ec334b", "1.18.0--r43ha9d7317_0": "sha256:5445d56fcb2a6e0dff0de68571d59c0c813c6810bc522d00d515d4c57cf122b8", "1.20.0--r43ha9d7317_0": "sha256:00f04431491a3bdeb9b7e3fcf643408207051b485ddb0fd24b121215123cb5c5"}, "docker": "quay.io/biocontainers/bioconductor-hireewas", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hireewas.
shpc-registry automated BioContainers addition for bioconductor-hireewas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hireewas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hireewas:1.20.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hireewas/1.20.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-hireewas/1.20.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hireewas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hireewas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hireewas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hireewas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hireewas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hireewas-inspect-deffile:

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