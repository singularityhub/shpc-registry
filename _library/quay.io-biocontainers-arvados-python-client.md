---
layout: container
name:  "quay.io/biocontainers/arvados-python-client"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arvados-python-client/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arvados-python-client/container.yaml"
updated_at: "2023-10-26 02:34:09.810826"
latest: "2.0.2--py_0"
container_url: "https://biocontainers.pro/tools/arvados-python-client"
aliases:
 - "arv-copy"
 - "arv-federation-migrate"
 - "arv-get"
 - "arv-keepdocker"
 - "arv-ls"
 - "arv-migrate-docker19"
 - "arv-normalize"
 - "arv-put"
 - "arv-ws"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
 - "futurize"
 - "pasteurize"
 - "2to3-3.8"
 - "idle3.8"
versions:
 - "2.0.2--py_0"
description: "shpc-registry automated BioContainers addition for arvados-python-client"
config: {"url": "https://biocontainers.pro/tools/arvados-python-client", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arvados-python-client", "latest": {"2.0.2--py_0": "sha256:f3f6a04e4a465fa9d6510bb8baab41d435622a7d95415a79fe94dac907658345"}, "tags": {"2.0.2--py_0": "sha256:f3f6a04e4a465fa9d6510bb8baab41d435622a7d95415a79fe94dac907658345"}, "docker": "quay.io/biocontainers/arvados-python-client", "aliases": {"arv-copy": "/usr/local/bin/arv-copy", "arv-federation-migrate": "/usr/local/bin/arv-federation-migrate", "arv-get": "/usr/local/bin/arv-get", "arv-keepdocker": "/usr/local/bin/arv-keepdocker", "arv-ls": "/usr/local/bin/arv-ls", "arv-migrate-docker19": "/usr/local/bin/arv-migrate-docker19", "arv-normalize": "/usr/local/bin/arv-normalize", "arv-put": "/usr/local/bin/arv-put", "arv-ws": "/usr/local/bin/arv-ws", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify", "futurize": "/usr/local/bin/futurize", "pasteurize": "/usr/local/bin/pasteurize", "2to3-3.8": "/usr/local/bin/2to3-3.8", "idle3.8": "/usr/local/bin/idle3.8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arvados-python-client.
shpc-registry automated BioContainers addition for arvados-python-client
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arvados-python-client
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arvados-python-client:2.0.2--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arvados-python-client/2.0.2--py_0
$ module help quay.io/biocontainers/arvados-python-client/2.0.2--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arvados-python-client-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arvados-python-client-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arvados-python-client-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arvados-python-client-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arvados-python-client-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arvados-python-client-inspect-deffile:

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


#### arv-migrate-docker19

```bash
$ singularity exec <container> /usr/local/bin/arv-migrate-docker19
$ podman run --it --rm --entrypoint /usr/local/bin/arv-migrate-docker19   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arv-migrate-docker19   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### futurize

```bash
$ singularity exec <container> /usr/local/bin/futurize
$ podman run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/futurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pasteurize

```bash
$ singularity exec <container> /usr/local/bin/pasteurize
$ podman run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pasteurize   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.8

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.8
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.8

```bash
$ singularity exec <container> /usr/local/bin/idle3.8
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.8   -v ${PWD} -w ${PWD} <container> -c " $@"
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