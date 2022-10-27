---
layout: container
name:  "quay.io/biocontainers/immuneml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/immuneml/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/immuneml/container.yaml"
updated_at: "2022-10-27 00:53:57.463493"
latest: "2.2.0--py39hbf8eff0_0"
container_url: "https://biocontainers.pro/tools/immuneml"
aliases:
 - "airr-tools"
 - "immune-ml"
 - "immune-ml-quickstart"
 - "pystache"
 - "pystache-test"
versions:
 - "2.2.0--py39hbf8eff0_0"
description: "shpc-registry automated BioContainers addition for immuneml"
config: {"url": "https://biocontainers.pro/tools/immuneml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for immuneml", "latest": {"2.2.0--py39hbf8eff0_0": "sha256:60a6ea6a986487ea863598dc0585e75e337dbe36fb6cef5494d54ae135a3a347"}, "tags": {"2.2.0--py39hbf8eff0_0": "sha256:60a6ea6a986487ea863598dc0585e75e337dbe36fb6cef5494d54ae135a3a347"}, "docker": "quay.io/biocontainers/immuneml", "aliases": {"airr-tools": "/usr/local/bin/airr-tools", "immune-ml": "/usr/local/bin/immune-ml", "immune-ml-quickstart": "/usr/local/bin/immune-ml-quickstart", "pystache": "/usr/local/bin/pystache", "pystache-test": "/usr/local/bin/pystache-test"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/immuneml.
shpc-registry automated BioContainers addition for immuneml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/immuneml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/immuneml:2.2.0--py39hbf8eff0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/immuneml/2.2.0--py39hbf8eff0_0
$ module help quay.io/biocontainers/immuneml/2.2.0--py39hbf8eff0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### immuneml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### immuneml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### immuneml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### immuneml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### immuneml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### immuneml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### airr-tools

```bash
$ singularity exec <container> /usr/local/bin/airr-tools
$ podman run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/airr-tools   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### immune-ml

```bash
$ singularity exec <container> /usr/local/bin/immune-ml
$ podman run --it --rm --entrypoint /usr/local/bin/immune-ml   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/immune-ml   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### immune-ml-quickstart

```bash
$ singularity exec <container> /usr/local/bin/immune-ml-quickstart
$ podman run --it --rm --entrypoint /usr/local/bin/immune-ml-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/immune-ml-quickstart   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pystache

```bash
$ singularity exec <container> /usr/local/bin/pystache
$ podman run --it --rm --entrypoint /usr/local/bin/pystache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pystache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pystache-test

```bash
$ singularity exec <container> /usr/local/bin/pystache-test
$ podman run --it --rm --entrypoint /usr/local/bin/pystache-test   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pystache-test   -v ${PWD} -w ${PWD} <container> -c " $@"
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