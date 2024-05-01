---
layout: container
name:  "quay.io/biocontainers/hapbin"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hapbin/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hapbin/container.yaml"
updated_at: "2024-05-01 02:53:08.936850"
latest: "1.3.0--hdbdd923_5"
container_url: "https://biocontainers.pro/tools/hapbin"
aliases:
 - "ehhbin"
 - "hapbinconv"
 - "xpehhbin"
versions:
 - "1.3.0--h87f3376_3"
 - "1.3.0--h87f3376_4"
 - "1.3.0--hdbdd923_5"
description: "shpc-registry automated BioContainers addition for hapbin"
config: {"url": "https://biocontainers.pro/tools/hapbin", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hapbin", "latest": {"1.3.0--hdbdd923_5": "sha256:9d607ae7106e492a13738dfeb9fe5c70dc78025307285acdd95537be6a6ea080"}, "tags": {"1.3.0--h87f3376_3": "sha256:5460436000502eaad2e74461cfafa4f0339a16a4fadc2e5f479fe2339bc0430d", "1.3.0--h87f3376_4": "sha256:4438711921df3a5bff26c4d28ee0434384591036bd9672c2aa6986cf8d3bf23d", "1.3.0--hdbdd923_5": "sha256:9d607ae7106e492a13738dfeb9fe5c70dc78025307285acdd95537be6a6ea080"}, "docker": "quay.io/biocontainers/hapbin", "aliases": {"ehhbin": "/usr/local/bin/ehhbin", "hapbinconv": "/usr/local/bin/hapbinconv", "xpehhbin": "/usr/local/bin/xpehhbin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hapbin.
shpc-registry automated BioContainers addition for hapbin
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hapbin
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hapbin:1.3.0--hdbdd923_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hapbin/1.3.0--hdbdd923_5
$ module help quay.io/biocontainers/hapbin/1.3.0--hdbdd923_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hapbin-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hapbin-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hapbin-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hapbin-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hapbin-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hapbin-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ehhbin

```bash
$ singularity exec <container> /usr/local/bin/ehhbin
$ podman run --it --rm --entrypoint /usr/local/bin/ehhbin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ehhbin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hapbinconv

```bash
$ singularity exec <container> /usr/local/bin/hapbinconv
$ podman run --it --rm --entrypoint /usr/local/bin/hapbinconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapbinconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xpehhbin

```bash
$ singularity exec <container> /usr/local/bin/xpehhbin
$ podman run --it --rm --entrypoint /usr/local/bin/xpehhbin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xpehhbin   -v ${PWD} -w ${PWD} <container> -c " $@"
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