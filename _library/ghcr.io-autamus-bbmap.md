---
layout: container
name:  "ghcr.io/autamus/bbmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/bbmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/bbmap/container.yaml"
updated_at: "2023-11-13 03:33:38.888312"
latest: "38.63"
container_url: "https://github.com/orgs/autamus/packages/container/package/bbmap"

versions:
 - "38.63"
 - "latest"
description: "A suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data."
config: {"docker": "ghcr.io/autamus/bbmap", "url": "https://github.com/orgs/autamus/packages/container/package/bbmap", "maintainer": "@vsoch", "description": "A suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data.", "latest": {"38.63": "sha256:0566ca00109ab3061d444bca490dba55a7cf2052124b39418d3b9ae6ebb4e1aa"}, "tags": {"38.63": "sha256:0566ca00109ab3061d444bca490dba55a7cf2052124b39418d3b9ae6ebb4e1aa", "latest": "sha256:0566ca00109ab3061d444bca490dba55a7cf2052124b39418d3b9ae6ebb4e1aa"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/bbmap.
A suite of fast, multithreaded bioinformatics tools designed for analysis of DNA and RNA sequence data.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/bbmap
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/bbmap:38.63
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/bbmap/38.63
$ module help ghcr.io/autamus/bbmap/38.63
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bbmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bbmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bbmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bbmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bbmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bbmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bbmap

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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