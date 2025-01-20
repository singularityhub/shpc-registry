---
layout: container
name:  "quay.io/biocontainers/andi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/andi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/andi/container.yaml"
updated_at: "2025-01-20 03:27:12.822460"
latest: "0.14--hfc2f157_2"
container_url: "https://biocontainers.pro/tools/andi"
aliases:
 - "andi"
 - "gsl-randist"
versions:
 - "0.13--hcde4609_3"
 - "0.13--h082502c_4"
 - "0.14--h082502c_0"
 - "0.14--h47df53c_1"
 - "0.14--hfc2f157_2"
description: "shpc-registry automated BioContainers addition for andi"
config: {"url": "https://biocontainers.pro/tools/andi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for andi", "latest": {"0.14--hfc2f157_2": "sha256:9770a8ea2ab0fb587345d161ea34f5c7ff99367f576d33c0db7e2ef7488b2f22"}, "tags": {"0.13--hcde4609_3": "sha256:281f7f10cd6af2eaa5055d61e95597085273a8c8952b94fc04e2d59c9d26d428", "0.13--h082502c_4": "sha256:a1e26a176a651eebc2ba2267e759a1cba2f5b22d34f9a7a2f28dd344bb1942a0", "0.14--h082502c_0": "sha256:789fce03d991fcd93122fc820eab76f2b674620a29a66b579fb1c5e3fc4cdfac", "0.14--h47df53c_1": "sha256:b726cc7b9f9fa82aa1639f2fb7ac9eabda328a64966e7589ad6111546077fba2", "0.14--hfc2f157_2": "sha256:9770a8ea2ab0fb587345d161ea34f5c7ff99367f576d33c0db7e2ef7488b2f22"}, "docker": "quay.io/biocontainers/andi", "aliases": {"andi": "/usr/local/bin/andi", "gsl-randist": "/usr/local/bin/gsl-randist"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/andi.
shpc-registry automated BioContainers addition for andi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/andi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/andi:0.14--hfc2f157_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/andi/0.14--hfc2f157_2
$ module help quay.io/biocontainers/andi/0.14--hfc2f157_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### andi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### andi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### andi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### andi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### andi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### andi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### andi

```bash
$ singularity exec <container> /usr/local/bin/andi
$ podman run --it --rm --entrypoint /usr/local/bin/andi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/andi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsl-randist

```bash
$ singularity exec <container> /usr/local/bin/gsl-randist
$ podman run --it --rm --entrypoint /usr/local/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsl-randist   -v ${PWD} -w ${PWD} <container> -c " $@"
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