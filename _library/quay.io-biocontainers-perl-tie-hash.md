---
layout: container
name:  "quay.io/biocontainers/perl-tie-hash"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-tie-hash/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-tie-hash/container.yaml"
updated_at: "2023-07-31 02:36:38.817891"
latest: "1.05--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/perl-tie-hash"

versions:
 - "1.05--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for perl-tie-hash"
config: {"url": "https://biocontainers.pro/tools/perl-tie-hash", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-tie-hash", "latest": {"1.05--pl5321hdfd78af_2": "sha256:7be03007002b6b84bc54157daaf2f4d1d8719ea700731c8a56a1aa1ce26c1b84"}, "tags": {"1.05--pl5321hdfd78af_2": "sha256:7be03007002b6b84bc54157daaf2f4d1d8719ea700731c8a56a1aa1ce26c1b84"}, "docker": "quay.io/biocontainers/perl-tie-hash"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-tie-hash.
shpc-registry automated BioContainers addition for perl-tie-hash
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-tie-hash
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-tie-hash:1.05--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-tie-hash/1.05--pl5321hdfd78af_2
$ module help quay.io/biocontainers/perl-tie-hash/1.05--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-tie-hash-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-tie-hash-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-tie-hash-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-tie-hash-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-tie-hash-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-tie-hash-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-tie-hash

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