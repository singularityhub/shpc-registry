---
layout: container
name:  "quay.io/biocontainers/perl-gd-svg"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-gd-svg/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-gd-svg/container.yaml"
updated_at: "2022-10-27 00:52:28.856804"
latest: "0.33--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-gd-svg"

versions:
 - "0.33--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-gd-svg"
config: {"url": "https://biocontainers.pro/tools/perl-gd-svg", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-gd-svg", "latest": {"0.33--pl5321hdfd78af_2": "sha256:f3ee1ad731f367a47282851c1842b2e27dd552748199782d7ef16c2e379660b0"}, "tags": {"0.33--pl5321hdfd78af_2": "sha256:f3ee1ad731f367a47282851c1842b2e27dd552748199782d7ef16c2e379660b0"}, "docker": "quay.io/biocontainers/perl-gd-svg"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-gd-svg.
shpc-registry automated BioContainers addition for perl-gd-svg
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-gd-svg
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-gd-svg:0.33--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-gd-svg/0.33--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-gd-svg/0.33--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-gd-svg-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-gd-svg-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-gd-svg-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-gd-svg-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-gd-svg-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-gd-svg-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-gd-svg

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