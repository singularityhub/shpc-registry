---
layout: container
name:  "quay.io/biocontainers/perl-perl-version"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-perl-version/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-perl-version/container.yaml"
updated_at: "2025-08-31 03:38:37.173542"
latest: "1.018--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-perl-version"
aliases:
 - "perl-reversion"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.013--pl5321hdfd78af_4"
 - "1.018--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-perl-version"
config: {"url": "https://biocontainers.pro/tools/perl-perl-version", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-perl-version", "latest": {"1.018--pl5321hdfd78af_0": "sha256:5df3a4ed854d3f746b7d8b2a4ab4c1b8c8cdbe118620ecb7c367bf4f7061b7ea"}, "tags": {"1.013--pl5321hdfd78af_4": "sha256:847c782146e4befdc5f3db27641b3abd69ae1e07e91c0cde749c826a9afb30bd", "1.018--pl5321hdfd78af_0": "sha256:5df3a4ed854d3f746b7d8b2a4ab4c1b8c8cdbe118620ecb7c367bf4f7061b7ea"}, "docker": "quay.io/biocontainers/perl-perl-version", "aliases": {"perl-reversion": "/usr/local/bin/perl-reversion", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-perl-version.
shpc-registry automated BioContainers addition for perl-perl-version
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-perl-version
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-perl-version:1.018--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-perl-version/1.018--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-perl-version/1.018--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-perl-version-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-perl-version-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-perl-version-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-perl-version-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-perl-version-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-perl-version-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### perl-reversion

```bash
$ singularity exec <container> /usr/local/bin/perl-reversion
$ podman run --it --rm --entrypoint /usr/local/bin/perl-reversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl-reversion   -v ${PWD} -w ${PWD} <container> -c " $@"
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