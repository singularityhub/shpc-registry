---
layout: container
name:  "quay.io/biocontainers/r-phewas"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-phewas/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-phewas/container.yaml"
updated_at: "2024-08-25 03:26:19.239309"
latest: "0.99.6--r43haf399aa_0"
container_url: "https://biocontainers.pro/tools/r-phewas"

versions:
 - "0.12.1--r41hb2e0dee_4"
 - "0.12.1--r42hb2e0dee_5"
 - "0.12.1--r42haf399aa_7"
 - "0.12.1--r43haf399aa_8"
 - "0.99.6--r43haf399aa_0"
description: "shpc-registry automated BioContainers addition for r-phewas"
config: {"url": "https://biocontainers.pro/tools/r-phewas", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-phewas", "latest": {"0.99.6--r43haf399aa_0": "sha256:73e63a8782b93967211eff9859a5f4fbd967b6537e3eb513d75ee01884485308"}, "tags": {"0.12.1--r41hb2e0dee_4": "sha256:c69fd88cfedca31216d3959e4e1977466424ffc77b82c9b5b793c921bcbe8540", "0.12.1--r42hb2e0dee_5": "sha256:35f67ae0f71b6f20c1fc80dec89d8d365635fb832f4c289c3b3cff6469c289ab", "0.12.1--r42haf399aa_7": "sha256:3b6a56802ed9fc47bc36f4029f5482624892337c64ffce178666aba8c807e28f", "0.12.1--r43haf399aa_8": "sha256:4ddac93765c0c6582973e078b6d83db4421d272935c3d5298d4a4b5d75179672", "0.99.6--r43haf399aa_0": "sha256:73e63a8782b93967211eff9859a5f4fbd967b6537e3eb513d75ee01884485308"}, "docker": "quay.io/biocontainers/r-phewas"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-phewas.
shpc-registry automated BioContainers addition for r-phewas
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-phewas
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-phewas:0.99.6--r43haf399aa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-phewas/0.99.6--r43haf399aa_0
$ module help quay.io/biocontainers/r-phewas/0.99.6--r43haf399aa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-phewas-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-phewas-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-phewas-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-phewas-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-phewas-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-phewas-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-phewas

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