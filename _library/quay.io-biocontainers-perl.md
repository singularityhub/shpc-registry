---
layout: container
name:  "quay.io/biocontainers/perl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl/container.yaml"
updated_at: "2024-03-19 02:58:57.247596"
latest: "5.26.2"
container_url: "https://biocontainers.pro/tools/perl"

versions:
 - "5.26.2"
 - "5.26"
description: "shpc-registry automated BioContainers addition for perl"
config: {"url": "https://biocontainers.pro/tools/perl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl", "latest": {"5.26.2": "sha256:8ae3c6d2fc43fb73efb20e26dd1d780ef05c32977435bb0bdfa670037913848f"}, "tags": {"5.26.2": "sha256:8ae3c6d2fc43fb73efb20e26dd1d780ef05c32977435bb0bdfa670037913848f", "5.26": "sha256:c9e71b7f4d41771ac4b824329936cb1c2161e32f2380629d0744f7e3235a3fde"}, "docker": "quay.io/biocontainers/perl"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl.
shpc-registry automated BioContainers addition for perl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl:5.26.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl/5.26.2
$ module help quay.io/biocontainers/perl/5.26.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl

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