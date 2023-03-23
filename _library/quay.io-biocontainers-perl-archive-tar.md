---
layout: container
name:  "quay.io/biocontainers/perl-archive-tar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-archive-tar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-archive-tar/container.yaml"
updated_at: "2023-03-23 03:17:00.201589"
latest: "2.40--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-archive-tar"

versions:
 - "2.40--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-archive-tar"
config: {"url": "https://biocontainers.pro/tools/perl-archive-tar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-archive-tar", "latest": {"2.40--pl5321hdfd78af_0": "sha256:f8b9416efe4f8eb76186b80bd0c7e2d549aa3f0da0c3a539a44f90f1c41931ff"}, "tags": {"2.40--pl5321hdfd78af_0": "sha256:f8b9416efe4f8eb76186b80bd0c7e2d549aa3f0da0c3a539a44f90f1c41931ff"}, "docker": "quay.io/biocontainers/perl-archive-tar"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-archive-tar.
shpc-registry automated BioContainers addition for perl-archive-tar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-archive-tar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-archive-tar:2.40--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-archive-tar/2.40--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-archive-tar/2.40--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-archive-tar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-archive-tar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-archive-tar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-archive-tar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-archive-tar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-archive-tar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-archive-tar

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