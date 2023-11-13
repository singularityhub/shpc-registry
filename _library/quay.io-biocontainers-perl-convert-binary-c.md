---
layout: container
name:  "quay.io/biocontainers/perl-convert-binary-c"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-convert-binary-c/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-convert-binary-c/container.yaml"
updated_at: "2023-11-13 02:55:03.776723"
latest: "0.84--pl5321h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/perl-convert-binary-c"
aliases:
 - "ccconfig"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.84--pl5321h9f5acd7_1"
 - "0.84--pl5321h9f5acd7_2"
 - "0.84--pl5321h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for perl-convert-binary-c"
config: {"url": "https://biocontainers.pro/tools/perl-convert-binary-c", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-convert-binary-c", "latest": {"0.84--pl5321h4ac6f70_3": "sha256:62f2118316c10d668f620f1b39c4ba2857ad52147c3af3172354023567f6987a"}, "tags": {"0.84--pl5321h9f5acd7_1": "sha256:e6e39cf20f8d688220197cfc3d3e584a9002c0ac4ad89b7493e0d67cc0f7ccd2", "0.84--pl5321h9f5acd7_2": "sha256:22a7aff8c72a3057d0d9a921cb4e6fbf385d62e83b0b6b3af0968e0ff72c0bfd", "0.84--pl5321h4ac6f70_3": "sha256:62f2118316c10d668f620f1b39c4ba2857ad52147c3af3172354023567f6987a"}, "docker": "quay.io/biocontainers/perl-convert-binary-c", "aliases": {"ccconfig": "/usr/local/bin/ccconfig", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-convert-binary-c.
shpc-registry automated BioContainers addition for perl-convert-binary-c
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-convert-binary-c
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-convert-binary-c:0.84--pl5321h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-convert-binary-c/0.84--pl5321h4ac6f70_3
$ module help quay.io/biocontainers/perl-convert-binary-c/0.84--pl5321h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-convert-binary-c-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-convert-binary-c-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-convert-binary-c-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-convert-binary-c-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-convert-binary-c-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-convert-binary-c-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ccconfig

```bash
$ singularity exec <container> /usr/local/bin/ccconfig
$ podman run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ccconfig   -v ${PWD} -w ${PWD} <container> -c " $@"
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