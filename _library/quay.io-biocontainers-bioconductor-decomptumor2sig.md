---
layout: container
name:  "quay.io/biocontainers/bioconductor-decomptumor2sig"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-decomptumor2sig/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-decomptumor2sig/container.yaml"
updated_at: "2024-02-07 02:39:46.866892"
latest: "2.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-decomptumor2sig"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.8.0--r41hdfd78af_0"
 - "2.14.0--r42hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.16.0--r43hdfd78af_0"
 - "2.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-decomptumor2sig"
config: {"url": "https://biocontainers.pro/tools/bioconductor-decomptumor2sig", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-decomptumor2sig", "latest": {"2.18.0--r43hdfd78af_0": "sha256:03effe2aa1c9e8f6f47e8550f8ad0d3678caa10e6a864da625699a0cc4ada7f2"}, "tags": {"2.8.0--r41hdfd78af_0": "sha256:1d1409f367d7a9f2679936552beab146144025d8ec4da6bcf40965a832c4e0f9", "2.14.0--r42hdfd78af_0": "sha256:24c14e5b537a900797d3c8bf99702e8dd0ef40d31f70231cf786d938f41b8d63", "2.10.0--r41hdfd78af_0": "sha256:83b7aafaaed346c4be37b968f2a4534937a024f1eb8342219eb8967d6f0df681", "2.16.0--r43hdfd78af_0": "sha256:3ae81b0339605ef98e4ed403c3250da73dc79534cb169fadc32e3e522bea2cf6", "2.18.0--r43hdfd78af_0": "sha256:03effe2aa1c9e8f6f47e8550f8ad0d3678caa10e6a864da625699a0cc4ada7f2"}, "docker": "quay.io/biocontainers/bioconductor-decomptumor2sig", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-decomptumor2sig.
shpc-registry automated BioContainers addition for bioconductor-decomptumor2sig
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-decomptumor2sig
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-decomptumor2sig:2.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-decomptumor2sig/2.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-decomptumor2sig/2.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-decomptumor2sig-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-decomptumor2sig-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-decomptumor2sig-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-decomptumor2sig-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-decomptumor2sig-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-decomptumor2sig-inspect-deffile:

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