---
layout: container
name:  "quay.io/biocontainers/perl-yaml-pp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-yaml-pp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-yaml-pp/container.yaml"
updated_at: "2025-12-11 04:43:57.261562"
latest: "0.39.0--pl5321hdfd78af_0"
container_url: "https://biocontainers.pro/tools/perl-yaml-pp"
aliases:
 - "yamlpp5-events"
 - "yamlpp5-highlight"
 - "yamlpp5-load"
 - "yamlpp5-load-dump"
 - "yamlpp5-parse-emit"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.021--pl5321hdfd78af_2"
 - "0.39.0--pl5321hdfd78af_0"
description: "shpc-registry automated BioContainers addition for perl-yaml-pp"
config: {"url": "https://biocontainers.pro/tools/perl-yaml-pp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-yaml-pp", "latest": {"0.39.0--pl5321hdfd78af_0": "sha256:bdf746405035032313134630ef469f600e55006da2576d8fe1f77068643b087e"}, "tags": {"0.021--pl5321hdfd78af_2": "sha256:1feaca22e6431d84bb2948c953acf939a6a88e1490b8d7c0395a0eff904bf6a3", "0.39.0--pl5321hdfd78af_0": "sha256:bdf746405035032313134630ef469f600e55006da2576d8fe1f77068643b087e"}, "docker": "quay.io/biocontainers/perl-yaml-pp", "aliases": {"yamlpp5-events": "/usr/local/bin/yamlpp5-events", "yamlpp5-highlight": "/usr/local/bin/yamlpp5-highlight", "yamlpp5-load": "/usr/local/bin/yamlpp5-load", "yamlpp5-load-dump": "/usr/local/bin/yamlpp5-load-dump", "yamlpp5-parse-emit": "/usr/local/bin/yamlpp5-parse-emit", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-yaml-pp.
shpc-registry automated BioContainers addition for perl-yaml-pp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-yaml-pp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-yaml-pp:0.39.0--pl5321hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-yaml-pp/0.39.0--pl5321hdfd78af_0
$ module help quay.io/biocontainers/perl-yaml-pp/0.39.0--pl5321hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-yaml-pp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-yaml-pp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-yaml-pp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-yaml-pp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-yaml-pp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-yaml-pp-inspect-deffile:

```bash
$ singularity inspect -d <container>
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