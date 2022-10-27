---
layout: container
name:  "quay.io/biocontainers/perl-bio-das"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-bio-das/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-bio-das/container.yaml"
updated_at: "2022-10-27 00:29:09.678196"
latest: "1.17--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-bio-das"

versions:
 - "1.17--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-bio-das"
config: {"url": "https://biocontainers.pro/tools/perl-bio-das", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-bio-das", "latest": {"1.17--pl5321hdfd78af_1": "sha256:ae8c8f3cc07ed0b9f3fc159ca9b08f6dfdf78e333fa2b124ab08b2bbedb0394d"}, "tags": {"1.17--pl5321hdfd78af_1": "sha256:ae8c8f3cc07ed0b9f3fc159ca9b08f6dfdf78e333fa2b124ab08b2bbedb0394d"}, "docker": "quay.io/biocontainers/perl-bio-das"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-bio-das.
shpc-registry automated BioContainers addition for perl-bio-das
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-bio-das
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-bio-das:1.17--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-bio-das/1.17--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-bio-das/1.17--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-bio-das-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-das-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-bio-das-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-bio-das-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-bio-das-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-bio-das-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-bio-das

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