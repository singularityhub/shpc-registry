---
layout: container
name:  "bids/validator"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/validator/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/validator/container.yaml"
updated_at: "2026-01-01 04:48:07.650053"
latest: "2.5.6"
container_url: "https://hub.docker.com/r/bids/validator"
aliases:
 - "bids-validator"
versions:
 - "latest"
 - "v1.7.0"
 - "v1.7.1"
 - "v1.7.3-dev.0"
 - "v1.7.4-dev.0"
 - "v1.8.1-dev.0"
 - "v1.8.5"
 - "v1.8.9"
 - "v1.9.2"
 - "2.1.0"
 - "2.0.11"
 - "2.2.0"
 - "2.1.1"
 - "2.2.3"
 - "2.5.6"
 - "2.2.6"
description: "A validator for BIDS (Brain Imaging Data Structure) datasets."
config: {"docker": "bids/validator", "url": "https://hub.docker.com/r/bids/validator", "maintainer": "@vsoch", "description": "A validator for BIDS (Brain Imaging Data Structure) datasets.", "latest": {"2.5.6": "crane digest bids/validator:2.5.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "tags": {"latest": "sha256:9dfffd2b77fd3331a9d6b790a44ad6e2878780c1d3bfbd30b7dc5d4d6114245d", "v1.7.0": "sha256:51c9481b357448cc2138909e03dfa8e053d424d5e776e94dbec929aeb96f9563", "v1.7.1": "sha256:d07b847f26e77e842abfd5b964f8553eb458ca796f4f0f5d1ca8d9290552ac2c", "v1.7.3-dev.0": "crane digest bids/validator:v1.7.3-dev.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v1.7.4-dev.0": "crane digest bids/validator:v1.7.4-dev.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v1.8.1-dev.0": "crane digest bids/validator:v1.8.1-dev.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v1.8.5": "crane digest bids/validator:v1.8.5: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v1.8.9": "crane digest bids/validator:v1.8.9: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "v1.9.2": "crane digest bids/validator:v1.9.2: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "2.1.0": "crane digest bids/validator:2.1.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "2.0.11": "crane digest bids/validator:2.0.11: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "2.2.0": "crane digest bids/validator:2.2.0: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "2.1.1": "crane digest bids/validator:2.1.1: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "2.2.3": "crane digest bids/validator:2.2.3: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "2.5.6": "crane digest bids/validator:2.5.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit", "2.2.6": "crane digest bids/validator:2.2.6: TOOMANYREQUESTS: You have reached your unauthenticated pull rate limit. https://www.docker.com/increase-rate-limit"}, "filter": ["v*"], "aliases": {"bids-validator": "/usr/local/bin/bids-validator"}}
---

This module is a singularity container wrapper for bids/validator.
A validator for BIDS (Brain Imaging Data Structure) datasets.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/validator
```

Or a specific version:

```bash
$ shpc install bids/validator:2.5.6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/validator/2.5.6
$ module help bids/validator/2.5.6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### validator-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### validator-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### validator-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### validator-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### validator-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### validator-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bids-validator

```bash
$ singularity exec <container> /usr/local/bin/bids-validator
$ podman run --it --rm --entrypoint /usr/local/bin/bids-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bids-validator   -v ${PWD} -w ${PWD} <container> -c " $@"
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