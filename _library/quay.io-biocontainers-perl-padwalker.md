---
layout: container
name:  "quay.io/biocontainers/perl-padwalker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-padwalker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-padwalker/container.yaml"
updated_at: "2024-07-05 02:57:36.046035"
latest: "2.5--pl5321h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/perl-padwalker"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.5--pl5321h9f5acd7_1"
 - "2.5--pl5321h9f5acd7_2"
 - "2.5--pl5321h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for perl-padwalker"
config: {"url": "https://biocontainers.pro/tools/perl-padwalker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-padwalker", "latest": {"2.5--pl5321h4ac6f70_3": "sha256:e4055c5f3581757c80b50413926935faccc6516f329075c0feb7062165e6163f"}, "tags": {"2.5--pl5321h9f5acd7_1": "sha256:24eeab9e13960ba2cd36c26ab16336747bf26da38f104d36f0e83de6d1ec4050", "2.5--pl5321h9f5acd7_2": "sha256:48759a891279a73296f88a0221290d0e44ec720905107dbda8f9f95da66afd0f", "2.5--pl5321h4ac6f70_3": "sha256:e4055c5f3581757c80b50413926935faccc6516f329075c0feb7062165e6163f"}, "docker": "quay.io/biocontainers/perl-padwalker", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-padwalker.
shpc-registry automated BioContainers addition for perl-padwalker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-padwalker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-padwalker:2.5--pl5321h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-padwalker/2.5--pl5321h4ac6f70_3
$ module help quay.io/biocontainers/perl-padwalker/2.5--pl5321h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-padwalker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-padwalker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-padwalker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-padwalker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-padwalker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-padwalker-inspect-deffile:

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