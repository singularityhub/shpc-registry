---
layout: container
name:  "quay.io/biocontainers/bioconductor-svanumt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-svanumt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-svanumt/container.yaml"
updated_at: "2024-06-22 03:12:06.921398"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-svanumt"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-svanumt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-svanumt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-svanumt", "latest": {"1.6.0--r43hdfd78af_0": "sha256:9b2b8518f338aa1e4be65fc694161f62bd0b7ea8de8a2d9192a23d0eaa210418"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:dd46f36b04fbe6e615c087078bc7fa428703e6dabc6eb6a554c00ad3499689d8", "1.4.0--r42hdfd78af_0": "sha256:349d7f04c7833c7bb99acaba229b5f846cfc5be83bbfb711775ff2237591b4cf", "1.6.0--r43hdfd78af_0": "sha256:9b2b8518f338aa1e4be65fc694161f62bd0b7ea8de8a2d9192a23d0eaa210418"}, "docker": "quay.io/biocontainers/bioconductor-svanumt"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-svanumt.
shpc-registry automated BioContainers addition for bioconductor-svanumt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-svanumt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-svanumt:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-svanumt/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-svanumt/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-svanumt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svanumt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-svanumt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-svanumt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-svanumt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-svanumt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-svanumt

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