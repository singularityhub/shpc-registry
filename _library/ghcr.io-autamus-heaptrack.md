---
layout: container
name:  "ghcr.io/autamus/heaptrack"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/heaptrack/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/heaptrack/container.yaml"
updated_at: "2025-01-24 02:46:12.635623"
latest: "1.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/heaptrack"
aliases:
 - "heaptrack"
 - "heaptrack_print"
versions:
 - "1.2.0"
 - "1.3.0"
 - "latest"
description: "Heaptrack traces all memory allocations and annotates these events with stack traces."
config: {"docker": "ghcr.io/autamus/heaptrack", "url": "https://github.com/orgs/autamus/packages/container/package/heaptrack", "maintainer": "@vsoch", "description": "Heaptrack traces all memory allocations and annotates these events with stack traces.", "latest": {"1.3.0": "sha256:74a2ea0fedfcf274054935beea22f863251a5788733433995cb2e7cf6de59610"}, "tags": {"1.2.0": "sha256:f44972b6f31dcc6778f984d097a3e75f034c17a01c27af0c0ef5903cf75960f7", "1.3.0": "sha256:74a2ea0fedfcf274054935beea22f863251a5788733433995cb2e7cf6de59610", "latest": "sha256:74a2ea0fedfcf274054935beea22f863251a5788733433995cb2e7cf6de59610"}, "aliases": {"heaptrack": "/opt/view/bin/heaptrack", "heaptrack_print": "/opt/view/bin/heaptrack_print"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/heaptrack.
Heaptrack traces all memory allocations and annotates these events with stack traces.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/heaptrack
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/heaptrack:1.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/heaptrack/1.3.0
$ module help ghcr.io/autamus/heaptrack/1.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### heaptrack-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### heaptrack-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### heaptrack-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### heaptrack-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### heaptrack-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### heaptrack-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### heaptrack

```bash
$ singularity exec <container> /opt/view/bin/heaptrack
$ podman run --it --rm --entrypoint /opt/view/bin/heaptrack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/heaptrack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### heaptrack_print

```bash
$ singularity exec <container> /opt/view/bin/heaptrack_print
$ podman run --it --rm --entrypoint /opt/view/bin/heaptrack_print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/heaptrack_print   -v ${PWD} -w ${PWD} <container> -c " $@"
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