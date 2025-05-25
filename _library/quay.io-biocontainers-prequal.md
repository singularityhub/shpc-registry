---
layout: container
name:  "quay.io/biocontainers/prequal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prequal/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prequal/container.yaml"
updated_at: "2025-05-25 04:12:01.728592"
latest: "1.02--h5ca1c30_7"
container_url: "https://biocontainers.pro/tools/prequal"
aliases:
 - "prequal"
versions:
 - "1.02--hb97b32f_3"
 - "1.02--h2202e69_5"
 - "1.02--h43eeafb_6"
 - "1.02--h5ca1c30_7"
description: "shpc-registry automated BioContainers addition for prequal"
config: {"url": "https://biocontainers.pro/tools/prequal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prequal", "latest": {"1.02--h5ca1c30_7": "sha256:4303b846b15f06c8c499c3d282cc4f063279bc973b63d5b2d77815dafd4c6dda"}, "tags": {"1.02--hb97b32f_3": "sha256:1f1a14effefc24a922d9946f8fba891c80a68be7286b6311f3f72eb2aa896bf5", "1.02--h2202e69_5": "sha256:7b38ed3ab0afe0a12becde211ae288c346c5066d525bed3b52791afb2f44b339", "1.02--h43eeafb_6": "sha256:6f9186106aa5234855c84661e1c1e95072148f328c623e7147fcc55a7ddfda18", "1.02--h5ca1c30_7": "sha256:4303b846b15f06c8c499c3d282cc4f063279bc973b63d5b2d77815dafd4c6dda"}, "docker": "quay.io/biocontainers/prequal", "aliases": {"prequal": "/usr/local/bin/prequal"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prequal.
shpc-registry automated BioContainers addition for prequal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prequal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prequal:1.02--h5ca1c30_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prequal/1.02--h5ca1c30_7
$ module help quay.io/biocontainers/prequal/1.02--h5ca1c30_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prequal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prequal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prequal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prequal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prequal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prequal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prequal

```bash
$ singularity exec <container> /usr/local/bin/prequal
$ podman run --it --rm --entrypoint /usr/local/bin/prequal   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prequal   -v ${PWD} -w ${PWD} <container> -c " $@"
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