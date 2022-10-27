---
layout: container
name:  "quay.io/biocontainers/perl-gfacs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-gfacs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/perl-gfacs/container.yaml"
updated_at: "2022-10-27 00:38:47.417124"
latest: "1.1.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-gfacs"
aliases:
 - "gFACs.pl"
versions:
 - "1.1.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-gfacs"
config: {"url": "https://biocontainers.pro/tools/perl-gfacs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-gfacs", "latest": {"1.1.1--hdfd78af_1": "sha256:71f699bb525e581f4820fce9ed2041f36c1d1d4ff34d0b0d463b4a778495b05a"}, "tags": {"1.1.1--hdfd78af_1": "sha256:71f699bb525e581f4820fce9ed2041f36c1d1d4ff34d0b0d463b4a778495b05a"}, "docker": "quay.io/biocontainers/perl-gfacs", "aliases": {"gFACs.pl": "/usr/local/bin/gFACs.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-gfacs.
shpc-registry automated BioContainers addition for perl-gfacs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-gfacs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-gfacs:1.1.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-gfacs/1.1.1--hdfd78af_1
$ module help quay.io/biocontainers/perl-gfacs/1.1.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-gfacs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-gfacs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-gfacs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-gfacs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-gfacs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-gfacs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gFACs.pl

```bash
$ singularity exec <container> /usr/local/bin/gFACs.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gFACs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gFACs.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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