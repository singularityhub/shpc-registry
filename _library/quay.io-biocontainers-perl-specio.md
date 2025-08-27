---
layout: container
name:  "quay.io/biocontainers/perl-specio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-specio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-specio/container.yaml"
updated_at: "2025-08-27 03:52:01.198800"
latest: "0.52--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-specio"

versions:
 - "0.48--pl5321hdfd78af_0"
 - "0.49--pl5321hdfd78af_0"
 - "0.50--pl5321hdfd78af_0"
 - "0.52--pl5321hdfd78af_0"
 - "0.51--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-specio"
config: {"url": "https://biocontainers.pro/tools/perl-specio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-specio", "latest": {"0.52--pl5321hdfd78af_0": "sha256:36dc486a514e733b9c20b544c6161286120db4c6570df7b0f8bc1a435e479ce6"}, "tags": {"0.48--pl5321hdfd78af_0": "sha256:f741ba368c0e51daa4b29922c142d4cc119d03d148a861a12f47413a08e68839", "0.49--pl5321hdfd78af_0": "sha256:39ead8cbc457b1f7351b4a7d7ae799fe55b795de140af1ca05f2e103411212de", "0.50--pl5321hdfd78af_0": "sha256:701b85a4e3c2928ec8113db77406c8b667e5d23567fa8dc52d59a9ba68e07b1b", "0.52--pl5321hdfd78af_0": "sha256:36dc486a514e733b9c20b544c6161286120db4c6570df7b0f8bc1a435e479ce6", "0.51--pl5321hdfd78af_0": "sha256:b6dd99717d4853d974d86a08f43c76ab8c294d775fba15c138d5abb5f8b041ab"}, "docker": "quay.io/biocontainers/perl-specio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-specio.
shpc-registry automated BioContainers addition for perl-specio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-specio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-specio:0.52--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-specio/0.52--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-specio/0.52--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-specio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-specio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-specio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-specio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-specio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-specio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-specio

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