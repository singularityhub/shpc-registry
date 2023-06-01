---
layout: container
name:  "quay.io/biocontainers/perl-biox-seq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-biox-seq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-biox-seq/container.yaml"
updated_at: "2023-06-01 03:36:11.885880"
latest: "0.008007--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-biox-seq"
aliases:
 - "bgzip.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.008006--pl5321hdfd78af_0"
 - "0.008007--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-biox-seq"
config: {"url": "https://biocontainers.pro/tools/perl-biox-seq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-biox-seq", "latest": {"0.008007--pl5321hdfd78af_0": "sha256:d52f66c1b61dad5ced4b3378c5e635578dd33a24bb85c60c6b97633eab226134"}, "tags": {"0.008006--pl5321hdfd78af_0": "sha256:194e6f0a79c5866e95f89733756fbb49865cce50661e728cd6b785114e1134b2", "0.008007--pl5321hdfd78af_0": "sha256:d52f66c1b61dad5ced4b3378c5e635578dd33a24bb85c60c6b97633eab226134"}, "docker": "quay.io/biocontainers/perl-biox-seq", "aliases": {"bgzip.pl": "/usr/local/bin/bgzip.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-biox-seq.
shpc-registry automated BioContainers addition for perl-biox-seq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-biox-seq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-biox-seq:0.008007--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-biox-seq/0.008007--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-biox-seq/0.008007--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-biox-seq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-biox-seq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-biox-seq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-biox-seq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-biox-seq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-biox-seq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bgzip.pl

```bash
$ singularity exec <container> /usr/local/bin/bgzip.pl
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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