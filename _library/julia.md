---
layout: container
name:  "julia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/julia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/julia/container.yaml"
updated_at: "2023-11-23 02:27:41.148335"
latest: "1.9.4"
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
description: "An interpreted, high-level, high-performance dynamic programming language for technical computing."
config: {"docker": "julia", "url": "https://hub.docker.com/_/julia", "maintainer": "@marcodelapierre", "description": "An interpreted, high-level, high-performance dynamic programming language for technical computing.", "latest": {"1.9.4": "sha256:2a6c8fc56eec5988886ae270da7f97a52b4cb75afba9aedb44195f2ecd7240a5"}, "tags": {"1.8.3": "sha256:172938f81c0a5f607a71c6babeb6f0d0aac7a9bb3d43b000734b80f764748448", "1.8.5": "sha256:c9c13e38ea7ef6a893b97834e75f00fec4fc07b24072088e1360171cb192ebb0", "1.9.0": "sha256:a4eba1f0c1c2076eef737f5f441c80de87997faab982e816fd256e50326c6c8d", "1.9.1": "sha256:9313aec843ab5395eb0898b004737497da2b7ed50d72b53fc94dfca014af7d51", "1.9.2": "sha256:f4ec5401b88c20c01565ad55b826821f987369ab461dedb72706d95798d4ddb0", "1.9.3": "sha256:2bb36ee0d8b44fb2a1e034fa4e636c66ccc713fa0a41ca23b5d9207b837cb41a", "1.9.4": "sha256:2a6c8fc56eec5988886ae270da7f97a52b4cb75afba9aedb44195f2ecd7240a5"}, "filter": ["^[0-9]+[.][0-9]+[.][0-9]+$"], "aliases": {"julia": "/usr/local/julia/bin/julia"}}
---

This module is a singularity container wrapper for julia.
An interpreted, high-level, high-performance dynamic programming language for technical computing.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install julia
```

Or a specific version:

```bash
$ shpc install julia:1.9.4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load julia/1.9.4
$ module help julia/1.9.4
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