---
layout: container
name:  "quay.io/biocontainers/perl-autodie"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-autodie/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-autodie/container.yaml"
updated_at: "2023-04-19 02:48:14.931522"
latest: "2.36--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-autodie"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "2.34--pl5321hdfd78af_0"
 - "2.35--pl5321hdfd78af_0"
 - "2.36--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-autodie"
config: {"url": "https://biocontainers.pro/tools/perl-autodie", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-autodie", "latest": {"2.36--pl5321hdfd78af_0": "sha256:b3db8b19dc2d562876070df9daed77559764f6dab8b3f8ddc9db5388693326db"}, "tags": {"2.34--pl5321hdfd78af_0": "sha256:ea59a18d6d29ab62e6f5a9c1d64d7b6a125f4c6cdc79e2150cfd59d7f3d1ce0a", "2.35--pl5321hdfd78af_0": "sha256:ee4501153ab2e599a751a145070494842132f524e3c6f5c6e5d884ab6a2f6bdd", "2.36--pl5321hdfd78af_0": "sha256:b3db8b19dc2d562876070df9daed77559764f6dab8b3f8ddc9db5388693326db"}, "docker": "quay.io/biocontainers/perl-autodie", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-autodie.
shpc-registry automated BioContainers addition for perl-autodie
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-autodie
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-autodie:2.36--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-autodie/2.36--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-autodie/2.36--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-autodie-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-autodie-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-autodie-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-autodie-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-autodie-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-autodie-inspect-deffile:

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