---
layout: container
name:  "quay.io/biocontainers/perl-digest-sha1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-digest-sha1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-digest-sha1/container.yaml"
updated_at: "2025-04-10 03:32:18.639854"
latest: "2.13--pl5321h9948957_8"
container_url: "https://biocontainers.pro/tools/perl-digest-sha1"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.13--pl5321h9f5acd7_3"
 - "2.13--pl5321h4ac6f70_5"
 - "2.13--pl5321h4ac6f70_6"
 - "2.13--pl5321h4ac6f70_7"
 - "2.13--pl5321h9948957_8"
description: "shpc-registry automated BioContainers addition for perl-digest-sha1"
config: {"url": "https://biocontainers.pro/tools/perl-digest-sha1", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-digest-sha1", "latest": {"2.13--pl5321h9948957_8": "sha256:b35120ff61bf8ea8c97041679dde3c256cca5a29c3c3c833e94a19d5b468bc59"}, "tags": {"2.13--pl5321h9f5acd7_3": "sha256:f42bc242a9225e70c5c087891512f40a305b65822a1cf8185817d3d910efe678", "2.13--pl5321h4ac6f70_5": "sha256:e7fac37a8d8ea78d656b05a8c93f1cacb1b33efe147fe2d483078f308c5e7f36", "2.13--pl5321h4ac6f70_6": "sha256:30514a56bf255f77b5d2d0c6eed35f394f3703eab2a70417f652d2ff16afbbce", "2.13--pl5321h4ac6f70_7": "sha256:851433dc5401d0445d1f25bfedce9ec385f95bc21e9ea62290ecf01714405fc3", "2.13--pl5321h9948957_8": "sha256:b35120ff61bf8ea8c97041679dde3c256cca5a29c3c3c833e94a19d5b468bc59"}, "docker": "quay.io/biocontainers/perl-digest-sha1", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-digest-sha1.
shpc-registry automated BioContainers addition for perl-digest-sha1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-digest-sha1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-digest-sha1:2.13--pl5321h9948957_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-digest-sha1/2.13--pl5321h9948957_8
$ module help quay.io/biocontainers/perl-digest-sha1/2.13--pl5321h9948957_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-digest-sha1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-digest-sha1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-digest-sha1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-digest-sha1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-digest-sha1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-digest-sha1-inspect-deffile:

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