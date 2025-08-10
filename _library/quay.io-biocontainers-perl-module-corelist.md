---
layout: container
name:  "quay.io/biocontainers/perl-module-corelist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-module-corelist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-module-corelist/container.yaml"
updated_at: "2025-08-10 04:15:16.999470"
latest: "5.20250702--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-module-corelist"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "5.20220620--pl5321hdfd78af_0"
 - "5.20250702--pl5321hdfd78af_0"
 - "5.20250528--pl5321hdfd78af_0"
 - "5.20230220--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-module-corelist"
config: {"url": "https://biocontainers.pro/tools/perl-module-corelist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-module-corelist", "latest": {"5.20250702--pl5321hdfd78af_0": "sha256:5457bec1bfa8fcdf7631e7aaf11f8091f8eafdf35f9039693bde9accc9e91d2e"}, "tags": {"5.20220620--pl5321hdfd78af_0": "sha256:8fbf203956ca52543bd5756676fe67fac8674acabb92c1dace18a2b873779b0e", "5.20250702--pl5321hdfd78af_0": "sha256:5457bec1bfa8fcdf7631e7aaf11f8091f8eafdf35f9039693bde9accc9e91d2e", "5.20250528--pl5321hdfd78af_0": "sha256:7b92e1fa262f3be576aa622788eb54b5eee15f426b30f6a02a7b28ec631f15b3", "5.20230220--pl5321hdfd78af_0": "sha256:b655594d650f57cd344cdef061dd74508069c979695f414d2b7b1adb9a08b5fc"}, "docker": "quay.io/biocontainers/perl-module-corelist", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-module-corelist.
shpc-registry automated BioContainers addition for perl-module-corelist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-module-corelist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-module-corelist:5.20250702--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-module-corelist/5.20250702--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-module-corelist/5.20250702--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-module-corelist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-module-corelist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-module-corelist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-module-corelist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-module-corelist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-module-corelist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.32.1

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.1
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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