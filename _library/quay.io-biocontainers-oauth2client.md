---
layout: container
name:  "quay.io/biocontainers/oauth2client"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/oauth2client/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/oauth2client/container.yaml"
updated_at: "2023-11-22 03:01:32.968691"
latest: "1.5.2--py36_0"
container_url: "https://biocontainers.pro/tools/oauth2client"
aliases:
 - "pyrsa-decrypt-bigfile"
 - "pyrsa-encrypt-bigfile"
 - "easy_install-3.6"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
 - "2to3-3.6"
versions:
 - "1.5.2--py36_0"
description: "shpc-registry automated BioContainers addition for oauth2client"
config: {"url": "https://biocontainers.pro/tools/oauth2client", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for oauth2client", "latest": {"1.5.2--py36_0": "sha256:1e79da7fe2a2fb5672670f5b2427b91a74f3166c6b8fa6fce824588e62fccb16"}, "tags": {"1.5.2--py36_0": "sha256:1e79da7fe2a2fb5672670f5b2427b91a74f3166c6b8fa6fce824588e62fccb16"}, "docker": "quay.io/biocontainers/oauth2client", "aliases": {"pyrsa-decrypt-bigfile": "/usr/local/bin/pyrsa-decrypt-bigfile", "pyrsa-encrypt-bigfile": "/usr/local/bin/pyrsa-encrypt-bigfile", "easy_install-3.6": "/usr/local/bin/easy_install-3.6", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify", "2to3-3.6": "/usr/local/bin/2to3-3.6"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/oauth2client.
shpc-registry automated BioContainers addition for oauth2client
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/oauth2client
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/oauth2client:1.5.2--py36_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/oauth2client/1.5.2--py36_0
$ module help quay.io/biocontainers/oauth2client/1.5.2--py36_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### oauth2client-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### oauth2client-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### oauth2client-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### oauth2client-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### oauth2client-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### oauth2client-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyrsa-decrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-decrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-decrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pyrsa-encrypt-bigfile

```bash
$ singularity exec <container> /usr/local/bin/pyrsa-encrypt-bigfile
$ podman run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyrsa-encrypt-bigfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### easy_install-3.6

```bash
$ singularity exec <container> /usr/local/bin/easy_install-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/easy_install-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### 2to3-3.6

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.6
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.6   -v ${PWD} -w ${PWD} <container> -c " $@"
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