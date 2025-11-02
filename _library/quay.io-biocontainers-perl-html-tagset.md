---
layout: container
name:  "quay.io/biocontainers/perl-html-tagset"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-html-tagset/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-html-tagset/container.yaml"
updated_at: "2025-11-02 03:42:25.204286"
latest: "3.24--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-html-tagset"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "3.20--pl5321hdfd78af_4"
 - "3.24--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-html-tagset"
config: {"url": "https://biocontainers.pro/tools/perl-html-tagset", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-html-tagset", "latest": {"3.24--pl5321hdfd78af_0": "sha256:a874f286d4d7134a9f7c0570f9c1d5c6c72a7f2e13cddcbd2aa65e92d4f3a3cf"}, "tags": {"3.20--pl5321hdfd78af_4": "sha256:f943b2142c6b460a8ccbd087d263a34a203aee4542ac637950247f5d476d70b0", "3.24--pl5321hdfd78af_0": "sha256:a874f286d4d7134a9f7c0570f9c1d5c6c72a7f2e13cddcbd2aa65e92d4f3a3cf"}, "docker": "quay.io/biocontainers/perl-html-tagset", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-html-tagset.
shpc-registry automated BioContainers addition for perl-html-tagset
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-html-tagset
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-html-tagset:3.24--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-html-tagset/3.24--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-html-tagset/3.24--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-html-tagset-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-tagset-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-html-tagset-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-html-tagset-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-html-tagset-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-html-tagset-inspect-deffile:

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