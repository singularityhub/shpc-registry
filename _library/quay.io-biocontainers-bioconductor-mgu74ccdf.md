---
layout: container
name:  "quay.io/biocontainers/bioconductor-mgu74ccdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mgu74ccdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mgu74ccdf/container.yaml"
updated_at: "2024-10-19 03:33:13.019850"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mgu74ccdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mgu74ccdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mgu74ccdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mgu74ccdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:3e834c3d4e496742ab9d55a2943961959a67d5c1d06c42bdf89707bd8fbbf29f"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:231ce10bdafa6da37e87596406e47b8cc988654f01d858eeb8267e98a22a82e9", "2.18.0--r42hdfd78af_10": "sha256:59720b37ac97ea84c23fa28089f7d2a55d198667078e539dbb4e3dea1824cc2b", "2.18.0--r43hdfd78af_11": "sha256:f290b261638dfc031aec97382c5531349de1f21faadba46c09285c26fc4dd527", "2.18.0--r43hdfd78af_12": "sha256:3e834c3d4e496742ab9d55a2943961959a67d5c1d06c42bdf89707bd8fbbf29f"}, "docker": "quay.io/biocontainers/bioconductor-mgu74ccdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mgu74ccdf.
shpc-registry automated BioContainers addition for bioconductor-mgu74ccdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74ccdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mgu74ccdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mgu74ccdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mgu74ccdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mgu74ccdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74ccdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mgu74ccdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mgu74ccdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mgu74ccdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mgu74ccdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mgu74ccdf

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