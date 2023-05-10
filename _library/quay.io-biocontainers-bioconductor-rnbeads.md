---
layout: container
name:  "quay.io/biocontainers/bioconductor-rnbeads"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rnbeads/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rnbeads/container.yaml"
updated_at: "2023-05-10 02:53:57.871236"
latest: "2.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rnbeads"

versions:
 - "2.8.1--r40hdfd78af_0"
 - "2.12.2--r41hdfd78af_0"
 - "2.10.0--r41hdfd78af_0"
 - "2.16.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rnbeads"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rnbeads", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rnbeads", "latest": {"2.16.0--r42hdfd78af_0": "sha256:918c3cdb763553b2749dd6f613ec370a95abd37cf5a85d13288fd954d6a2ca7e"}, "tags": {"2.8.1--r40hdfd78af_0": "sha256:ec256dc79dc300bf9f23cefa536237aa71778b3c6f441a7f651bb470d8c3c90f", "2.12.2--r41hdfd78af_0": "sha256:f5022cc2dd1ba5d4a58c84b5f62b1d752731923b94f40789a13f2d15f63f8296", "2.10.0--r41hdfd78af_0": "sha256:99f1c597750c916a5881d86de62c3f8333b80dbe5ef241f8e8e35f1c3c40d0e1", "2.16.0--r42hdfd78af_0": "sha256:918c3cdb763553b2749dd6f613ec370a95abd37cf5a85d13288fd954d6a2ca7e"}, "docker": "quay.io/biocontainers/bioconductor-rnbeads"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rnbeads.
shpc-registry automated BioContainers addition for bioconductor-rnbeads
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rnbeads
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rnbeads:2.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rnbeads/2.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rnbeads/2.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rnbeads-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnbeads-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rnbeads-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rnbeads-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rnbeads-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rnbeads-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rnbeads

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