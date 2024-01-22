---
layout: container
name:  "quay.io/biocontainers/perl-text-tabs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-text-tabs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-text-tabs/container.yaml"
updated_at: "2024-01-22 03:35:53.956390"
latest: "2013.0523--pl526_1"
container_url: "https://biocontainers.pro/tools/perl-text-tabs"

versions:
 - "2013.0523--pl526_1"
description: "shpc-registry automated BioContainers addition for perl-text-tabs"
config: {"url": "https://biocontainers.pro/tools/perl-text-tabs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-text-tabs", "latest": {"2013.0523--pl526_1": "sha256:67237fa3f96e037df27874d504bc6a25fc0c33c99f793b5113afa874f164b3b8"}, "tags": {"2013.0523--pl526_1": "sha256:67237fa3f96e037df27874d504bc6a25fc0c33c99f793b5113afa874f164b3b8"}, "docker": "quay.io/biocontainers/perl-text-tabs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-text-tabs.
shpc-registry automated BioContainers addition for perl-text-tabs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-text-tabs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-text-tabs:2013.0523--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-text-tabs/2013.0523--pl526_1
$ module help quay.io/biocontainers/perl-text-tabs/2013.0523--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-text-tabs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-text-tabs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-text-tabs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-text-tabs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-text-tabs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-text-tabs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-text-tabs

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