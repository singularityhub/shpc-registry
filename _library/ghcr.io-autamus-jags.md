---
layout: container
name:  "ghcr.io/autamus/jags"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/jags/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/jags/container.yaml"
updated_at: "2023-09-09 02:19:40.432239"
latest: "4.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/jags"
aliases:
 - "jags"
versions:
 - "4.3.0"
 - "latest"
description: "Just Another Gibbs Sampler. A program for analysis of Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation."
config: {"docker": "ghcr.io/autamus/jags", "url": "https://github.com/orgs/autamus/packages/container/package/jags", "maintainer": "@vsoch", "description": "Just Another Gibbs Sampler. A program for analysis of Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation.", "latest": {"4.3.0": "sha256:bde77ead68db14b12746178ff3781f658956b4f4d91d9704acade734bf197d0f"}, "tags": {"4.3.0": "sha256:bde77ead68db14b12746178ff3781f658956b4f4d91d9704acade734bf197d0f", "latest": "sha256:bde77ead68db14b12746178ff3781f658956b4f4d91d9704acade734bf197d0f"}, "aliases": {"jags": "/opt/view/bin/jags"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/jags.
Just Another Gibbs Sampler. A program for analysis of Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/jags
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/jags:4.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/jags/4.3.0
$ module help ghcr.io/autamus/jags/4.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### jags-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### jags-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### jags-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### jags-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### jags-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### jags-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### jags

```bash
$ singularity exec <container> /opt/view/bin/jags
$ podman run --it --rm --entrypoint /opt/view/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/jags   -v ${PWD} -w ${PWD} <container> -c " $@"
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