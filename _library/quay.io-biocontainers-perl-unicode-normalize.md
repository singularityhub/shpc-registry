---
layout: container
name:  "quay.io/biocontainers/perl-unicode-normalize"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-unicode-normalize/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-unicode-normalize/container.yaml"
updated_at: "2024-11-12 03:37:26.592899"
latest: "1.26--pl5321h4ac6f70_5"
container_url: "https://biocontainers.pro/tools/perl-unicode-normalize"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.26--pl5321h9f5acd7_3"
 - "1.26--pl5321h4ac6f70_5"
description: "shpc-registry automated BioContainers addition for perl-unicode-normalize"
config: {"url": "https://biocontainers.pro/tools/perl-unicode-normalize", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-unicode-normalize", "latest": {"1.26--pl5321h4ac6f70_5": "sha256:046afcdf5f8c53e1914d898fde7029814b4ff2ff502cdba15f200a61810cddac"}, "tags": {"1.26--pl5321h9f5acd7_3": "sha256:3c5ef4cf0560f1b2b868e4ca0747ee2f400e7599033e3905fd1f22edaa39529a", "1.26--pl5321h4ac6f70_5": "sha256:046afcdf5f8c53e1914d898fde7029814b4ff2ff502cdba15f200a61810cddac"}, "docker": "quay.io/biocontainers/perl-unicode-normalize", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-unicode-normalize.
shpc-registry automated BioContainers addition for perl-unicode-normalize
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-unicode-normalize
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-unicode-normalize:1.26--pl5321h4ac6f70_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-unicode-normalize/1.26--pl5321h4ac6f70_5
$ module help quay.io/biocontainers/perl-unicode-normalize/1.26--pl5321h4ac6f70_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-unicode-normalize-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-unicode-normalize-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-unicode-normalize-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-unicode-normalize-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-unicode-normalize-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-unicode-normalize-inspect-deffile:

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