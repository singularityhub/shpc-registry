---
layout: container
name:  "quay.io/biocontainers/perl-compress-bgzf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-compress-bgzf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-compress-bgzf/container.yaml"
updated_at: "2025-01-17 03:09:25.901960"
latest: "0.005--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-compress-bgzf"
aliases:
 - "bgzip.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.005--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-compress-bgzf"
config: {"url": "https://biocontainers.pro/tools/perl-compress-bgzf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-compress-bgzf", "latest": {"0.005--pl5321hdfd78af_1": "sha256:2754dc1f40bdbbfccfab5c18b68108b35db3e0faefbeed3932ef417135384a43"}, "tags": {"0.005--pl5321hdfd78af_1": "sha256:2754dc1f40bdbbfccfab5c18b68108b35db3e0faefbeed3932ef417135384a43"}, "docker": "quay.io/biocontainers/perl-compress-bgzf", "aliases": {"bgzip.pl": "/usr/local/bin/bgzip.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-compress-bgzf.
shpc-registry automated BioContainers addition for perl-compress-bgzf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-compress-bgzf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-compress-bgzf:0.005--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-compress-bgzf/0.005--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-compress-bgzf/0.005--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-compress-bgzf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-compress-bgzf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-compress-bgzf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-compress-bgzf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-compress-bgzf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-compress-bgzf-inspect-deffile:

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