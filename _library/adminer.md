---
layout: container
name:  "adminer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/adminer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/adminer/container.yaml"
updated_at: "2026-03-05 04:15:02.871320"
latest: "5.4.2"
container_url: "https://hub.docker.com/_/adminer"

versions:
 - "4.8.0-fastcgi"
 - "4.8.1"
 - "4.8.1-fastcgi"
 - "latest"
 - "4"
 - "5"
 - "5.0.6"
 - "4.17.1"
 - "5.2.1"
 - "5.1.0"
 - "5.3.0"
 - "5.4.0"
 - "5.4.1"
 - "5.4.2"
description: "Database management in a single PHP file."
config: {"docker": "adminer", "url": "https://hub.docker.com/_/adminer", "maintainer": "@vsoch", "description": "Database management in a single PHP file.", "latest": {"5.4.2": "crane digest adminer:5.4.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"4.8.0-fastcgi": "sha256:5368f087fed03f49e9de8731ee3d9998d7e78391720d500309b5bcde2a401058", "4.8.1": "sha256:34d37131366c5aa84e1693dbed48593ed6f95fb450b576c1a7a59d3a9c9e8802", "4.8.1-fastcgi": "sha256:470601adfd8d1ab5f1006c82ad76022283ce91ea86c56064218514b13b5f7d48", "latest": "crane digest adminer:latest: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "4": "crane digest adminer:4: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5": "crane digest adminer:5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.0.6": "crane digest adminer:5.0.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "4.17.1": "crane digest adminer:4.17.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.2.1": "crane digest adminer:5.2.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.1.0": "crane digest adminer:5.1.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.3.0": "crane digest adminer:5.3.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.4.0": "crane digest adminer:5.4.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.4.1": "crane digest adminer:5.4.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "5.4.2": "crane digest adminer:5.4.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}}
---

This module is a singularity container wrapper for adminer.
Database management in a single PHP file.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install adminer
```

Or a specific version:

```bash
$ shpc install adminer:5.4.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load adminer/5.4.2
$ module help adminer/5.4.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### adminer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### adminer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### adminer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### adminer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### adminer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### adminer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### adminer

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