---
layout: container
name:  "quay.io/biocontainers/perl-module-scandeps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-module-scandeps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-module-scandeps/container.yaml"
updated_at: "2025-01-27 07:14:43.060455"
latest: "1.33--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-module-scandeps"
aliases:
 - "scandeps.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.31--pl5321hdfd78af_0"
 - "1.32--pl5321hdfd78af_0"
 - "1.33--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-module-scandeps"
config: {"url": "https://biocontainers.pro/tools/perl-module-scandeps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-module-scandeps", "latest": {"1.33--pl5321hdfd78af_0": "sha256:7b5cdd2a1d953b804e6b13da82bbe901e7f456ef29e13b01124bb7bf363cf9d2"}, "tags": {"1.31--pl5321hdfd78af_0": "sha256:41f9cdce004b44452870d0e8b71731f479eb701e5ddc1074aff55a69878b13b8", "1.32--pl5321hdfd78af_0": "sha256:78ca9d66768dc7aa65ce68b1bd744fe5bdcb67f678750b4c0c82783f32fcc2b8", "1.33--pl5321hdfd78af_0": "sha256:7b5cdd2a1d953b804e6b13da82bbe901e7f456ef29e13b01124bb7bf363cf9d2"}, "docker": "quay.io/biocontainers/perl-module-scandeps", "aliases": {"scandeps.pl": "/usr/local/bin/scandeps.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-module-scandeps.
shpc-registry automated BioContainers addition for perl-module-scandeps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-module-scandeps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-module-scandeps:1.33--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-module-scandeps/1.33--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-module-scandeps/1.33--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-module-scandeps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-module-scandeps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-module-scandeps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-module-scandeps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-module-scandeps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-module-scandeps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### scandeps.pl

```bash
$ singularity exec <container> /usr/local/bin/scandeps.pl
$ podman run --it --rm --entrypoint /usr/local/bin/scandeps.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scandeps.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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