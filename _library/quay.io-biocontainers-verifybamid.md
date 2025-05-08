---
layout: container
name:  "quay.io/biocontainers/verifybamid"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/verifybamid/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/verifybamid/container.yaml"
updated_at: "2025-05-08 05:38:01.385456"
latest: "1.1.3--h5ca1c30_9"
container_url: "https://biocontainers.pro/tools/verifybamid"

versions:
 - "1.1.3--h5b5514e_6"
 - "1.1.3--h43eeafb_8"
 - "1.1.3--h5ca1c30_9"
description: "shpc-registry automated BioContainers addition for verifybamid"
config: {"url": "https://biocontainers.pro/tools/verifybamid", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for verifybamid", "latest": {"1.1.3--h5ca1c30_9": "sha256:0151f9141569af45e05e63819c24c4a506eb5da7f0f363ab5dc0f8ab7f30281c"}, "tags": {"1.1.3--h5b5514e_6": "sha256:8e721261d0eae5c7b6c24742dd9713cd2878351882c65f2b4903d4df456a6024", "1.1.3--h43eeafb_8": "sha256:301ab0f60bbf69f4be566fd5e29e429f80f01fafa588ec8d79cb8bb8cb21f692", "1.1.3--h5ca1c30_9": "sha256:0151f9141569af45e05e63819c24c4a506eb5da7f0f363ab5dc0f8ab7f30281c"}, "docker": "quay.io/biocontainers/verifybamid"}
---

This module is a singularity container wrapper for quay.io/biocontainers/verifybamid.
shpc-registry automated BioContainers addition for verifybamid
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/verifybamid
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/verifybamid:1.1.3--h5ca1c30_9
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/verifybamid/1.1.3--h5ca1c30_9
$ module help quay.io/biocontainers/verifybamid/1.1.3--h5ca1c30_9
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### verifybamid-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### verifybamid-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### verifybamid-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### verifybamid-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### verifybamid-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### verifybamid-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### verifybamid

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