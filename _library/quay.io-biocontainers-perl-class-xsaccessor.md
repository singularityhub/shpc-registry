---
layout: container
name:  "quay.io/biocontainers/perl-class-xsaccessor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-class-xsaccessor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-class-xsaccessor/container.yaml"
updated_at: "2024-02-08 08:17:26.722544"
latest: "1.19--pl5321h031d066_6"
container_url: "https://biocontainers.pro/tools/perl-class-xsaccessor"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.19--pl5321hec16e2b_5"
 - "1.19--pl5321h031d066_6"
description: "shpc-registry automated BioContainers addition for perl-class-xsaccessor"
config: {"url": "https://biocontainers.pro/tools/perl-class-xsaccessor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-class-xsaccessor", "latest": {"1.19--pl5321h031d066_6": "sha256:0206f0da3399a6abb1fa1682295add6067c862bac08bdd348d0010b7682a7e80"}, "tags": {"1.19--pl5321hec16e2b_5": "sha256:d17e8dee2f5b03e6a7c139eeb7dc0fb564b527ad826c5883521b7f8d839bc446", "1.19--pl5321h031d066_6": "sha256:0206f0da3399a6abb1fa1682295add6067c862bac08bdd348d0010b7682a7e80"}, "docker": "quay.io/biocontainers/perl-class-xsaccessor", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-class-xsaccessor.
shpc-registry automated BioContainers addition for perl-class-xsaccessor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-class-xsaccessor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-class-xsaccessor:1.19--pl5321h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-class-xsaccessor/1.19--pl5321h031d066_6
$ module help quay.io/biocontainers/perl-class-xsaccessor/1.19--pl5321h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-class-xsaccessor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-class-xsaccessor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-class-xsaccessor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-class-xsaccessor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-class-xsaccessor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-class-xsaccessor-inspect-deffile:

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