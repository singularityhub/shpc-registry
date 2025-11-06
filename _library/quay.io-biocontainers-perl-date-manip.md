---
layout: container
name:  "quay.io/biocontainers/perl-date-manip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-date-manip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-date-manip/container.yaml"
updated_at: "2025-11-06 04:07:01.082773"
latest: "6.98--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-date-manip"
aliases:
 - "dm_date"
 - "dm_zdump"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "6.88--pl5321hdfd78af_0"
 - "6.98--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-date-manip"
config: {"url": "https://biocontainers.pro/tools/perl-date-manip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-date-manip", "latest": {"6.98--pl5321hdfd78af_0": "sha256:f372da06249dc22b6a1ff8776ad7bd70e0f9184207ef27d891660b488f3076dd"}, "tags": {"6.88--pl5321hdfd78af_0": "sha256:40d5912a2e28cd49e7400f1c77f201b0a479b0636e53929f20c2c1ff36b4d260", "6.98--pl5321hdfd78af_0": "sha256:f372da06249dc22b6a1ff8776ad7bd70e0f9184207ef27d891660b488f3076dd"}, "docker": "quay.io/biocontainers/perl-date-manip", "aliases": {"dm_date": "/usr/local/bin/dm_date", "dm_zdump": "/usr/local/bin/dm_zdump", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-date-manip.
shpc-registry automated BioContainers addition for perl-date-manip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-date-manip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-date-manip:6.98--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-date-manip/6.98--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-date-manip/6.98--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-date-manip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-date-manip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-date-manip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-date-manip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-date-manip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-date-manip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dm_date

```bash
$ singularity exec <container> /usr/local/bin/dm_date
$ podman run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_date   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dm_zdump

```bash
$ singularity exec <container> /usr/local/bin/dm_zdump
$ podman run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dm_zdump   -v ${PWD} -w ${PWD} <container> -c " $@"
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