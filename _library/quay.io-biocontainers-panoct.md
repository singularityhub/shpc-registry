---
layout: container
name:  "quay.io/biocontainers/panoct"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/panoct/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/panoct/container.yaml"
updated_at: "2023-01-27 03:32:21.363240"
latest: "3.23--pl526_1"
container_url: "https://biocontainers.pro/tools/panoct"
aliases:
 - "gene_order.pl"
 - "panoct.pl"
 - "paralog_matchtable.pl"
 - "perl5.26.2"
 - "podselect"
versions:
 - "3.23--pl526_1"
description: "shpc-registry automated BioContainers addition for panoct"
config: {"url": "https://biocontainers.pro/tools/panoct", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for panoct", "latest": {"3.23--pl526_1": "sha256:5e69b3242f2ee4ef28d1ae3ea3e437e3a9e0ff392ecc4f2388cb161e96073803"}, "tags": {"3.23--pl526_1": "sha256:5e69b3242f2ee4ef28d1ae3ea3e437e3a9e0ff392ecc4f2388cb161e96073803"}, "docker": "quay.io/biocontainers/panoct", "aliases": {"gene_order.pl": "/usr/local/bin/gene_order.pl", "panoct.pl": "/usr/local/bin/panoct.pl", "paralog_matchtable.pl": "/usr/local/bin/paralog_matchtable.pl", "perl5.26.2": "/usr/local/bin/perl5.26.2", "podselect": "/usr/local/bin/podselect"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/panoct.
shpc-registry automated BioContainers addition for panoct
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/panoct
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/panoct:3.23--pl526_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/panoct/3.23--pl526_1
$ module help quay.io/biocontainers/panoct/3.23--pl526_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### panoct-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### panoct-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### panoct-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### panoct-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### panoct-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### panoct-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gene_order.pl

```bash
$ singularity exec <container> /usr/local/bin/gene_order.pl
$ podman run --it --rm --entrypoint /usr/local/bin/gene_order.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gene_order.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### panoct.pl

```bash
$ singularity exec <container> /usr/local/bin/panoct.pl
$ podman run --it --rm --entrypoint /usr/local/bin/panoct.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/panoct.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### paralog_matchtable.pl

```bash
$ singularity exec <container> /usr/local/bin/paralog_matchtable.pl
$ podman run --it --rm --entrypoint /usr/local/bin/paralog_matchtable.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/paralog_matchtable.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.26.2

```bash
$ singularity exec <container> /usr/local/bin/perl5.26.2
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.26.2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### podselect

```bash
$ singularity exec <container> /usr/local/bin/podselect
$ podman run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/podselect   -v ${PWD} -w ${PWD} <container> -c " $@"
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