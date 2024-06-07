---
layout: container
name:  "quay.io/biocontainers/perl-json-validator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-json-validator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-json-validator/container.yaml"
updated_at: "2024-06-07 03:18:21.853609"
latest: "5.14--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-json-validator"
aliases:
 - "hypnotoad"
 - "mojo"
 - "morbo"
 - "yamlpp5-events"
 - "yamlpp5-highlight"
 - "yamlpp5-load"
 - "yamlpp5-load-dump"
 - "yamlpp5-parse-emit"
versions:
 - "5.14--pl5321hdfd78af_0"
description: "singularity registry hpc automated addition for perl-json-validator"
config: {"url": "https://biocontainers.pro/tools/perl-json-validator", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for perl-json-validator", "latest": {"5.14--pl5321hdfd78af_0": "sha256:03484c26bbf6043e02b75a8a711eeca45c34a5da2d1aa82bf5857240eb069ded"}, "tags": {"5.14--pl5321hdfd78af_0": "sha256:03484c26bbf6043e02b75a8a711eeca45c34a5da2d1aa82bf5857240eb069ded"}, "docker": "quay.io/biocontainers/perl-json-validator", "aliases": {"hypnotoad": "/usr/local/bin/hypnotoad", "mojo": "/usr/local/bin/mojo", "morbo": "/usr/local/bin/morbo", "yamlpp5-events": "/usr/local/bin/yamlpp5-events", "yamlpp5-highlight": "/usr/local/bin/yamlpp5-highlight", "yamlpp5-load": "/usr/local/bin/yamlpp5-load", "yamlpp5-load-dump": "/usr/local/bin/yamlpp5-load-dump", "yamlpp5-parse-emit": "/usr/local/bin/yamlpp5-parse-emit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-json-validator.
singularity registry hpc automated addition for perl-json-validator
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-json-validator
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-json-validator:5.14--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-json-validator/5.14--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-json-validator/5.14--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-json-validator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-validator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-json-validator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-json-validator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-json-validator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-json-validator-inspect-deffile:

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


#### yamlpp5-events

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-events
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-highlight

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-highlight
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-highlight   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-highlight   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-load

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-load
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-load   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-load   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-load-dump

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-load-dump
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-load-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-load-dump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yamlpp5-parse-emit

```bash
$ singularity exec <container> /usr/local/bin/yamlpp5-parse-emit
$ podman run --it --rm --entrypoint /usr/local/bin/yamlpp5-parse-emit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yamlpp5-parse-emit   -v ${PWD} -w ${PWD} <container> -c " $@"
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