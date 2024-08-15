---
layout: container
name:  "quay.io/biocontainers/bioconductor-csar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-csar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-csar/container.yaml"
updated_at: "2024-08-15 03:42:47.553748"
latest: "1.54.0--r43ha9d7317_1"
container_url: "https://biocontainers.pro/tools/bioconductor-csar"

versions:
 - "1.46.0--r41hc0cfd56_2"
 - "1.50.0--r42hc0cfd56_0"
 - "1.50.0--r42ha9d7317_1"
 - "1.52.0--r43ha9d7317_0"
 - "1.54.0--r43ha9d7317_0"
 - "1.54.0--r43ha9d7317_1"
description: "shpc-registry automated BioContainers addition for bioconductor-csar"
config: {"url": "https://biocontainers.pro/tools/bioconductor-csar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-csar", "latest": {"1.54.0--r43ha9d7317_1": "sha256:7e9efeb94ab9e10032e8b96fff3480437dd50bad7e363000aca2b147805f66f6"}, "tags": {"1.46.0--r41hc0cfd56_2": "sha256:48f7b04399c514fab7bb35ddd62affcefb8ed49b4c2194854eb0b5eb89bda879", "1.50.0--r42hc0cfd56_0": "sha256:852fa603953a9fa0552274f1b231a6d7d169449b6d95ced4614fdf67b83124db", "1.50.0--r42ha9d7317_1": "sha256:2bd2fe27e3db9e4776e6bbb13f4bf13285529f6642852c2b154b2cff195c071b", "1.52.0--r43ha9d7317_0": "sha256:5fbe295a8c85583c962a0a07168c24452f16daba19199d31e9c43b3a6af9068f", "1.54.0--r43ha9d7317_0": "sha256:4f6c5f65d7612e2f1c925aa145ec235475cabb48bd26d9734033e1323b6a9d9a", "1.54.0--r43ha9d7317_1": "sha256:7e9efeb94ab9e10032e8b96fff3480437dd50bad7e363000aca2b147805f66f6"}, "docker": "quay.io/biocontainers/bioconductor-csar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-csar.
shpc-registry automated BioContainers addition for bioconductor-csar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-csar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-csar:1.54.0--r43ha9d7317_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-csar/1.54.0--r43ha9d7317_1
$ module help quay.io/biocontainers/bioconductor-csar/1.54.0--r43ha9d7317_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-csar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-csar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-csar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-csar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-csar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-csar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-csar

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