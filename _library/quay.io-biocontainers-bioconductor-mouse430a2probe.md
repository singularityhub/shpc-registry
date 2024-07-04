---
layout: container
name:  "quay.io/biocontainers/bioconductor-mouse430a2probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mouse430a2probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mouse430a2probe/container.yaml"
updated_at: "2024-07-04 02:43:38.007423"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mouse430a2probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mouse430a2probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mouse430a2probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mouse430a2probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:4bf42ca254b6509925bad0f098cb0258858760151cb63d6e8fda1873a6fcf4d8"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:9c6ba3ef77cea0fb99c2bd5355ba5b4a3aa4f71c9e97b43f55c0fc203074abb5", "2.18.0--r42hdfd78af_10": "sha256:ae09e97b602be8abde98af4c3830d19e16d9d99712b80aa2f9ba9009c6c05f21", "2.18.0--r43hdfd78af_11": "sha256:0803ee5e6ccd3831137f7b08d0c398fe03820c45f4d50bea51908a081ee14d19", "2.18.0--r43hdfd78af_12": "sha256:4bf42ca254b6509925bad0f098cb0258858760151cb63d6e8fda1873a6fcf4d8"}, "docker": "quay.io/biocontainers/bioconductor-mouse430a2probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mouse430a2probe.
shpc-registry automated BioContainers addition for bioconductor-mouse430a2probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse430a2probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mouse430a2probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mouse430a2probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mouse430a2probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mouse430a2probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse430a2probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mouse430a2probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mouse430a2probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mouse430a2probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mouse430a2probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mouse430a2probe

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