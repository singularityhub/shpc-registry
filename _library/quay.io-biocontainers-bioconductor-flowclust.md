---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowclust/container.yaml"
updated_at: "2024-07-18 03:11:19.792190"
latest: "3.40.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-flowclust"

versions:
 - "3.32.0--r41hc0cfd56_2"
 - "3.36.0--r42hc0cfd56_0"
 - "3.36.0--r42ha9d7317_1"
 - "3.38.0--r43ha9d7317_0"
 - "3.40.0--r43ha9d7317_0"
 - "3.40.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-flowclust"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowclust", "latest": {"3.40.0--r43ha9d7317_1": "sha256:abdddd631049dcb9623fb5d937a4f946fb3bb91c6d864a942dc61b4227e23f36"}, "tags": {"3.32.0--r41hc0cfd56_2": "sha256:360521ee03ca333a691a0087ca848dd624828137fe9a6a1a8250f82fa3203ccc", "3.36.0--r42hc0cfd56_0": "sha256:c1156787a01866e761e10792de4cf598cc17776240946d438ad3ee6549f0be51", "3.36.0--r42ha9d7317_1": "sha256:8fe9eb03b79187a0088fc371b4c1ae0c8bcc21452f4d02fb6498bfb00c58d83c", "3.38.0--r43ha9d7317_0": "sha256:9b883a2d4e7cc46046884c0b2aaa00252999a54e67b5ffcc7344837d2095a160", "3.40.0--r43ha9d7317_0": "sha256:8c1f8fc80eebbae7dd9a7d440d4a3f577a75507ed431d76f797c3c275606cb26", "3.40.0--r43ha9d7317_1": "sha256:abdddd631049dcb9623fb5d937a4f946fb3bb91c6d864a942dc61b4227e23f36"}, "docker": "quay.io/biocontainers/bioconductor-flowclust"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowclust.
shpc-registry automated BioContainers addition for bioconductor-flowclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowclust:3.40.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowclust/3.40.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-flowclust/3.40.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowclust-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowclust

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