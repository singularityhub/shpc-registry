---
layout: container
name:  "julia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/julia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/julia/container.yaml"
updated_at: "2025-12-04 04:16:16.769771"
latest: "1.12.1"
container_url: "https://hub.docker.com/_/julia"
aliases:
 - "julia"
versions:
 - "1.8.3"
 - "1.8.5"
 - "1.9.0"
 - "1.9.1"
 - "1.9.2"
 - "1.9.3"
 - "1.9.4"
 - "1.10.0"
 - "1.10.1"
 - "1.10.2"
 - "1.10.3"
 - "1.10.4"
 - "1.10.5"
 - "1.11.1"
 - "1.10.6"
 - "1.11.2"
 - "1.10.7"
 - "1.11.3"
 - "1.10.8"
 - "1.11.4"
 - "1.10.9"
 - "1.11.5"
 - "1.11.6"
 - "1.10.10"
 - "1.11.7"
 - "1.12.1"
description: "An interpreted, high-level, high-performance dynamic programming language for technical computing."
config: {"docker": "julia", "url": "https://hub.docker.com/_/julia", "maintainer": "@marcodelapierre", "description": "An interpreted, high-level, high-performance dynamic programming language for technical computing.", "latest": {"1.12.1": "crane digest julia:1.12.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"1.8.3": "crane digest julia:1.8.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.8.5": "crane digest julia:1.8.5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.9.0": "crane digest julia:1.9.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.9.1": "crane digest julia:1.9.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.9.2": "crane digest julia:1.9.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.9.3": "crane digest julia:1.9.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.9.4": "crane digest julia:1.9.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.0": "crane digest julia:1.10.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.1": "crane digest julia:1.10.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.2": "crane digest julia:1.10.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.3": "crane digest julia:1.10.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.4": "crane digest julia:1.10.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.5": "crane digest julia:1.10.5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.11.1": "crane digest julia:1.11.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.6": "crane digest julia:1.10.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.11.2": "crane digest julia:1.11.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.7": "crane digest julia:1.10.7: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.11.3": "crane digest julia:1.11.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.8": "crane digest julia:1.10.8: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.11.4": "crane digest julia:1.11.4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.9": "crane digest julia:1.10.9: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.11.5": "crane digest julia:1.11.5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.11.6": "crane digest julia:1.11.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.10.10": "crane digest julia:1.10.10: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.11.7": "crane digest julia:1.11.7: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "1.12.1": "crane digest julia:1.12.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"julia": "/usr/local/julia/bin/julia"}}
---

This module is a singularity container wrapper for julia.
An interpreted, high-level, high-performance dynamic programming language for technical computing.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install julia
```

Or a specific version:

```bash
$ shpc install julia:1.12.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load julia/1.12.1
$ module help julia/1.12.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### julia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### julia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### julia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### julia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### julia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### julia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### julia

```bash
$ singularity exec <container> /usr/local/julia/bin/julia
$ podman run --it --rm --entrypoint /usr/local/julia/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/julia/bin/julia   -v ${PWD} -w ${PWD} <container> -c " $@"
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