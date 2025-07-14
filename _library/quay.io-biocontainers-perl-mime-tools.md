---
layout: container
name:  "quay.io/biocontainers/perl-mime-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-mime-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-mime-tools/container.yaml"
updated_at: "2025-07-14 03:58:32.431744"
latest: "5.515--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-mime-tools"
aliases:
 - "binhex.pl"
 - "debinhex.pl"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "5.508--pl5321hdfd78af_2"
 - "5.515--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-mime-tools"
config: {"url": "https://biocontainers.pro/tools/perl-mime-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-mime-tools", "latest": {"5.515--pl5321hdfd78af_0": "sha256:21659b3ad2ac2443061eadcde37b1cb1233b475bc9c6cec39bb9896aa4f5b24c"}, "tags": {"5.508--pl5321hdfd78af_2": "sha256:8072aa4bbc6aa2a86036d8bdd4b0c74d5f2e765a7a2a2bfb35d3da8ba9b0c021", "5.515--pl5321hdfd78af_0": "sha256:21659b3ad2ac2443061eadcde37b1cb1233b475bc9c6cec39bb9896aa4f5b24c"}, "docker": "quay.io/biocontainers/perl-mime-tools", "aliases": {"binhex.pl": "/usr/local/bin/binhex.pl", "debinhex.pl": "/usr/local/bin/debinhex.pl", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-mime-tools.
shpc-registry automated BioContainers addition for perl-mime-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-mime-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-mime-tools:5.515--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-mime-tools/5.515--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-mime-tools/5.515--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-mime-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-mime-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-mime-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-mime-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-mime-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-mime-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### binhex.pl

```bash
$ singularity exec <container> /usr/local/bin/binhex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/binhex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/binhex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### debinhex.pl

```bash
$ singularity exec <container> /usr/local/bin/debinhex.pl
$ podman run --it --rm --entrypoint /usr/local/bin/debinhex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/debinhex.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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