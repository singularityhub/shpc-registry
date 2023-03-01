---
layout: container
name:  "quay.io/biocontainers/perl-extutils-makemaker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-extutils-makemaker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-extutils-makemaker/container.yaml"
updated_at: "2023-03-01 03:44:20.697673"
latest: "7.36--pl526_1"
container_url: "https://biocontainers.pro/tools/perl-extutils-makemaker"
aliases:
 - "perl5.26.2"
 - "podselect"
versions:
 - "7.36--pl526_1"
description: "shpc-registry automated BioContainers addition for perl-extutils-makemaker"
config: {"url": "https://biocontainers.pro/tools/perl-extutils-makemaker", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-extutils-makemaker", "latest": {"7.36--pl526_1": "sha256:ae43774d344d3a58dd1b4b2e66b66a87db95ebb0e330e0a00b1d92e5c6a57059"}, "tags": {"7.36--pl526_1": "sha256:ae43774d344d3a58dd1b4b2e66b66a87db95ebb0e330e0a00b1d92e5c6a57059"}, "docker": "quay.io/biocontainers/perl-extutils-makemaker", "aliases": {"perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-extutils-makemaker.
shpc-registry automated BioContainers addition for perl-extutils-makemaker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-extutils-makemaker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-extutils-makemaker:7.36--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-extutils-makemaker/7.36--pl526_1
$ module help quay.io/biocontainers/perl-extutils-makemaker/7.36--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-extutils-makemaker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-extutils-makemaker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-extutils-makemaker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-extutils-makemaker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-extutils-makemaker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-extutils-makemaker-inspect-deffile:

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