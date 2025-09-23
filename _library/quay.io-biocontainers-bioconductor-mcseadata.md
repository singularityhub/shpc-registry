---
layout: container
name:  "quay.io/biocontainers/bioconductor-mcseadata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mcseadata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mcseadata/container.yaml"
updated_at: "2025-09-23 04:43:27.634940"
latest: "1.26.1--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mcseadata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.18.0--r42hdfd78af_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.1--r40hdfd78af_1"
 - "1.20.1--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.26.1--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mcseadata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mcseadata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mcseadata", "latest": {"1.26.1--r44hdfd78af_0": "sha256:ee5fb4cb41c1cc990226c9e3c866f6616ac30f7152fd96a67dadcf234ffeb632"}, "tags": {"1.9.0--r40_0": "sha256:c5eb00801ebbea5228b9c018ae45d7b1caa621a433879b740340ff32b7138e99", "1.18.0--r42hdfd78af_0": "sha256:f38acfa00cd3bce4f9298f9d31baf5a601947a6ad64844f1d3ca878ba10cb648", "1.17.0--r42hdfd78af_0": "sha256:0f0828fa71c1653377c0479e5be0475f21f7de0e7fd2fbd79747c196352ddc13", "1.14.0--r41hdfd78af_1": "sha256:6f2e201c52c48eb011cd27330beee59fde3fcfeebffbf414513e9dd312ff4af4", "1.12.0--r41hdfd78af_0": "sha256:d2f933f972503ce41e98003ef25c47ee3852fe008c14f9f399cddcd0ef11edfc", "1.10.1--r40hdfd78af_1": "sha256:5eaba2e332cb80bfca52744b5841c4ac1422a8d4799ae923ed1b25d719b6b814", "1.20.1--r43hdfd78af_0": "sha256:24881ebb8515be2057ec2d35f6c6887fe2663821aaea430785c3952b44a31e38", "1.22.0--r43hdfd78af_0": "sha256:8bf73b1434d14bbb12dab67757395d22175af776fc654b0324213e4c32316036", "1.26.1--r44hdfd78af_0": "sha256:ee5fb4cb41c1cc990226c9e3c866f6616ac30f7152fd96a67dadcf234ffeb632"}, "docker": "quay.io/biocontainers/bioconductor-mcseadata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mcseadata.
shpc-registry automated BioContainers addition for bioconductor-mcseadata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mcseadata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mcseadata:1.26.1--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mcseadata/1.26.1--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mcseadata/1.26.1--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mcseadata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mcseadata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mcseadata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mcseadata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mcseadata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mcseadata-inspect-deffile:

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