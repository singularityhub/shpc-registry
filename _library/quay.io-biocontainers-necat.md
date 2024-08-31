---
layout: container
name:  "quay.io/biocontainers/necat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/necat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/necat/container.yaml"
updated_at: "2024-08-31 03:28:34.478910"
latest: "0.0.1_update20200803--h43eeafb_5"
container_url: "https://biocontainers.pro/tools/necat"
aliases:
 - "necat"
 - "perl5.32.1"
 - "streamzip"
versions:
 - "0.0.1_update20200803--h5b5514e_2"
 - "0.0.1_update20200803--h43eeafb_4"
 - "0.0.1_update20200803--h43eeafb_5"
description: "shpc-registry automated BioContainers addition for necat"
config: {"url": "https://biocontainers.pro/tools/necat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for necat", "latest": {"0.0.1_update20200803--h43eeafb_5": "sha256:9ba8bee26ec4030af8bb4ef5639eae7bc0c8d9907dd9dca6c0fe0ab21a321cb5"}, "tags": {"0.0.1_update20200803--h5b5514e_2": "sha256:51a36bc071bd80444be836df03044d9fd09dfd3b78d59591487f5e873da9589a", "0.0.1_update20200803--h43eeafb_4": "sha256:30de3800a764847f55952a0398d88f13612b1d1f7d3fdf539b7d74c8debf7a27", "0.0.1_update20200803--h43eeafb_5": "sha256:9ba8bee26ec4030af8bb4ef5639eae7bc0c8d9907dd9dca6c0fe0ab21a321cb5"}, "docker": "quay.io/biocontainers/necat", "aliases": {"necat": "/usr/local/bin/necat", "perl5.32.1": "/usr/local/bin/perl5.32.1", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/necat.
shpc-registry automated BioContainers addition for necat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/necat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/necat:0.0.1_update20200803--h43eeafb_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/necat/0.0.1_update20200803--h43eeafb_5
$ module help quay.io/biocontainers/necat/0.0.1_update20200803--h43eeafb_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### necat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### necat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### necat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### necat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### necat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### necat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### necat

```bash
$ singularity exec <container> /usr/local/bin/necat
$ podman run --it --rm --entrypoint /usr/local/bin/necat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/necat   -v ${PWD} -w ${PWD} <container> -c " $@"
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