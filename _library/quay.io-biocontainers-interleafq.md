---
layout: container
name:  "quay.io/biocontainers/interleafq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/interleafq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/interleafq/container.yaml"
updated_at: "2024-10-20 03:21:12.862981"
latest: "1.1.0--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/interleafq"
aliases:
 - "fqc"
 - "fqlen.pl"
 - "interleafq"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.1.0--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for interleafq"
config: {"url": "https://biocontainers.pro/tools/interleafq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for interleafq", "latest": {"1.1.0--pl5321hdfd78af_2": "sha256:55258613a4d7d476fb6f654e3858acb54099519ae7a15ab5505f3194f6daab01"}, "tags": {"1.1.0--pl5321hdfd78af_2": "sha256:55258613a4d7d476fb6f654e3858acb54099519ae7a15ab5505f3194f6daab01"}, "docker": "quay.io/biocontainers/interleafq", "aliases": {"fqc": "/usr/local/bin/fqc", "fqlen.pl": "/usr/local/bin/fqlen.pl", "interleafq": "/usr/local/bin/interleafq", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/interleafq.
shpc-registry automated BioContainers addition for interleafq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/interleafq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/interleafq:1.1.0--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/interleafq/1.1.0--pl5321hdfd78af_2
$ module help quay.io/biocontainers/interleafq/1.1.0--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### interleafq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### interleafq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### interleafq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### interleafq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### interleafq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### interleafq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fqc

```bash
$ singularity exec <container> /usr/local/bin/fqc
$ podman run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fqlen.pl

```bash
$ singularity exec <container> /usr/local/bin/fqlen.pl
$ podman run --it --rm --entrypoint /usr/local/bin/fqlen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fqlen.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### interleafq

```bash
$ singularity exec <container> /usr/local/bin/interleafq
$ podman run --it --rm --entrypoint /usr/local/bin/interleafq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/interleafq   -v ${PWD} -w ${PWD} <container> -c " $@"
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