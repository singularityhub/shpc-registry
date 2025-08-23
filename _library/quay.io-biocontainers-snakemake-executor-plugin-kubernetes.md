---
layout: container
name:  "quay.io/biocontainers/snakemake-executor-plugin-kubernetes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-executor-plugin-kubernetes/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-executor-plugin-kubernetes/container.yaml"
updated_at: "2025-08-23 03:40:25.697124"
latest: "0.5.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-executor-plugin-kubernetes"
aliases:
 - "wsdump"
 - "2to3-3.12"
 - "idle3.12"
 - "pydoc3.12"
 - "python3.12"
 - "python3.12-config"
 - "pyrsa-decrypt"
 - "pyrsa-encrypt"
 - "pyrsa-keygen"
 - "pyrsa-priv2pub"
 - "pyrsa-sign"
 - "pyrsa-verify"
 - "normalizer"
versions:
 - "0.1.4--pyhdfd78af_0"
 - "0.1.5--pyhdfd78af_0"
 - "0.2.0--pyhdfd78af_0"
 - "0.2.1--pyhdfd78af_0"
 - "0.2.2--pyhdfd78af_0"
 - "0.3.0--pyhdfd78af_0"
 - "0.3.2--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
 - "0.4.1--pyhdfd78af_0"
 - "0.4.2--pyhdfd78af_0"
 - "0.5.0--pyhdfd78af_0"
 - "0.4.4--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-executor-plugin-kubernetes"
config: {"url": "https://biocontainers.pro/tools/snakemake-executor-plugin-kubernetes", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-executor-plugin-kubernetes", "latest": {"0.5.0--pyhdfd78af_0": "sha256:3eeb5685cde7b6bd90b78002c75f05b8a9a6d7427a24e08735f4518eef5f1dce"}, "tags": {"0.1.4--pyhdfd78af_0": "sha256:6aab8d09f4e04e77cbac75eca157ebe0892bf18579fe6fa5307fdba96a93967c", "0.1.5--pyhdfd78af_0": "sha256:3a4d25d89cf7136112c973dcb6cb8e2adfe36a1d614ddd3dcdf08659b81daeb7", "0.2.0--pyhdfd78af_0": "sha256:6ef8336b32f92ec32d1fbbc8790adb84f0ff3f0505222b6bb745ac93c31b6bc5", "0.2.1--pyhdfd78af_0": "sha256:e78b28b3c1a0eb1052a81028aae6cff010c0b69797f17a0b778b3796f9852e8f", "0.2.2--pyhdfd78af_0": "sha256:772e08bf063bdeab075c2a1c9ba57b837b09288ad3817ca0a45061cfe3f10a24", "0.3.0--pyhdfd78af_0": "sha256:fab6d58db88c1182b4a0018514cc5b9bacb2d6f63a107fec6d0c2800d06db1fb", "0.3.2--pyhdfd78af_0": "sha256:951c9ed1ba578c7cc61103c02d09743ba1f7cb3bc807dd7c7e81e6b000f98ed4", "0.4.0--pyhdfd78af_0": "sha256:73972a306ee330d4b1349a9ed0a38f063223b122157836c9565d33f8880d5276", "0.4.1--pyhdfd78af_0": "sha256:fe9f1a8a89d562495964a04dbc2dbfc9c68043836120ef70806724ddeca363ca", "0.4.2--pyhdfd78af_0": "sha256:c727fb2d0e6dc94bb131013b57c3a653e977e183be6ef0ab0ef9f9c09f1fa795", "0.5.0--pyhdfd78af_0": "sha256:3eeb5685cde7b6bd90b78002c75f05b8a9a6d7427a24e08735f4518eef5f1dce", "0.4.4--pyhdfd78af_0": "sha256:5dee2f0604db59c0ac71529242a5bb2897be76c2f5159c48d0a4f983d551ce83"}, "docker": "quay.io/biocontainers/snakemake-executor-plugin-kubernetes", "aliases": {"wsdump": "/usr/local/bin/wsdump", "2to3-3.12": "/usr/local/bin/2to3-3.12", "idle3.12": "/usr/local/bin/idle3.12", "pydoc3.12": "/usr/local/bin/pydoc3.12", "python3.12": "/usr/local/bin/python3.12", "python3.12-config": "/usr/local/bin/python3.12-config", "pyrsa-decrypt": "/usr/local/bin/pyrsa-decrypt", "pyrsa-encrypt": "/usr/local/bin/pyrsa-encrypt", "pyrsa-keygen": "/usr/local/bin/pyrsa-keygen", "pyrsa-priv2pub": "/usr/local/bin/pyrsa-priv2pub", "pyrsa-sign": "/usr/local/bin/pyrsa-sign", "pyrsa-verify": "/usr/local/bin/pyrsa-verify", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-executor-plugin-kubernetes.
singularity registry hpc automated addition for snakemake-executor-plugin-kubernetes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-executor-plugin-kubernetes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-executor-plugin-kubernetes:0.5.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-executor-plugin-kubernetes/0.5.0--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-executor-plugin-kubernetes/0.5.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-executor-plugin-kubernetes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-executor-plugin-kubernetes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-executor-plugin-kubernetes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-executor-plugin-kubernetes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-executor-plugin-kubernetes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-executor-plugin-kubernetes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wsdump

```bash
$ singularity exec <container> /usr/local/bin/wsdump
$ podman run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wsdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.12

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.12
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.12

```bash
$ singularity exec <container> /usr/local/bin/idle3.12
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.12

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.12
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12

```bash
$ singularity exec <container> /usr/local/bin/python3.12
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.12-config

```bash
$ singularity exec <container> /usr/local/bin/python3.12-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.12-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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