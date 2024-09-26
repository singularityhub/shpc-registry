---
layout: container
name:  "quay.io/biocontainers/geco2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/geco2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/geco2/container.yaml"
updated_at: "2024-09-26 10:24:20.442421"
latest: "1.1--h031d066_4"
container_url: "https://biocontainers.pro/tools/geco2"
aliases:
 - "GeCo2"
 - "GeDe2"
versions:
 - "1.1--hec16e2b_2"
 - "1.1--h031d066_4"
description: "shpc-registry automated BioContainers addition for geco2"
config: {"url": "https://biocontainers.pro/tools/geco2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for geco2", "latest": {"1.1--h031d066_4": "sha256:e24af23e3dc0e029ed9a3b51fb3e40aea2599cf2fbdb988dad4342b69dfbce4f"}, "tags": {"1.1--hec16e2b_2": "sha256:07cb2d25452da4e75b8d7a91367497a010598d04cffb7e36d0d31606d93bf0a3", "1.1--h031d066_4": "sha256:e24af23e3dc0e029ed9a3b51fb3e40aea2599cf2fbdb988dad4342b69dfbce4f"}, "docker": "quay.io/biocontainers/geco2", "aliases": {"GeCo2": "/usr/local/bin/GeCo2", "GeDe2": "/usr/local/bin/GeDe2"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/geco2.
shpc-registry automated BioContainers addition for geco2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/geco2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/geco2:1.1--h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/geco2/1.1--h031d066_4
$ module help quay.io/biocontainers/geco2/1.1--h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### geco2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### geco2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### geco2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### geco2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### geco2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### geco2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GeCo2

```bash
$ singularity exec <container> /usr/local/bin/GeCo2
$ podman run --it --rm --entrypoint /usr/local/bin/GeCo2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeCo2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### GeDe2

```bash
$ singularity exec <container> /usr/local/bin/GeDe2
$ podman run --it --rm --entrypoint /usr/local/bin/GeDe2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GeDe2   -v ${PWD} -w ${PWD} <container> -c " $@"
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