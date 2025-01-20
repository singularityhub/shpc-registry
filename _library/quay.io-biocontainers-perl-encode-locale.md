---
layout: container
name:  "quay.io/biocontainers/perl-encode-locale"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-encode-locale/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-encode-locale/container.yaml"
updated_at: "2025-01-20 03:00:19.195855"
latest: "1.05--pl5321hdfd78af_7"
container_url: "https://biocontainers.pro/tools/perl-encode-locale"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.05--pl5321hdfd78af_7"
description: "shpc-registry automated BioContainers addition for perl-encode-locale"
config: {"url": "https://biocontainers.pro/tools/perl-encode-locale", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-encode-locale", "latest": {"1.05--pl5321hdfd78af_7": "sha256:c9db34d7959007fba7cc5697272ff5e7c6b1d30c3ff9f35b48a5e47c7a508f6c"}, "tags": {"1.05--pl5321hdfd78af_7": "sha256:c9db34d7959007fba7cc5697272ff5e7c6b1d30c3ff9f35b48a5e47c7a508f6c"}, "docker": "quay.io/biocontainers/perl-encode-locale", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-encode-locale.
shpc-registry automated BioContainers addition for perl-encode-locale
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-encode-locale
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-encode-locale:1.05--pl5321hdfd78af_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-encode-locale/1.05--pl5321hdfd78af_7
$ module help quay.io/biocontainers/perl-encode-locale/1.05--pl5321hdfd78af_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-encode-locale-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-encode-locale-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-encode-locale-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-encode-locale-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-encode-locale-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-encode-locale-inspect-deffile:

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