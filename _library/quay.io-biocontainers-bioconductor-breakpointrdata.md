---
layout: container
name:  "quay.io/biocontainers/bioconductor-breakpointrdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-breakpointrdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-breakpointrdata/container.yaml"
updated_at: "2024-08-08 02:41:45.957297"
latest: "1.20.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-breakpointrdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.16.0--r42hdfd78af_0"
 - "1.15.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-breakpointrdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-breakpointrdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-breakpointrdata", "latest": {"1.20.0--r43hdfd78af_0": "sha256:25edca183ae97094f1e238711ef5fe617542799e12f99b7ead4e59fd378bf1cd"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:4632309994266977023d5666ca081c1dc3d4565c447e7d03b824d22ffaa7beed", "1.16.0--r42hdfd78af_0": "sha256:fe9cca009c9fc03ec2ad16f5abdc207588fb57cc4b1ca9bf25218aeed690daf2", "1.15.0--r42hdfd78af_0": "sha256:533de351191b620e0b58ed436c352fa2cc3e36e7813a2fea63f9d448eab7ad4d", "1.12.0--r41hdfd78af_1": "sha256:12a73d45d83bd3d9b34c277fcff86cab1490b23b2d6b4472323e0c4777a5fc43", "1.10.0--r41hdfd78af_0": "sha256:79c311e8cbdfd4d48533f29bcb970a18b14dc386134ad9903514da63b1c8fef8", "1.18.0--r43hdfd78af_0": "sha256:17ee5e9fb767545947985749f532d2ad3a7a53b8ad4d8921a29adad024cffd16", "1.20.0--r43hdfd78af_0": "sha256:25edca183ae97094f1e238711ef5fe617542799e12f99b7ead4e59fd378bf1cd"}, "docker": "quay.io/biocontainers/bioconductor-breakpointrdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-breakpointrdata.
shpc-registry automated BioContainers addition for bioconductor-breakpointrdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-breakpointrdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-breakpointrdata:1.20.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-breakpointrdata/1.20.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-breakpointrdata/1.20.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-breakpointrdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breakpointrdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-breakpointrdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-breakpointrdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-breakpointrdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-breakpointrdata-inspect-deffile:

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