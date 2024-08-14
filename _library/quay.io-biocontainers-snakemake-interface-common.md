---
layout: container
name:  "quay.io/biocontainers/snakemake-interface-common"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-interface-common/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-interface-common/container.yaml"
updated_at: "2024-08-14 02:39:53.406661"
latest: "1.17.2--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/snakemake-interface-common"
aliases:
 - "2to3-3.11"
 - "idle3.11"
 - "pydoc3.11"
 - "python3.11"
 - "python3.11-config"
 - "python3.1"
versions:
 - "1.3.2--pyhdfd78af_0"
 - "1.3.3--pyhdfd78af_0"
 - "1.13.0--pyhdfd78af_0"
 - "1.12.0--pyhdfd78af_0"
 - "1.10.0--pyhdfd78af_0"
 - "1.8.0--pyhdfd78af_0"
 - "1.7.3--pyhdfd78af_0"
 - "1.14.2--pyhdfd78af_0"
 - "1.15.0--pyhdfd78af_0"
 - "1.14.5--pyhdfd78af_0"
 - "1.15.0--pyhdfd78af_1"
 - "1.16.0--pyhdfd78af_0"
 - "1.15.3--pyhdfd78af_0"
 - "1.17.1--pyhdfd78af_0"
 - "1.17.2--pyhdfd78af_0"
description: "singularity registry hpc automated addition for snakemake-interface-common"
config: {"url": "https://biocontainers.pro/tools/snakemake-interface-common", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for snakemake-interface-common", "latest": {"1.17.2--pyhdfd78af_0": "sha256:930eb084f33ca76b17ec9fe83a8c8ea333fbcaa7d0aa38b323af7102f2e59a11"}, "tags": {"1.3.2--pyhdfd78af_0": "sha256:7e93336aa4916239ce3f22b8fda19fca1cf7c62ab2c128a208ea0237d43d3654", "1.3.3--pyhdfd78af_0": "sha256:3515869806b5ae5df4c43376493e312a7e089ec03f656e6ee239d2f8006c0131", "1.13.0--pyhdfd78af_0": "sha256:714879daeb01a00909f8ba7a93b7bca5324576b25b6860e1c1abea42544994fc", "1.12.0--pyhdfd78af_0": "sha256:409b6a71789c93a4596a7b14b055b9180440b0e450313cf4cfd7e5ff0e3d9079", "1.10.0--pyhdfd78af_0": "sha256:08becbdc3ba89912468b49f532c8fc49b5c0b7dbffe6ec0ccb5cc15d239127ea", "1.8.0--pyhdfd78af_0": "sha256:67087bd8555e04ebf778035bc2b0eb69240c14d7d54e1eba0ecc7da16a344ec7", "1.7.3--pyhdfd78af_0": "sha256:306c63e0d9c9e26e56ff32e8f35a158368cab33afbf4d34d978544d11ec6e50a", "1.14.2--pyhdfd78af_0": "sha256:fca8690447904ce2b5ca7f9c645c46cd1e3de0fb1b83b81f4ecbb60bc1b974fd", "1.15.0--pyhdfd78af_0": "sha256:d3007237bd9c890bee82796684e571338d8692983758bd3fbb1dc7e268db946f", "1.14.5--pyhdfd78af_0": "sha256:09472bee24f1e2d2558fa23981b4f04d43d7e6890a1a266a8ff0ef801d5b5136", "1.15.0--pyhdfd78af_1": "sha256:64f5dc66327155ab7b67c96d1b3c36037945affe842310d2841ecadf93c26b0c", "1.16.0--pyhdfd78af_0": "sha256:f8c77082674133cdcb297eeeca7ae9196aa50098ce69e2ee56f1fda588a876b2", "1.15.3--pyhdfd78af_0": "sha256:01321a257949ce0f590fb54ca59aeb2a0d5501c8eb3e78c5e28ce2b8d62a7931", "1.17.1--pyhdfd78af_0": "sha256:83b24fd18ffb43cc9f624998b1bf85241de98abb3b8af162681cdfd9342603ea", "1.17.2--pyhdfd78af_0": "sha256:930eb084f33ca76b17ec9fe83a8c8ea333fbcaa7d0aa38b323af7102f2e59a11"}, "docker": "quay.io/biocontainers/snakemake-interface-common", "aliases": {"2to3-3.11": "/usr/local/bin/2to3-3.11", "idle3.11": "/usr/local/bin/idle3.11", "pydoc3.11": "/usr/local/bin/pydoc3.11", "python3.11": "/usr/local/bin/python3.11", "python3.11-config": "/usr/local/bin/python3.11-config", "python3.1": "/usr/local/bin/python3.1"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-interface-common.
singularity registry hpc automated addition for snakemake-interface-common
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-interface-common
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-interface-common:1.17.2--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-interface-common/1.17.2--pyhdfd78af_0
$ module help quay.io/biocontainers/snakemake-interface-common/1.17.2--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-interface-common-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-interface-common-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-interface-common-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-interface-common-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-interface-common-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-interface-common-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 2to3-3.11

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.11
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.11

```bash
$ singularity exec <container> /usr/local/bin/idle3.11
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.11

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.11
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11

```bash
$ singularity exec <container> /usr/local/bin/python3.11
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.11-config

```bash
$ singularity exec <container> /usr/local/bin/python3.11-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
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