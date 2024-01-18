---
layout: container
name:  "quay.io/biocontainers/perl-mojo-sqlite"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-mojo-sqlite/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-mojo-sqlite/container.yaml"
updated_at: "2024-01-18 03:05:03.493987"
latest: "3.009--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-mojo-sqlite"
aliases:
 - "hypnotoad"
 - "mojo"
 - "morbo"
 - "config_data"
 - "dbilogstrip"
 - "dbiprof"
 - "dbiproxy"
versions:
 - "3.009--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for perl-mojo-sqlite"
config: {"url": "https://biocontainers.pro/tools/perl-mojo-sqlite", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-mojo-sqlite", "latest": {"3.009--pl5321hdfd78af_0": "sha256:0f05f3b04e45ecebcefd2dc6b2e9f13531d7ebddf1525508ff6153dfdc04f19d"}, "tags": {"3.009--pl5321hdfd78af_0": "sha256:0f05f3b04e45ecebcefd2dc6b2e9f13531d7ebddf1525508ff6153dfdc04f19d"}, "docker": "quay.io/biocontainers/perl-mojo-sqlite", "aliases": {"hypnotoad": "/usr/local/bin/hypnotoad", "mojo": "/usr/local/bin/mojo", "morbo": "/usr/local/bin/morbo", "config_data": "/usr/local/bin/config_data", "dbilogstrip": "/usr/local/bin/dbilogstrip", "dbiprof": "/usr/local/bin/dbiprof", "dbiproxy": "/usr/local/bin/dbiproxy"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-mojo-sqlite.
singularity registry hpc automated addition for perl-mojo-sqlite
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-mojo-sqlite
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-mojo-sqlite:3.009--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-mojo-sqlite/3.009--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-mojo-sqlite/3.009--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-mojo-sqlite-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-mojo-sqlite-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-mojo-sqlite-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-mojo-sqlite-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-mojo-sqlite-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-mojo-sqlite-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hypnotoad

```bash
$ singularity exec <container> /usr/local/bin/hypnotoad
$ podman run --it --rm --entrypoint /usr/local/bin/hypnotoad   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hypnotoad   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mojo

```bash
$ singularity exec <container> /usr/local/bin/mojo
$ podman run --it --rm --entrypoint /usr/local/bin/mojo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mojo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### morbo

```bash
$ singularity exec <container> /usr/local/bin/morbo
$ podman run --it --rm --entrypoint /usr/local/bin/morbo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/morbo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### config_data

```bash
$ singularity exec <container> /usr/local/bin/config_data
$ podman run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/config_data   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbilogstrip

```bash
$ singularity exec <container> /usr/local/bin/dbilogstrip
$ podman run --it --rm --entrypoint /usr/local/bin/dbilogstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbilogstrip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbiprof

```bash
$ singularity exec <container> /usr/local/bin/dbiprof
$ podman run --it --rm --entrypoint /usr/local/bin/dbiprof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbiprof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dbiproxy

```bash
$ singularity exec <container> /usr/local/bin/dbiproxy
$ podman run --it --rm --entrypoint /usr/local/bin/dbiproxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dbiproxy   -v ${PWD} -w ${PWD} <container> -c " $@"
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