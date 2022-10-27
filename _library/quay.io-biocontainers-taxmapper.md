---
layout: container
name:  "quay.io/biocontainers/taxmapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/taxmapper/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/taxmapper/container.yaml"
updated_at: "2022-10-27 01:13:11.521166"
latest: "1.0.2--py_3"
container_url: "https://biocontainers.pro/tools/taxmapper"
aliases:
 - "ddls"
 - "taxmapper"
versions:
 - "1.0.2--py_3"
description: "shpc-registry automated BioContainers addition for taxmapper"
config: {"url": "https://biocontainers.pro/tools/taxmapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for taxmapper", "latest": {"1.0.2--py_3": "sha256:080f59425c21689eba6561f7ac7602b0950d75eca67b8f8da268e033da281eee"}, "tags": {"1.0.2--py_3": "sha256:080f59425c21689eba6561f7ac7602b0950d75eca67b8f8da268e033da281eee"}, "docker": "quay.io/biocontainers/taxmapper", "aliases": {"ddls": "/usr/local/bin/ddls", "taxmapper": "/usr/local/bin/taxmapper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/taxmapper.
shpc-registry automated BioContainers addition for taxmapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/taxmapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/taxmapper:1.0.2--py_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/taxmapper/1.0.2--py_3
$ module help quay.io/biocontainers/taxmapper/1.0.2--py_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### taxmapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### taxmapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### taxmapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### taxmapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### taxmapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### taxmapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ddls

```bash
$ singularity exec <container> /usr/local/bin/ddls
$ podman run --it --rm --entrypoint /usr/local/bin/ddls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ddls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### taxmapper

```bash
$ singularity exec <container> /usr/local/bin/taxmapper
$ podman run --it --rm --entrypoint /usr/local/bin/taxmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/taxmapper   -v ${PWD} -w ${PWD} <container> -c " $@"
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