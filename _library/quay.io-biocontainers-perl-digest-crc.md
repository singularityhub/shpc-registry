---
layout: container
name:  "quay.io/biocontainers/perl-digest-crc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-digest-crc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-digest-crc/container.yaml"
updated_at: "2023-06-23 03:32:33.287802"
latest: "0.23--pl5321h031d066_4"
container_url: "https://biocontainers.pro/tools/perl-digest-crc"

versions:
 - "0.23--pl5321hec16e2b_2"
 - "0.23--pl5321h031d066_4"
description: "shpc-registry automated BioContainers addition for perl-digest-crc"
config: {"url": "https://biocontainers.pro/tools/perl-digest-crc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-digest-crc", "latest": {"0.23--pl5321h031d066_4": "sha256:37459cf4d5af65211a23bd6a4731a122e81b7cc680c103bdcd46475776649676"}, "tags": {"0.23--pl5321hec16e2b_2": "sha256:980dcd83f0f442d4e4db16bf476eed02493ead28e925c31b222a2dfb2acf95b3", "0.23--pl5321h031d066_4": "sha256:37459cf4d5af65211a23bd6a4731a122e81b7cc680c103bdcd46475776649676"}, "docker": "quay.io/biocontainers/perl-digest-crc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-digest-crc.
shpc-registry automated BioContainers addition for perl-digest-crc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-digest-crc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-digest-crc:0.23--pl5321h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-digest-crc/0.23--pl5321h031d066_4
$ module help quay.io/biocontainers/perl-digest-crc/0.23--pl5321h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-digest-crc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-digest-crc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-digest-crc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-digest-crc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-digest-crc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-digest-crc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-digest-crc

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