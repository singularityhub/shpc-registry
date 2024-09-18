---
layout: container
name:  "quay.io/biocontainers/strainest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/strainest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/strainest/container.yaml"
updated_at: "2024-09-18 03:13:27.113820"
latest: "1.2.4--py36h6bb024c_3"
container_url: "https://biocontainers.pro/tools/strainest"

versions:
 - "1.2.4--py36h6bb024c_3"
 - "1.2.4--py27h6bb024c_3"
description: "shpc-registry automated BioContainers addition for strainest"
config: {"url": "https://biocontainers.pro/tools/strainest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for strainest", "latest": {"1.2.4--py36h6bb024c_3": "sha256:fecd370d6e02146ecda8c9ad0424b50448406a6f07de760e88b87e9298faf3ef"}, "tags": {"1.2.4--py36h6bb024c_3": "sha256:fecd370d6e02146ecda8c9ad0424b50448406a6f07de760e88b87e9298faf3ef", "1.2.4--py27h6bb024c_3": "sha256:907a25699a413512ea839a27f143b48dbeef40c71a293866d7e45628c24529fe"}, "docker": "quay.io/biocontainers/strainest"}
---

This module is a singularity container wrapper for quay.io/biocontainers/strainest.
shpc-registry automated BioContainers addition for strainest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/strainest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/strainest:1.2.4--py36h6bb024c_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/strainest/1.2.4--py36h6bb024c_3
$ module help quay.io/biocontainers/strainest/1.2.4--py36h6bb024c_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### strainest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### strainest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### strainest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### strainest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### strainest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### strainest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### strainest

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