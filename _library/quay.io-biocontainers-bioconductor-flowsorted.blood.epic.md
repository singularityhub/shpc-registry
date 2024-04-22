---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowsorted.blood.epic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowsorted.blood.epic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowsorted.blood.epic/container.yaml"
updated_at: "2024-04-22 02:49:48.181672"
latest: "2.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowsorted.blood.epic"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.12.1--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "2.2.0--r42hdfd78af_0"
 - "2.4.2--r43hdfd78af_0"
 - "2.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowsorted.blood.epic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowsorted.blood.epic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowsorted.blood.epic", "latest": {"2.6.0--r43hdfd78af_0": "sha256:79b5bc6362e5bcdf5c2a67ac17795bea5bd00043cef727477b5e77310b68ab7a"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:10ff49b495a6dff41cc2b44732e385dc978ef950c70b4483b23694cc54e6b51c", "1.12.1--r41hdfd78af_1": "sha256:8f6c12a38d9755b06989f09876bdad656853e4a140a71b4a611e49f35f238528", "1.10.0--r41hdfd78af_0": "sha256:c5e9303e93fd05d981c4c9bbb57d43571a7aa5a0d0dfd6d343eeeacffc4a4d0a", "2.2.0--r42hdfd78af_0": "sha256:44a59f3352bb4d30d0cff1093018f72e9523fd1deff750be1d70dca7b8aac375", "2.4.2--r43hdfd78af_0": "sha256:cc0749d008e4dcd46bbbe0ae650aad9a6a8a41a19c908facc6feba05bfff5598", "2.6.0--r43hdfd78af_0": "sha256:79b5bc6362e5bcdf5c2a67ac17795bea5bd00043cef727477b5e77310b68ab7a"}, "docker": "quay.io/biocontainers/bioconductor-flowsorted.blood.epic", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowsorted.blood.epic.
shpc-registry automated BioContainers addition for bioconductor-flowsorted.blood.epic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowsorted.blood.epic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowsorted.blood.epic:2.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowsorted.blood.epic/2.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowsorted.blood.epic/2.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowsorted.blood.epic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowsorted.blood.epic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowsorted.blood.epic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowsorted.blood.epic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowsorted.blood.epic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowsorted.blood.epic-inspect-deffile:

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