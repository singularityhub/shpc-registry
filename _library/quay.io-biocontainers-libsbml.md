---
layout: container
name:  "quay.io/biocontainers/libsbml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libsbml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libsbml/container.yaml"
updated_at: "2024-06-22 02:44:23.099581"
latest: "5.18.0--h5422e7e_10"
container_url: "https://biocontainers.pro/tools/libsbml"

versions:
 - "5.18.0--h3928612_7"
 - "5.18.0--h5422e7e_9"
 - "5.18.0--h5422e7e_10"
description: "shpc-registry automated BioContainers addition for libsbml"
config: {"url": "https://biocontainers.pro/tools/libsbml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libsbml", "latest": {"5.18.0--h5422e7e_10": "sha256:1f2dfd8aaffe6c2fb19146da60d2fac5dbf60e5f4c613f5f1191c0d9ed80ce54"}, "tags": {"5.18.0--h3928612_7": "sha256:139ac90b5392e887589cdf9c25bb7689bba06a86d2d230a4430d80e2f649d470", "5.18.0--h5422e7e_9": "sha256:cf6380c5ca5451ed7503b517ead60e2f7464d3c5a8b67fe8dd85b3729606a443", "5.18.0--h5422e7e_10": "sha256:1f2dfd8aaffe6c2fb19146da60d2fac5dbf60e5f4c613f5f1191c0d9ed80ce54"}, "docker": "quay.io/biocontainers/libsbml"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libsbml.
shpc-registry automated BioContainers addition for libsbml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libsbml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libsbml:5.18.0--h5422e7e_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libsbml/5.18.0--h5422e7e_10
$ module help quay.io/biocontainers/libsbml/5.18.0--h5422e7e_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libsbml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libsbml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libsbml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libsbml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libsbml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libsbml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libsbml

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