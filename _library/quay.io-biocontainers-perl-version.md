---
layout: container
name:  "quay.io/biocontainers/perl-version"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-version/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-version/container.yaml"
updated_at: "2024-08-12 03:48:32.236304"
latest: "0.9924--pl5321hec16e2b_2"
container_url: "https://biocontainers.pro/tools/perl-version"

versions:
 - "0.9924--pl5321hec16e2b_2"
description: "shpc-registry automated BioContainers addition for perl-version"
config: {"url": "https://biocontainers.pro/tools/perl-version", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-version", "latest": {"0.9924--pl5321hec16e2b_2": "sha256:998cd490fc1f1818805d76d976b72ca52e8ca530a43072aad8bc138788487aeb"}, "tags": {"0.9924--pl5321hec16e2b_2": "sha256:998cd490fc1f1818805d76d976b72ca52e8ca530a43072aad8bc138788487aeb"}, "docker": "quay.io/biocontainers/perl-version"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-version.
shpc-registry automated BioContainers addition for perl-version
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-version
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-version:0.9924--pl5321hec16e2b_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-version/0.9924--pl5321hec16e2b_2
$ module help quay.io/biocontainers/perl-version/0.9924--pl5321hec16e2b_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-version-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-version-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-version-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-version-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-version-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-version-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-version

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