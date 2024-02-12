---
layout: container
name:  "php"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/php/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/php/container.yaml"
updated_at: "2024-02-12 03:06:00.633703"
latest: "8-alpine3.19"
container_url: "https://hub.docker.com/_/php"
aliases:
 - "php"
 - "php-cgi"
 - "php-config"
 - "phpdbg"
 - "phpize"
versions:
 - "7.3.27-zts-alpine3.12"
 - "8.0.3-alpine"
 - "8.0.5-alpine"
 - "8.0.6-alpine"
 - "8.0.7-alpine"
 - "8.1.0"
 - "8.1.0RC1"
 - "8.1.0alpha1"
 - "8.1.0alpha1-alpine"
 - "8.1.1"
 - "8.1.2"
 - "8.1.3"
 - "latest"
 - "8"
 - "8-alpine3.15"
 - "8.1"
 - "8.0"
 - "7"
 - "8-alpine3.16"
 - "8.2-rc"
 - "8-alpine3.17"
 - "8.2"
 - "8-alpine3.18"
 - "8-alpine3.19"
description: "While designed for web development, the PHP scripting language also provides general-purpose use."
config: {"docker": "php", "url": "https://hub.docker.com/_/php", "maintainer": "@vsoch", "description": "While designed for web development, the PHP scripting language also provides general-purpose use.", "latest": {"8-alpine3.19": "sha256:ea8cdb42a3def0a4d65226f9348fa4ea67ef9bbefb445200778f329c795e9b4b"}, "tags": {"7.3.27-zts-alpine3.12": "sha256:33c32435b162a6aa427a506f4d3fd3616ab1897a0211c5787649e9e07b967223", "8.0.3-alpine": "sha256:f32cd843417d9271d1500ed3867922175604a243d8033ad1572d617ad7954171", "8.0.5-alpine": "sha256:b728c7e60d1bdb28bfba1bbd4ac3328fbde3a70a959a55c318ccae3fc4d170cf", "8.0.6-alpine": "sha256:a5afa558fcf8030edbc0f160339eaeefccdf1af53df35d0d26171c470a7ab5b6", "8.0.7-alpine": "sha256:edd37734c824c65cdbc1e68c9ac928c590a5c750b6b49c656a302b3b0742d371", "8.1.0": "sha256:b2afd03bcad73aa0a207b0be83310fb2cb35b7a47aceb89e82437b1d19bf81c5", "8.1.0RC1": "sha256:cfa06c39de438a7b7a3977d6412ec580721ad440472b0973ed87ff3758adb0aa", "8.1.0alpha1": "sha256:a63a64bc485982b0543af4ff2fe6e42cd82d65afc39eb4e073f5d361636513fb", "8.1.0alpha1-alpine": "sha256:028c42e86276c77e4bf5d05fb9df93142344d83f971f369a80b6f6e30a50e14b", "8.1.1": "sha256:444ba13f11741642a2692430f6678d47fb028442160ec9a5cfa9da7d3c0a9e07", "8.1.2": "sha256:f1d66b530e99d2e3c2ea302523c5a10ae9e666ddb5ceaacb7dda0af20c7976d7", "8.1.3": "sha256:c0dc322c09db1db4a02f98c97a361a91308c29a3d256703c1e1b64f1ddc28ac6", "latest": "sha256:fc30b665b620e6c0094cca72259ebf16bea4874719c792aba1c87aacb08f1e29", "8": "sha256:fc30b665b620e6c0094cca72259ebf16bea4874719c792aba1c87aacb08f1e29", "8-alpine3.15": "sha256:26d871b044c414dcf3564a018197211627d8b06e7b29415e870a585a2f365c3f", "8.1": "sha256:22130782854d1e8844b404a03c869e9ba91a24645c3d6af2e739874f32a12909", "8.0": "sha256:0569e384b9064c04dec55dc6e41be41b494a878dfbb6577a7d76bd50cfd5bc00", "7": "sha256:620a6b9f4d4feef2210026172570465e9d0c1de79766418d3affd09190a7fda5", "8-alpine3.16": "sha256:9085a1c6e1c866314dccad5687254f98a139a36938e87235e65f13c83bfe9352", "8.2-rc": "sha256:49b4363cd48f5d9a20e74bccbb27a91fbcdb33def4e5a9cb3e0f3968dfdb33af", "8-alpine3.17": "sha256:af0809570027627bd16e89dea01fefcec427a1220dcaa494ee9d7afdfcfc2fcc", "8.2": "sha256:e0941c06b8a4f6e48c7c57672dce608d1e314419b5c14b4f385cd9550cc7abb6", "8-alpine3.18": "sha256:eac969afaba4b30c9228f9e1421188ac9997105c06dc51203fc7c4cf739bd688", "8-alpine3.19": "sha256:ea8cdb42a3def0a4d65226f9348fa4ea67ef9bbefb445200778f329c795e9b4b"}, "aliases": {"php": "/usr/local/bin/php", "php-cgi": "/usr/local/bin/php-cgi", "php-config": "/usr/local/bin/php-config", "phpdbg": "/usr/local/bin/phpdbg", "phpize": "/usr/local/bin/phpize"}}
---

This module is a singularity container wrapper for php.
While designed for web development, the PHP scripting language also provides general-purpose use.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install php
```

Or a specific version:

```bash
$ shpc install php:8-alpine3.19
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load php/8-alpine3.19
$ module help php/8-alpine3.19
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### php-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### php-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### php-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### php-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### php-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### php-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### php

```bash
$ singularity exec <container> /usr/local/bin/php
$ podman run --it --rm --entrypoint /usr/local/bin/php   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/php   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### php-cgi

```bash
$ singularity exec <container> /usr/local/bin/php-cgi
$ podman run --it --rm --entrypoint /usr/local/bin/php-cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/php-cgi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### php-config

```bash
$ singularity exec <container> /usr/local/bin/php-config
$ podman run --it --rm --entrypoint /usr/local/bin/php-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/php-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phpdbg

```bash
$ singularity exec <container> /usr/local/bin/phpdbg
$ podman run --it --rm --entrypoint /usr/local/bin/phpdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phpdbg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### phpize

```bash
$ singularity exec <container> /usr/local/bin/phpize
$ podman run --it --rm --entrypoint /usr/local/bin/phpize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phpize   -v ${PWD} -w ${PWD} <container> -c " $@"
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