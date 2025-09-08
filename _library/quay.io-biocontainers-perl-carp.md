---
layout: container
name:  "quay.io/biocontainers/perl-carp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-carp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-carp/container.yaml"
updated_at: "2025-09-08 05:04:21.082036"
latest: "1.38--pl5321hdfd78af_4"
container_url: "https://biocontainers.pro/tools/perl-carp"

versions:
 - "1.38--pl5321hdfd78af_4"
description: "shpc-registry automated BioContainers addition for perl-carp"
config: {"url": "https://biocontainers.pro/tools/perl-carp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-carp", "latest": {"1.38--pl5321hdfd78af_4": "sha256:fe57f6fce704cf50efe32419a1a8ee115e2b5c1f113d4327d2d057150f70f822"}, "tags": {"1.38--pl5321hdfd78af_4": "sha256:fe57f6fce704cf50efe32419a1a8ee115e2b5c1f113d4327d2d057150f70f822"}, "docker": "quay.io/biocontainers/perl-carp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-carp.
shpc-registry automated BioContainers addition for perl-carp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-carp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-carp:1.38--pl5321hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-carp/1.38--pl5321hdfd78af_4
$ module help quay.io/biocontainers/perl-carp/1.38--pl5321hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-carp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-carp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-carp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-carp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-carp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-carp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-carp

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