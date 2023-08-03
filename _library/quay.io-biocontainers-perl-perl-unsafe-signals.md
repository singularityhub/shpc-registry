---
layout: container
name:  "quay.io/biocontainers/perl-perl-unsafe-signals"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-perl-unsafe-signals/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-perl-unsafe-signals/container.yaml"
updated_at: "2023-08-03 02:49:05.421031"
latest: "0.03--pl5321h4ac6f70_7"
container_url: "https://biocontainers.pro/tools/perl-perl-unsafe-signals"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.03--pl5321h9f5acd7_5"
 - "0.03--pl5321h9f5acd7_6"
 - "0.03--pl5321h4ac6f70_7"
description: "shpc-registry automated BioContainers addition for perl-perl-unsafe-signals"
config: {"url": "https://biocontainers.pro/tools/perl-perl-unsafe-signals", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-perl-unsafe-signals", "latest": {"0.03--pl5321h4ac6f70_7": "sha256:5f8eececff8dcec4b015d3bdafded6e8092f0b8182c511893c4a4b25f4a1b39f"}, "tags": {"0.03--pl5321h9f5acd7_5": "sha256:a226af0249430febc7f9def6c31ec331c6b5e0600b4e1fd775cc8b7d2f100596", "0.03--pl5321h9f5acd7_6": "sha256:e59a24093c098b57883c9eae43e660784768505ad0fc34813313f6785af7ed7c", "0.03--pl5321h4ac6f70_7": "sha256:5f8eececff8dcec4b015d3bdafded6e8092f0b8182c511893c4a4b25f4a1b39f"}, "docker": "quay.io/biocontainers/perl-perl-unsafe-signals", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-perl-unsafe-signals.
shpc-registry automated BioContainers addition for perl-perl-unsafe-signals
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-perl-unsafe-signals
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-perl-unsafe-signals:0.03--pl5321h4ac6f70_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-perl-unsafe-signals/0.03--pl5321h4ac6f70_7
$ module help quay.io/biocontainers/perl-perl-unsafe-signals/0.03--pl5321h4ac6f70_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-perl-unsafe-signals-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-perl-unsafe-signals-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-perl-unsafe-signals-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-perl-unsafe-signals-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-perl-unsafe-signals-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-perl-unsafe-signals-inspect-deffile:

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