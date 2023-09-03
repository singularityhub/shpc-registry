---
layout: container
name:  "quay.io/biocontainers/bioconductor-msmb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-msmb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-msmb/container.yaml"
updated_at: "2023-09-03 02:33:17.381349"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-msmb"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_0"
 - "1.15.2--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-msmb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-msmb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-msmb", "latest": {"1.18.0--r43hdfd78af_0": "sha256:692099c2f5327d2c2a2a385e3f113b99c398cf187cd3e39423a88a059a583f77"}, "tags": {"1.8.0--r40hdfd78af_0": "sha256:7b6cd660c3e94c3024638632e3452bfe989e883e7f898819b4a4707dfeb65119", "1.15.2--r42hdfd78af_0": "sha256:9756cbbee0c4e8483ab42072a8170b32a2ab4383da9eab1ee8d86704103253ef", "1.12.0--r41hdfd78af_1": "sha256:2f9290c3360fbb51695cb0f753f61dd5f3fa5f462e1e01a0fd834560c61851ea", "1.10.0--r41hdfd78af_0": "sha256:004fe9e7bb8d4a38725621a9e2e86d0fc318a0845860bdf439dc7e1a9673a2e1", "1.18.0--r43hdfd78af_0": "sha256:692099c2f5327d2c2a2a385e3f113b99c398cf187cd3e39423a88a059a583f77"}, "docker": "quay.io/biocontainers/bioconductor-msmb", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-msmb.
shpc-registry automated BioContainers addition for bioconductor-msmb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-msmb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-msmb:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-msmb/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-msmb/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-msmb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msmb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-msmb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-msmb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-msmb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-msmb-inspect-deffile:

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