---
layout: container
name:  "quay.io/biocontainers/asn2gb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/asn2gb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/asn2gb/container.yaml"
updated_at: "2025-08-14 04:04:40.215788"
latest: "18.2--h9ee0642_3"
container_url: "https://biocontainers.pro/tools/asn2gb"
aliases:
 - "asn2gb"
 - "idn"
versions:
 - "18.2--h9ee0642_3"
description: "shpc-registry automated BioContainers addition for asn2gb"
config: {"url": "https://biocontainers.pro/tools/asn2gb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for asn2gb", "latest": {"18.2--h9ee0642_3": "sha256:7a3836210bc32927642f0862f060cde4edb7aad26651b236e914753ba10ac663"}, "tags": {"18.2--h9ee0642_3": "sha256:7a3836210bc32927642f0862f060cde4edb7aad26651b236e914753ba10ac663"}, "docker": "quay.io/biocontainers/asn2gb", "aliases": {"asn2gb": "/usr/local/bin/asn2gb", "idn": "/usr/local/bin/idn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/asn2gb.
shpc-registry automated BioContainers addition for asn2gb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/asn2gb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/asn2gb:18.2--h9ee0642_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/asn2gb/18.2--h9ee0642_3
$ module help quay.io/biocontainers/asn2gb/18.2--h9ee0642_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### asn2gb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### asn2gb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### asn2gb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### asn2gb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### asn2gb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### asn2gb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### asn2gb

```bash
$ singularity exec <container> /usr/local/bin/asn2gb
$ podman run --it --rm --entrypoint /usr/local/bin/asn2gb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn2gb   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idn

```bash
$ singularity exec <container> /usr/local/bin/idn
$ podman run --it --rm --entrypoint /usr/local/bin/idn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idn   -v ${PWD} -w ${PWD} <container> -c " $@"
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