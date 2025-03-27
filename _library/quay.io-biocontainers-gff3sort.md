---
layout: container
name:  "quay.io/biocontainers/gff3sort"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gff3sort/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gff3sort/container.yaml"
updated_at: "2025-03-27 03:31:35.962530"
latest: "0.1.a1a2bc9--hdfd78af_2"
container_url: "https://biocontainers.pro/tools/gff3sort"
aliases:
 - "check-disorder.pl"
 - "gff3sort.pl"
 - "findrule"
 - "perl5.26.2"
 - "podselect"
versions:
 - "0.1.a1a2bc9--hdfd78af_2"
description: "shpc-registry automated BioContainers addition for gff3sort"
config: {"url": "https://biocontainers.pro/tools/gff3sort", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gff3sort", "latest": {"0.1.a1a2bc9--hdfd78af_2": "sha256:825bb9bc88934ae8fbc95ddff899eda431cade048d4bf3a833c7420e479881a8"}, "tags": {"0.1.a1a2bc9--hdfd78af_2": "sha256:825bb9bc88934ae8fbc95ddff899eda431cade048d4bf3a833c7420e479881a8"}, "docker": "quay.io/biocontainers/gff3sort", "aliases": {"check-disorder.pl": "/usr/local/bin/check-disorder.pl", "gff3sort.pl": "/usr/local/bin/gff3sort.pl", "findrule": "/usr/local/bin/findrule", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gff3sort.
shpc-registry automated BioContainers addition for gff3sort
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gff3sort
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gff3sort:0.1.a1a2bc9--hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gff3sort/0.1.a1a2bc9--hdfd78af_2
$ module help quay.io/biocontainers/gff3sort/0.1.a1a2bc9--hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gff3sort-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gff3sort-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gff3sort-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gff3sort-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gff3sort-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gff3sort-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### check-disorder.pl

```bash
$ singularity exec <container> /usr/local/bin/check-disorder.pl
$ podman run --it --rm --entrypoint /usr/local/bin/check-disorder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/check-disorder.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff3sort.pl

```bash
$ singularity exec <container> /usr/local/bin/gff3sort.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gff3sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff3sort.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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