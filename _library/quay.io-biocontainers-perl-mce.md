---
layout: container
name:  "quay.io/biocontainers/perl-mce"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-mce/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-mce/container.yaml"
updated_at: "2023-06-20 02:47:11.704320"
latest: "1.884--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-mce"

versions:
 - "1.881--pl5321hdfd78af_0"
 - "1.884--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-mce"
config: {"url": "https://biocontainers.pro/tools/perl-mce", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-mce", "latest": {"1.884--pl5321hdfd78af_0": "sha256:299ee7e7cfd32dee3bc6592345517af2ad1fbda882aa5dee08595d76ee662b2d"}, "tags": {"1.881--pl5321hdfd78af_0": "sha256:2e83ce1420d72486b317d36f4b93a19af6b2ca3f9ba3da4c74eb1b6117431b11", "1.884--pl5321hdfd78af_0": "sha256:299ee7e7cfd32dee3bc6592345517af2ad1fbda882aa5dee08595d76ee662b2d"}, "docker": "quay.io/biocontainers/perl-mce"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-mce.
shpc-registry automated BioContainers addition for perl-mce
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-mce
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-mce:1.884--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-mce/1.884--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-mce/1.884--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-mce-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-mce-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-mce-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-mce-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-mce-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-mce-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-mce

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