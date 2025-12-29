---
layout: container
name:  "quay.io/biocontainers/fann"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fann/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fann/container.yaml"
updated_at: "2025-12-29 03:56:55.198102"
latest: "2.2.0--h503566f_7"
container_url: "https://biocontainers.pro/tools/fann"

versions:
 - "2.2.0--h87f3376_4"
 - "2.2.0--hdbdd923_6"
 - "2.2.0--h503566f_7"
description: "shpc-registry automated BioContainers addition for fann"
config: {"url": "https://biocontainers.pro/tools/fann", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fann", "latest": {"2.2.0--h503566f_7": "sha256:7a069d8f217f5c21204b8425e16c721ce7f0b41ee27f80eccc8b0beb4dce9afe"}, "tags": {"2.2.0--h87f3376_4": "sha256:e480b92b8d598028eade0cd49a8a530fd3a5cf200903b883b0b50eddf70b829f", "2.2.0--hdbdd923_6": "sha256:c0ab7030caf0f67442c68045a15c6ef38ade4210f3f693af9f302211947c6494", "2.2.0--h503566f_7": "sha256:7a069d8f217f5c21204b8425e16c721ce7f0b41ee27f80eccc8b0beb4dce9afe"}, "docker": "quay.io/biocontainers/fann"}
---

This module is a singularity container wrapper for quay.io/biocontainers/fann.
shpc-registry automated BioContainers addition for fann
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fann
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fann:2.2.0--h503566f_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fann/2.2.0--h503566f_7
$ module help quay.io/biocontainers/fann/2.2.0--h503566f_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fann-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fann-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fann-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fann-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fann-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fann-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### fann

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