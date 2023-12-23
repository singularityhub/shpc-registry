---
layout: container
name:  "quay.io/biocontainers/bioconductor-synextend"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-synextend/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-synextend/container.yaml"
updated_at: "2023-12-23 03:01:54.652878"
latest: "1.14.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-synextend"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.2--r42hc0cfd56_0"
 - "1.10.2--r42ha9d7317_1"
 - "1.12.0--r43ha9d7317_0"
 - "1.14.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-synextend"
config: {"url": "https://biocontainers.pro/tools/bioconductor-synextend", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-synextend", "latest": {"1.14.0--r43ha9d7317_0": "sha256:b6431573b03fa602cd638b5c5a9a229ca0b03252a65a8bf739e921d9db446409"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:4cfe457a4cb59bede6d82f0f70b3f02a8778eb3d2ff66c49ff9762af4247f67b", "1.10.2--r42hc0cfd56_0": "sha256:68eecad67fc5884749147f3a015b3de4ce630fff2f4b6783b84a57c2eb2940cf", "1.10.2--r42ha9d7317_1": "sha256:8cdddb491f60c907498d29556dea9eb8e1bf25e01f818f9065a33bcc5444f60f", "1.12.0--r43ha9d7317_0": "sha256:034fa722d798891f7e2e7be2a270a08ec00afd3784711614790cff21ad0f56eb", "1.14.0--r43ha9d7317_0": "sha256:b6431573b03fa602cd638b5c5a9a229ca0b03252a65a8bf739e921d9db446409"}, "docker": "quay.io/biocontainers/bioconductor-synextend"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-synextend.
shpc-registry automated BioContainers addition for bioconductor-synextend
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-synextend
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-synextend:1.14.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-synextend/1.14.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-synextend/1.14.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-synextend-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synextend-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-synextend-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-synextend-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-synextend-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-synextend-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-synextend

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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