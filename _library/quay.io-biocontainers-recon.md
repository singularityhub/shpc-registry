---
layout: container
name:  "quay.io/biocontainers/recon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/recon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/recon/container.yaml"
updated_at: "2023-08-14 02:22:41.127759"
latest: "1.08--h031d066_6"
container_url: "https://biocontainers.pro/tools/recon"
aliases:
 - "edgeredef"
 - "eledef"
 - "eleredef"
 - "famdef"
 - "imagespread"
versions:
 - "1.08--hec16e2b_4"
 - "1.08--h031d066_6"
description: "shpc-registry automated BioContainers addition for recon"
config: {"url": "https://biocontainers.pro/tools/recon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for recon", "latest": {"1.08--h031d066_6": "sha256:e1be8ca1d58394331349516ff8f7e1ccb3295e284666d946f53b7bdeb41335e2"}, "tags": {"1.08--hec16e2b_4": "sha256:574ca009a2637d0ca0b94c8d27b14ee43ad5fd8c3504e68d69b4e8cc0e21ddcb", "1.08--h031d066_6": "sha256:e1be8ca1d58394331349516ff8f7e1ccb3295e284666d946f53b7bdeb41335e2"}, "docker": "quay.io/biocontainers/recon", "aliases": {"edgeredef": "/usr/local/bin/edgeredef", "eledef": "/usr/local/bin/eledef", "eleredef": "/usr/local/bin/eleredef", "famdef": "/usr/local/bin/famdef", "imagespread": "/usr/local/bin/imagespread"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/recon.
shpc-registry automated BioContainers addition for recon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/recon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/recon:1.08--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/recon/1.08--h031d066_6
$ module help quay.io/biocontainers/recon/1.08--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### recon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### recon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### recon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### recon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### recon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### recon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### edgeredef

```bash
$ singularity exec <container> /usr/local/bin/edgeredef
$ podman run --it --rm --entrypoint /usr/local/bin/edgeredef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/edgeredef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eledef

```bash
$ singularity exec <container> /usr/local/bin/eledef
$ podman run --it --rm --entrypoint /usr/local/bin/eledef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eledef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eleredef

```bash
$ singularity exec <container> /usr/local/bin/eleredef
$ podman run --it --rm --entrypoint /usr/local/bin/eleredef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eleredef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### famdef

```bash
$ singularity exec <container> /usr/local/bin/famdef
$ podman run --it --rm --entrypoint /usr/local/bin/famdef   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/famdef   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### imagespread

```bash
$ singularity exec <container> /usr/local/bin/imagespread
$ podman run --it --rm --entrypoint /usr/local/bin/imagespread   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/imagespread   -v ${PWD} -w ${PWD} <container> -c " $@"
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