---
layout: container
name:  "quay.io/biocontainers/perl-escape-houdini"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-escape-houdini/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-escape-houdini/container.yaml"
updated_at: "2025-02-03 02:49:16.010731"
latest: "0.3.0--pl5321h7b50bb2_4"
container_url: "https://biocontainers.pro/tools/perl-escape-houdini"
aliases:
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.3.0--pl5321hec16e2b_2"
 - "0.3.0--pl5321h031d066_3"
 - "0.3.0--pl5321h7b50bb2_4"
description: "shpc-registry automated BioContainers addition for perl-escape-houdini"
config: {"url": "https://biocontainers.pro/tools/perl-escape-houdini", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-escape-houdini", "latest": {"0.3.0--pl5321h7b50bb2_4": "sha256:23a0c6774267d111445e06e046f35111fbb18c836c6a1501ce0dab3b824f713f"}, "tags": {"0.3.0--pl5321hec16e2b_2": "sha256:9ff4d7e4be358aea91b72b97eb91a9bf14120f136e3ab96882bca8dc1aedd70e", "0.3.0--pl5321h031d066_3": "sha256:e63bfa5f2a2fe0e2832a11e6806eb9f8579b5c25710936782fb0947f0a2b6a5c", "0.3.0--pl5321h7b50bb2_4": "sha256:23a0c6774267d111445e06e046f35111fbb18c836c6a1501ce0dab3b824f713f"}, "docker": "quay.io/biocontainers/perl-escape-houdini", "aliases": {"perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-escape-houdini.
shpc-registry automated BioContainers addition for perl-escape-houdini
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-escape-houdini
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-escape-houdini:0.3.0--pl5321h7b50bb2_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-escape-houdini/0.3.0--pl5321h7b50bb2_4
$ module help quay.io/biocontainers/perl-escape-houdini/0.3.0--pl5321h7b50bb2_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-escape-houdini-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-escape-houdini-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-escape-houdini-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-escape-houdini-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-escape-houdini-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-escape-houdini-inspect-deffile:

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