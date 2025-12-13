---
layout: container
name:  "quay.io/biocontainers/dartunifrac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dartunifrac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dartunifrac/container.yaml"
updated_at: "2025-12-13 03:55:31.280426"
latest: "0.2.7--h3dc2dae_0"
container_url: "https://biocontainers.pro/tools/dartunifrac"
aliases:
 - "dartunifrac"
 - "striped_unifrac"
versions:
 - "0.2.3--h3ab6199_0"
 - "0.2.5--h3dc2dae_0"
 - "0.2.6--h3dc2dae_0"
 - "0.2.7--h3dc2dae_0"
description: "singularity registry hpc automated addition for dartunifrac"
config: {"url": "https://biocontainers.pro/tools/dartunifrac", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for dartunifrac", "latest": {"0.2.7--h3dc2dae_0": "sha256:e1c3300346233f4c407823384bd50cd938c7e55545830f9cae1b42005f0e9986"}, "tags": {"0.2.3--h3ab6199_0": "sha256:43589b888cd2003e40093f81513a8fb32a2626291204461e8da5d7d3d4d808b2", "0.2.5--h3dc2dae_0": "sha256:f8a2f5851a71b0358b2f6baa0c03ef7c236bb52623e598807b30b4e734869f8a", "0.2.6--h3dc2dae_0": "sha256:ea6f3191a74b7e42f3e262ca474b51a6cb455f8fda4398fb966aa7705fdd3927", "0.2.7--h3dc2dae_0": "sha256:e1c3300346233f4c407823384bd50cd938c7e55545830f9cae1b42005f0e9986"}, "docker": "quay.io/biocontainers/dartunifrac", "aliases": {"dartunifrac": "/usr/local/bin/dartunifrac", "striped_unifrac": "/usr/local/bin/striped_unifrac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dartunifrac.
singularity registry hpc automated addition for dartunifrac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dartunifrac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dartunifrac:0.2.7--h3dc2dae_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dartunifrac/0.2.7--h3dc2dae_0
$ module help quay.io/biocontainers/dartunifrac/0.2.7--h3dc2dae_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dartunifrac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dartunifrac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dartunifrac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dartunifrac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dartunifrac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dartunifrac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dartunifrac

```bash
$ singularity exec <container> /usr/local/bin/dartunifrac
$ podman run --it --rm --entrypoint /usr/local/bin/dartunifrac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dartunifrac   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### striped_unifrac

```bash
$ singularity exec <container> /usr/local/bin/striped_unifrac
$ podman run --it --rm --entrypoint /usr/local/bin/striped_unifrac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/striped_unifrac   -v ${PWD} -w ${PWD} <container> -c " $@"
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