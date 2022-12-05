---
layout: container
name:  "quay.io/biocontainers/perl-list-util"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-list-util/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-list-util/container.yaml"
updated_at: "2022-12-05 03:21:54.563588"
latest: "1.38--pl526_1"
container_url: "https://biocontainers.pro/tools/perl-list-util"
aliases:
 - "perl5.26.2"
 - "podselect"
versions:
 - "1.38--pl526_1"
description: "shpc-registry automated BioContainers addition for perl-list-util"
config: {"url": "https://biocontainers.pro/tools/perl-list-util", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-list-util", "latest": {"1.38--pl526_1": "sha256:cb89dc4bc97f7daad3af6bd7b6ed1b4a074f2e040fdb19edfb4e34bfd530d6f7"}, "tags": {"1.38--pl526_1": "sha256:cb89dc4bc97f7daad3af6bd7b6ed1b4a074f2e040fdb19edfb4e34bfd530d6f7"}, "docker": "quay.io/biocontainers/perl-list-util", "aliases": {"perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-list-util.
shpc-registry automated BioContainers addition for perl-list-util
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-list-util
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-list-util:1.38--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-list-util/1.38--pl526_1
$ module help quay.io/biocontainers/perl-list-util/1.38--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-list-util-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-list-util-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-list-util-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-list-util-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-list-util-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-list-util-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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