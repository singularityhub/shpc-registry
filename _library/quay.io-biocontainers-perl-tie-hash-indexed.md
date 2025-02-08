---
layout: container
name:  "quay.io/biocontainers/perl-tie-hash-indexed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-tie-hash-indexed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-tie-hash-indexed/container.yaml"
updated_at: "2025-02-08 03:13:04.217058"
latest: "0.08--pl5321h7b50bb2_4"
container_url: "https://biocontainers.pro/tools/perl-tie-hash-indexed"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.08--pl5321hec16e2b_1"
 - "0.08--pl5321h031d066_3"
 - "0.08--pl5321h7b50bb2_4"
description: "shpc-registry automated BioContainers addition for perl-tie-hash-indexed"
config: {"url": "https://biocontainers.pro/tools/perl-tie-hash-indexed", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-tie-hash-indexed", "latest": {"0.08--pl5321h7b50bb2_4": "sha256:d1c3d564c5981abf7f422f7e95b4e8918b8caad9e4063e2cc6d01c9c369066c5"}, "tags": {"0.08--pl5321hec16e2b_1": "sha256:e3161fc1de4906bd89f32bcdf6e83d4af41174a7649ca79ae10174de1019b242", "0.08--pl5321h031d066_3": "sha256:ee8b5c3742f0ba51865927fcb66e3dc4754b7428fcf326618dcd84c2efc36c87", "0.08--pl5321h7b50bb2_4": "sha256:d1c3d564c5981abf7f422f7e95b4e8918b8caad9e4063e2cc6d01c9c369066c5"}, "docker": "quay.io/biocontainers/perl-tie-hash-indexed", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-tie-hash-indexed.
shpc-registry automated BioContainers addition for perl-tie-hash-indexed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-tie-hash-indexed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-tie-hash-indexed:0.08--pl5321h7b50bb2_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-tie-hash-indexed/0.08--pl5321h7b50bb2_4
$ module help quay.io/biocontainers/perl-tie-hash-indexed/0.08--pl5321h7b50bb2_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-tie-hash-indexed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-tie-hash-indexed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-tie-hash-indexed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-tie-hash-indexed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-tie-hash-indexed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-tie-hash-indexed-inspect-deffile:

```bash
$ singularity inspect -d <container>
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