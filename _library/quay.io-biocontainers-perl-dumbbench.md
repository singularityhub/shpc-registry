---
layout: container
name:  "quay.io/biocontainers/perl-dumbbench"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-dumbbench/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-dumbbench/container.yaml"
updated_at: "2024-10-17 03:32:32.416499"
latest: "0.111--pl5321hdfd78af_1"
container_url: "https://biocontainers.pro/tools/perl-dumbbench"
aliases:
 - "dumbbench"
 - "use-devel-assertos"
 - "findrule"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.111--pl5321hdfd78af_1"
description: "shpc-registry automated BioContainers addition for perl-dumbbench"
config: {"url": "https://biocontainers.pro/tools/perl-dumbbench", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-dumbbench", "latest": {"0.111--pl5321hdfd78af_1": "sha256:3b02f7474f6b72758df31860281c17dd5c6a1400e2d4d575dcba89619a565316"}, "tags": {"0.111--pl5321hdfd78af_1": "sha256:3b02f7474f6b72758df31860281c17dd5c6a1400e2d4d575dcba89619a565316"}, "docker": "quay.io/biocontainers/perl-dumbbench", "aliases": {"dumbbench": "/usr/local/bin/dumbbench", "use-devel-assertos": "/usr/local/bin/use-devel-assertos", "findrule": "/usr/local/bin/findrule", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-dumbbench.
shpc-registry automated BioContainers addition for perl-dumbbench
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-dumbbench
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-dumbbench:0.111--pl5321hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-dumbbench/0.111--pl5321hdfd78af_1
$ module help quay.io/biocontainers/perl-dumbbench/0.111--pl5321hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-dumbbench-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-dumbbench-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-dumbbench-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-dumbbench-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-dumbbench-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-dumbbench-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dumbbench

```bash
$ singularity exec <container> /usr/local/bin/dumbbench
$ podman run --it --rm --entrypoint /usr/local/bin/dumbbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dumbbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### use-devel-assertos

```bash
$ singularity exec <container> /usr/local/bin/use-devel-assertos
$ podman run --it --rm --entrypoint /usr/local/bin/use-devel-assertos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/use-devel-assertos   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### findrule

```bash
$ singularity exec <container> /usr/local/bin/findrule
$ podman run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/findrule   -v ${PWD} -w ${PWD} <container> -c " $@"
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