---
layout: container
name:  "quay.io/biocontainers/metagenome-atlas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metagenome-atlas/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metagenome-atlas/container.yaml"
updated_at: "2022-10-27 00:49:21.343824"
latest: "2.9.1--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/metagenome-atlas"
aliases:
 - "atlas"
 - "cookiecutter"
 - "mamba-package"
 - "slugify"
versions:
 - "2.9.1--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for metagenome-atlas"
config: {"url": "https://biocontainers.pro/tools/metagenome-atlas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metagenome-atlas", "latest": {"2.9.1--pyhdfd78af_0": "sha256:5b24ec8e8747ee48f0b7f8b690d574e026617895f4ebd37e777878634885faca"}, "tags": {"2.9.1--pyhdfd78af_0": "sha256:5b24ec8e8747ee48f0b7f8b690d574e026617895f4ebd37e777878634885faca"}, "docker": "quay.io/biocontainers/metagenome-atlas", "aliases": {"atlas": "/usr/local/bin/atlas", "cookiecutter": "/usr/local/bin/cookiecutter", "mamba-package": "/usr/local/bin/mamba-package", "slugify": "/usr/local/bin/slugify"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metagenome-atlas.
shpc-registry automated BioContainers addition for metagenome-atlas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metagenome-atlas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metagenome-atlas:2.9.1--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metagenome-atlas/2.9.1--pyhdfd78af_0
$ module help quay.io/biocontainers/metagenome-atlas/2.9.1--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metagenome-atlas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metagenome-atlas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metagenome-atlas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metagenome-atlas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metagenome-atlas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metagenome-atlas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### atlas

```bash
$ singularity exec <container> /usr/local/bin/atlas
$ podman run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/atlas   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cookiecutter

```bash
$ singularity exec <container> /usr/local/bin/cookiecutter
$ podman run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cookiecutter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mamba-package

```bash
$ singularity exec <container> /usr/local/bin/mamba-package
$ podman run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mamba-package   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slugify

```bash
$ singularity exec <container> /usr/local/bin/slugify
$ podman run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slugify   -v ${PWD} -w ${PWD} <container> -c " $@"
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