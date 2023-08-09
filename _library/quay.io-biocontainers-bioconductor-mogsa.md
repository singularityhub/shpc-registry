---
layout: container
name:  "quay.io/biocontainers/bioconductor-mogsa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mogsa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mogsa/container.yaml"
updated_at: "2023-08-09 03:26:30.806399"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mogsa"

versions:
 - "1.28.0--r41hdfd78af_0"
 - "1.32.0--r42hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mogsa"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mogsa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mogsa", "latest": {"1.34.0--r43hdfd78af_0": "sha256:f46b1c25a8d47fd492bbd477a52e14c1c6bec405097ca3613c75eb0e0fbe6f22"}, "tags": {"1.28.0--r41hdfd78af_0": "sha256:7d4bd9516635f72fc65db0b05d5a5bf2245e5cfc9095f4a828608f18ea8da80c", "1.32.0--r42hdfd78af_0": "sha256:e9aae9ad6712b3f8b09c1516b5c1d32a4900acc6f58240867508f5f7606d307c", "1.34.0--r43hdfd78af_0": "sha256:f46b1c25a8d47fd492bbd477a52e14c1c6bec405097ca3613c75eb0e0fbe6f22"}, "docker": "quay.io/biocontainers/bioconductor-mogsa"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mogsa.
shpc-registry automated BioContainers addition for bioconductor-mogsa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mogsa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mogsa:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mogsa/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mogsa/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mogsa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogsa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogsa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mogsa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mogsa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mogsa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mogsa

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