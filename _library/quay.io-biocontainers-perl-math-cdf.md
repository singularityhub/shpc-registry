---
layout: container
name:  "quay.io/biocontainers/perl-math-cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-math-cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-math-cdf/container.yaml"
updated_at: "2025-04-16 03:24:36.629495"
latest: "0.1--pl5321h7b50bb2_11"
container_url: "https://biocontainers.pro/tools/perl-math-cdf"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.1--pl5321hec16e2b_7"
 - "0.1--pl5321h031d066_9"
 - "0.1--pl5321h031d066_10"
 - "0.1--pl5321h7b50bb2_11"
description: "shpc-registry automated BioContainers addition for perl-math-cdf"
config: {"url": "https://biocontainers.pro/tools/perl-math-cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-math-cdf", "latest": {"0.1--pl5321h7b50bb2_11": "sha256:747608ec240c582fe12d2805bc16a60a5233a0829b3140982b078cc93a370bc2"}, "tags": {"0.1--pl5321hec16e2b_7": "sha256:73511372b587115f61bf317f1716bf4ff3377cc0c5c3b2db3e4f3a261b29d864", "0.1--pl5321h031d066_9": "sha256:1b30cb1ed25cffb85deb62bbd323fa1ec82b390c32a17ede0b8f7e1e4419fada", "0.1--pl5321h031d066_10": "sha256:e513f0172026b7851b4d9d5c94ef052b3b8ff8935bd6dc2e4613f248ffdb3e3e", "0.1--pl5321h7b50bb2_11": "sha256:747608ec240c582fe12d2805bc16a60a5233a0829b3140982b078cc93a370bc2"}, "docker": "quay.io/biocontainers/perl-math-cdf", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-math-cdf.
shpc-registry automated BioContainers addition for perl-math-cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-math-cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-math-cdf:0.1--pl5321h7b50bb2_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-math-cdf/0.1--pl5321h7b50bb2_11
$ module help quay.io/biocontainers/perl-math-cdf/0.1--pl5321h7b50bb2_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-math-cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-math-cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-math-cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-math-cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-math-cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-math-cdf-inspect-deffile:

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