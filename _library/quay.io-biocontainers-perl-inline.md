---
layout: container
name:  "quay.io/biocontainers/perl-inline"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-inline/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-inline/container.yaml"
updated_at: "2022-11-15 00:11:09.281281"
latest: "0.86--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-inline"

versions:
 - "0.86--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-inline"
config: {"url": "https://biocontainers.pro/tools/perl-inline", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-inline", "latest": {"0.86--pl5321hdfd78af_0": "sha256:ac3abd535af748ced430327458b4528d5780dbb174e4a4af0d0a262de15c46d5"}, "tags": {"0.86--pl5321hdfd78af_0": "sha256:ac3abd535af748ced430327458b4528d5780dbb174e4a4af0d0a262de15c46d5"}, "docker": "quay.io/biocontainers/perl-inline"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-inline.
shpc-registry automated BioContainers addition for perl-inline
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-inline
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-inline:0.86--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-inline/0.86--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-inline/0.86--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-inline-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-inline-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-inline-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-inline-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-inline-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-inline-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-inline

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