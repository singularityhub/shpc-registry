---
layout: container
name:  "quay.io/biocontainers/perl-getopt-long"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-getopt-long/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-getopt-long/container.yaml"
updated_at: "2024-10-20 03:25:13.559369"
latest: "2.58--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-getopt-long"

versions:
 - "2.52--pl5321hdfd78af_0"
 - "2.53--pl5321hdfd78af_0"
 - "2.54--pl5321hdfd78af_0"
 - "2.58--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-getopt-long"
config: {"url": "https://biocontainers.pro/tools/perl-getopt-long", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-getopt-long", "latest": {"2.58--pl5321hdfd78af_0": "sha256:50a2e558c5fb37878cf869a2f7838c90252ea4ec56e794c96f2b2c0450285e33"}, "tags": {"2.52--pl5321hdfd78af_0": "sha256:0605150d30c518707fdb0ab8469583069a097ed459a8b10ac6aabd34ef36fab1", "2.53--pl5321hdfd78af_0": "sha256:5b6394bf33afd795ab998b3a4aa0eee25988cf64bbdf98d7eab05ec8e0d52a2a", "2.54--pl5321hdfd78af_0": "sha256:c673c0424ea5cc6f0453a4d02ab5decec80b6590d5278967b519aa7be51b880d", "2.58--pl5321hdfd78af_0": "sha256:50a2e558c5fb37878cf869a2f7838c90252ea4ec56e794c96f2b2c0450285e33"}, "docker": "quay.io/biocontainers/perl-getopt-long"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-getopt-long.
shpc-registry automated BioContainers addition for perl-getopt-long
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-getopt-long
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-getopt-long:2.58--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-getopt-long/2.58--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-getopt-long/2.58--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-getopt-long-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-getopt-long-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-getopt-long-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-getopt-long-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-getopt-long-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-getopt-long-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-getopt-long

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