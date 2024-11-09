---
layout: container
name:  "quay.io/biocontainers/perl-algorithm-cluster"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-algorithm-cluster/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-algorithm-cluster/container.yaml"
updated_at: "2024-11-09 03:32:05.877373"
latest: "1.59--pl5321h031d066_4"
container_url: "https://biocontainers.pro/tools/perl-algorithm-cluster"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "1.59--pl5321hec16e2b_1"
 - "1.59--pl5321h031d066_3"
 - "1.59--pl5321h031d066_4"
description: "shpc-registry automated BioContainers addition for perl-algorithm-cluster"
config: {"url": "https://biocontainers.pro/tools/perl-algorithm-cluster", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-algorithm-cluster", "latest": {"1.59--pl5321h031d066_4": "sha256:783cf26b79c91395eca2cdaad57b21ad37df1252ea76c2941d23ebee542c6170"}, "tags": {"1.59--pl5321hec16e2b_1": "sha256:2ca0fda843e189719d3231ae9cfb5e3e96a0ce6d32f328a31c66bdc217a57869", "1.59--pl5321h031d066_3": "sha256:f6fb854f3d13a2ea2543fd41ad5c89c072bf14192018eb48662ec8e12a439b4b", "1.59--pl5321h031d066_4": "sha256:783cf26b79c91395eca2cdaad57b21ad37df1252ea76c2941d23ebee542c6170"}, "docker": "quay.io/biocontainers/perl-algorithm-cluster", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-algorithm-cluster.
shpc-registry automated BioContainers addition for perl-algorithm-cluster
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-algorithm-cluster
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-algorithm-cluster:1.59--pl5321h031d066_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-algorithm-cluster/1.59--pl5321h031d066_4
$ module help quay.io/biocontainers/perl-algorithm-cluster/1.59--pl5321h031d066_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-algorithm-cluster-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-algorithm-cluster-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-algorithm-cluster-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-algorithm-cluster-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-algorithm-cluster-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-algorithm-cluster-inspect-deffile:

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