---
layout: container
name:  "quay.io/biocontainers/perl-locale"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-locale/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-locale/container.yaml"
updated_at: "2025-09-21 03:21:58.861588"
latest: "1.03--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-locale"

versions:
 - "1.03--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-locale"
config: {"url": "https://biocontainers.pro/tools/perl-locale", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-locale", "latest": {"1.03--pl5321hdfd78af_2": "sha256:bec45597b32290d6da6da8327a6d08144383c38ad94ca843169c2faca2e90ac3"}, "tags": {"1.03--pl5321hdfd78af_2": "sha256:bec45597b32290d6da6da8327a6d08144383c38ad94ca843169c2faca2e90ac3"}, "docker": "quay.io/biocontainers/perl-locale"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-locale.
shpc-registry automated BioContainers addition for perl-locale
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-locale
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-locale:1.03--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-locale/1.03--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-locale/1.03--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-locale-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-locale-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-locale-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-locale-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-locale-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-locale-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-locale

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