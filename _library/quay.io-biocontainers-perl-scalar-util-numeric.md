---
layout: container
name:  "quay.io/biocontainers/perl-scalar-util-numeric"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-scalar-util-numeric/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-scalar-util-numeric/container.yaml"
updated_at: "2024-11-18 16:59:07.485389"
latest: "0.40--pl5321h031d066_5"
container_url: "https://biocontainers.pro/tools/perl-scalar-util-numeric"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.40--pl5321hec16e2b_3"
 - "0.40--pl5321h031d066_5"
description: "shpc-registry automated BioContainers addition for perl-scalar-util-numeric"
config: {"url": "https://biocontainers.pro/tools/perl-scalar-util-numeric", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-scalar-util-numeric", "latest": {"0.40--pl5321h031d066_5": "sha256:590cfc0921bfff8d37fcfe26294fe21f5598052dcd5b197b87d5a6a148ca493b"}, "tags": {"0.40--pl5321hec16e2b_3": "sha256:266574ab139294d1347b0db32570df571cccabe19857a3f74cbf2d6962f4d724", "0.40--pl5321h031d066_5": "sha256:590cfc0921bfff8d37fcfe26294fe21f5598052dcd5b197b87d5a6a148ca493b"}, "docker": "quay.io/biocontainers/perl-scalar-util-numeric", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-scalar-util-numeric.
shpc-registry automated BioContainers addition for perl-scalar-util-numeric
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-scalar-util-numeric
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-scalar-util-numeric:0.40--pl5321h031d066_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-scalar-util-numeric/0.40--pl5321h031d066_5
$ module help quay.io/biocontainers/perl-scalar-util-numeric/0.40--pl5321h031d066_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-scalar-util-numeric-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-scalar-util-numeric-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-scalar-util-numeric-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-scalar-util-numeric-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-scalar-util-numeric-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-scalar-util-numeric-inspect-deffile:

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