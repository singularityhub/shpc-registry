---
layout: container
name:  "quay.io/biocontainers/perl-libwww-perl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-libwww-perl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-libwww-perl/container.yaml"
updated_at: "2026-01-17 03:32:48.922070"
latest: "6.81--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-libwww-perl"
aliases:
 - "lwp-download"
 - "lwp-dump"
 - "lwp-mirror"
 - "lwp-request"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "6.67--pl5321hdfd78af_0"
 - "6.68--pl5321hdfd78af_0"
 - "6.67--pl5321hdfd78af_1"
 - "6.79--pl5321hdfd78af_0"
 - "6.80--pl5321hdfd78af_0"
 - "6.81--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-libwww-perl"
config: {"url": "https://biocontainers.pro/tools/perl-libwww-perl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-libwww-perl", "latest": {"6.81--pl5321hdfd78af_0": "sha256:e64efc178056e443cc7dd900e51f1e901e44e284fde8893d1d5e6863590b516f"}, "tags": {"6.67--pl5321hdfd78af_0": "sha256:3d1546bab8ebc5f110d74385a7e39728b647c8a922d273a954b3c342d9e4c0f0", "6.68--pl5321hdfd78af_0": "sha256:b09b841c68f4951f813d0f48afdb0b43c220409d472960475a555c4882b00fe2", "6.67--pl5321hdfd78af_1": "sha256:20b1937d6702794ad569df5d30f618ba9f13e12f5242453a0ad7ae90f277011e", "6.79--pl5321hdfd78af_0": "sha256:9dd0fea0734e39a3c8afdc96a4c978b4618bb0385c8cffc717c6b842113b9765", "6.80--pl5321hdfd78af_0": "sha256:a4da5252c372236311715e2883ebe7ac3b24863d0f214445db2a8c9a34771124", "6.81--pl5321hdfd78af_0": "sha256:e64efc178056e443cc7dd900e51f1e901e44e284fde8893d1d5e6863590b516f"}, "docker": "quay.io/biocontainers/perl-libwww-perl", "aliases": {"lwp-download": "/usr/local/bin/lwp-download", "lwp-dump": "/usr/local/bin/lwp-dump", "lwp-mirror": "/usr/local/bin/lwp-mirror", "lwp-request": "/usr/local/bin/lwp-request", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-libwww-perl.
shpc-registry automated BioContainers addition for perl-libwww-perl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-libwww-perl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-libwww-perl:6.81--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-libwww-perl/6.81--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-libwww-perl/6.81--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-libwww-perl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-libwww-perl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-libwww-perl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-libwww-perl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-libwww-perl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-libwww-perl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lwp-download

```bash
$ singularity exec <container> /usr/local/bin/lwp-download
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-dump

```bash
$ singularity exec <container> /usr/local/bin/lwp-dump
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-mirror

```bash
$ singularity exec <container> /usr/local/bin/lwp-mirror
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-mirror   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### lwp-request

```bash
$ singularity exec <container> /usr/local/bin/lwp-request
$ podman run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lwp-request   -v ${PWD} -w ${PWD} <container> -c " $@"
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