---
layout: container
name:  "quay.io/biocontainers/crunchstat-summary"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/crunchstat-summary/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/crunchstat-summary/container.yaml"
updated_at: "2025-12-26 04:00:40.915339"
latest: "3.2.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/crunchstat-summary"
aliases:
 - "arv-copy"
 - "arv-federation-migrate"
 - "arv-get"
 - "arv-keepdocker"
 - "arv-ls"
 - "arv-normalize"
 - "arv-put"
 - "arv-ws"
 - "crunchstat-summary"
 - "websockets"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "normalizer"
versions:
 - "3.1.2--pyhdfd78af_0"
 - "3.2.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for crunchstat-summary"
config: {"url": "https://biocontainers.pro/tools/crunchstat-summary", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for crunchstat-summary", "latest": {"3.2.0--pyhdfd78af_0": "sha256:0c0bdff65528564206bd648fd5c63c31cac9315ce3f1addf4f14aea5d86d958d"}, "tags": {"3.1.2--pyhdfd78af_0": "sha256:5c519257e99a5ed22796075726c0e905a5c93f8d60a56ebf0b20828604a37833", "3.2.0--pyhdfd78af_0": "sha256:0c0bdff65528564206bd648fd5c63c31cac9315ce3f1addf4f14aea5d86d958d"}, "docker": "quay.io/biocontainers/crunchstat-summary", "aliases": {"arv-copy": "/usr/local/bin/arv-copy", "arv-federation-migrate": "/usr/local/bin/arv-federation-migrate", "arv-get": "/usr/local/bin/arv-get", "arv-keepdocker": "/usr/local/bin/arv-keepdocker", "arv-ls": "/usr/local/bin/arv-ls", "arv-normalize": "/usr/local/bin/arv-normalize", "arv-put": "/usr/local/bin/arv-put", "arv-ws": "/usr/local/bin/arv-ws", "crunchstat-summary": "/usr/local/bin/crunchstat-summary", "websockets": "/usr/local/bin/websockets", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/crunchstat-summary.
singularity registry hpc automated addition for crunchstat-summary
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/crunchstat-summary
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/crunchstat-summary:3.2.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/crunchstat-summary/3.2.0--pyhdfd78af_0
$ module help quay.io/biocontainers/crunchstat-summary/3.2.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### crunchstat-summary-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### crunchstat-summary-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### crunchstat-summary-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### crunchstat-summary-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### crunchstat-summary-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### crunchstat-summary-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arv-copy

```bash
$ singularity exec <container> /usr/local/bin/arv-copy
$ podman run --it --rm --entrypoint /usr/local/bin/arv-copy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-copy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-federation-migrate

```bash
$ singularity exec <container> /usr/local/bin/arv-federation-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/arv-federation-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-federation-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-get

```bash
$ singularity exec <container> /usr/local/bin/arv-get
$ podman run --it --rm --entrypoint /usr/local/bin/arv-get   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-get   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-keepdocker

```bash
$ singularity exec <container> /usr/local/bin/arv-keepdocker
$ podman run --it --rm --entrypoint /usr/local/bin/arv-keepdocker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-keepdocker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-ls

```bash
$ singularity exec <container> /usr/local/bin/arv-ls
$ podman run --it --rm --entrypoint /usr/local/bin/arv-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-ls   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-normalize

```bash
$ singularity exec <container> /usr/local/bin/arv-normalize
$ podman run --it --rm --entrypoint /usr/local/bin/arv-normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-normalize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-put

```bash
$ singularity exec <container> /usr/local/bin/arv-put
$ podman run --it --rm --entrypoint /usr/local/bin/arv-put   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-put   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### arv-ws

```bash
$ singularity exec <container> /usr/local/bin/arv-ws
$ podman run --it --rm --entrypoint /usr/local/bin/arv-ws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-ws   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### crunchstat-summary

```bash
$ singularity exec <container> /usr/local/bin/crunchstat-summary
$ podman run --it --rm --entrypoint /usr/local/bin/crunchstat-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/crunchstat-summary   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### websockets

```bash
$ singularity exec <container> /usr/local/bin/websockets
$ podman run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/websockets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-decrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-keygen

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-keygen
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-keygen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-priv2pub

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-priv2pub
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-priv2pub   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-sign

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-sign
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-sign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-sign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-verify

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-verify
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-verify   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.13

```bash
$ singularity exec <container> /usr/local/bin/idle3.13
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.13

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.13
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13

```bash
$ singularity exec <container> /usr/local/bin/python3.13
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.13-config

```bash
$ singularity exec <container> /usr/local/bin/python3.13-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.13-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
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