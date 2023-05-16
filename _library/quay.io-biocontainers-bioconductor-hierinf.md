---
layout: container
name:  "quay.io/biocontainers/bioconductor-hierinf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hierinf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hierinf/container.yaml"
updated_at: "2023-05-16 03:03:58.932325"
latest: "1.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hierinf"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hierinf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hierinf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hierinf", "latest": {"1.16.0--r42hdfd78af_0": "sha256:9d75169a4c212102ac062a0ae85919a31acf50aadc34a7ecea607339d60d2227"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:aaefe3a22e8ba7e1404990a69ab996d4543f0c6802cb40bf3686401574d00b27", "1.16.0--r42hdfd78af_0": "sha256:9d75169a4c212102ac062a0ae85919a31acf50aadc34a7ecea607339d60d2227", "1.12.0--r41hdfd78af_0": "sha256:117123f887a27efad217d1c8c9652bc9e9f0fdbc1ca1cf556451f3dd8d784b90", "1.10.0--r41hdfd78af_0": "sha256:344e3005b9faf263721de8faf4ad7ccc6869a01a8e3aac1e44a7b762daa7cc7e"}, "docker": "quay.io/biocontainers/bioconductor-hierinf", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hierinf.
shpc-registry automated BioContainers addition for bioconductor-hierinf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hierinf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hierinf:1.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hierinf/1.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hierinf/1.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hierinf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hierinf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hierinf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hierinf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hierinf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hierinf-inspect-deffile:

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