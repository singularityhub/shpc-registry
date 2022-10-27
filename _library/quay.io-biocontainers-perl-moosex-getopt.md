---
layout: container
name:  "quay.io/biocontainers/perl-moosex-getopt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-moosex-getopt/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-moosex-getopt/container.yaml"
updated_at: "2022-10-27 00:32:19.250802"
latest: "0.75--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-moosex-getopt"

versions:
 - "0.75--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-moosex-getopt"
config: {"url": "https://biocontainers.pro/tools/perl-moosex-getopt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-moosex-getopt", "latest": {"0.75--pl5321hdfd78af_0": "sha256:0096db86ed5952cd9386f61cce936c0e840b5b56489941d6d4a89214e190b93f"}, "tags": {"0.75--pl5321hdfd78af_0": "sha256:0096db86ed5952cd9386f61cce936c0e840b5b56489941d6d4a89214e190b93f"}, "docker": "quay.io/biocontainers/perl-moosex-getopt"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-moosex-getopt.
shpc-registry automated BioContainers addition for perl-moosex-getopt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-moosex-getopt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-moosex-getopt:0.75--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-moosex-getopt/0.75--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-moosex-getopt/0.75--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-moosex-getopt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-getopt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-moosex-getopt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-moosex-getopt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-moosex-getopt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-moosex-getopt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-moosex-getopt

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