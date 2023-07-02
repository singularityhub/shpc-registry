---
layout: container
name:  "quay.io/biocontainers/perl-email-simple"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-email-simple/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-email-simple/container.yaml"
updated_at: "2023-07-02 03:28:30.529149"
latest: "2.218--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-email-simple"
aliases:
 - "perl5.26.2"
 - "podselect"
versions:
 - "2.216--hdfd78af_1"
 - "2.218--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-email-simple"
config: {"url": "https://biocontainers.pro/tools/perl-email-simple", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-email-simple", "latest": {"2.218--hdfd78af_0": "sha256:e705063e6076e8b260d8fec1c1e0e6a4aac19f0c3c6279af3ac7fdc036afb539"}, "tags": {"2.216--hdfd78af_1": "sha256:d9caada984725df743642ef97e1e83af1ecfe8ff1624dffe916d50e71eee072d", "2.218--hdfd78af_0": "sha256:e705063e6076e8b260d8fec1c1e0e6a4aac19f0c3c6279af3ac7fdc036afb539"}, "docker": "quay.io/biocontainers/perl-email-simple", "aliases": {"perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-email-simple.
shpc-registry automated BioContainers addition for perl-email-simple
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-email-simple
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-email-simple:2.218--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-email-simple/2.218--hdfd78af_0
$ module help quay.io/biocontainers/perl-email-simple/2.218--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-email-simple-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-email-simple-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-email-simple-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-email-simple-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-email-simple-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-email-simple-inspect-deffile:

```bash
$ singularity inspect -d <container>
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