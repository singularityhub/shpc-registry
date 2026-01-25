---
layout: container
name:  "quay.io/biocontainers/sylph-tax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sylph-tax/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sylph-tax/container.yaml"
updated_at: "2026-01-25 04:11:48.288281"
latest: "1.8.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/sylph-tax"
aliases:
 - "sylph-tax"
 - "idle3.13"
 - "pydoc3.13"
 - "python3.13"
 - "python3.13-config"
 - "numpy-config"
 - "normalizer"
versions:
 - "1.1.0--pyhdfd78af_0"
 - "1.1.1--pyhdfd78af_1"
 - "1.2.0--pyhdfd78af_0"
 - "1.1.2--pyhdfd78af_0"
 - "1.3.0--pyhdfd78af_0"
 - "1.5.1--pyhdfd78af_0"
 - "1.4.0--pyhdfd78af_0"
 - "1.7.0--pyhdfd78af_0"
 - "1.6.0--pyhdfd78af_0"
 - "1.8.0--pyhdfd78af_0"
 - "1.7.1--pyhdfd78af_0"
description: "singularity registry hpc automated addition for sylph-tax"
config: {"url": "https://biocontainers.pro/tools/sylph-tax", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sylph-tax", "latest": {"1.8.0--pyhdfd78af_0": "sha256:67f700a00dff47ccb1bf81a7fd0314b5f0e39f9dd76ad254e93153d21ad1ceae"}, "tags": {"1.1.0--pyhdfd78af_0": "sha256:1ff8be4412b5cfff98232626af7c2bbc46a601fa1b5513e7d6dada608c3fb2a3", "1.1.1--pyhdfd78af_1": "sha256:1cb9455edec898f40b466cccd7fd149ae03a1355be3d5459391c8908c45ea6d5", "1.2.0--pyhdfd78af_0": "sha256:bec3991be39c1dd6100dc1fa8b6c4b011ab8ce63b5695b03126c6ad93e8ca9f3", "1.1.2--pyhdfd78af_0": "sha256:c31509ec3944abd4c663305e8462a67041272834bcbd88c6d62066a4e3f768df", "1.3.0--pyhdfd78af_0": "sha256:b4dd5459d9f1ef092aa1b51c3c8dc4384650259fe2d7bd4de97a7d11071dc458", "1.5.1--pyhdfd78af_0": "sha256:11cd8807d08321e026633f9b1ad779ef46deffecc190b0f21fe224c448652d05", "1.4.0--pyhdfd78af_0": "sha256:edafd08ce5fe07fcd6e5f9121f5fbdf9298a90f4849d5bc5d1fd2e6a33c1f051", "1.7.0--pyhdfd78af_0": "sha256:d17d6441c60bdc7e2b25663d0c1dea50ec37bcbbf71ce2b4ba72c0b1852c15d4", "1.6.0--pyhdfd78af_0": "sha256:92ae64644f9fc7bdd3d9772c898646bdbbb6809f6c369c6004037874a859cca6", "1.8.0--pyhdfd78af_0": "sha256:67f700a00dff47ccb1bf81a7fd0314b5f0e39f9dd76ad254e93153d21ad1ceae", "1.7.1--pyhdfd78af_0": "sha256:7d5ddd8012de40c3e84c4609e6098468e82213bb6c28a7996aa65de7673247bb"}, "docker": "quay.io/biocontainers/sylph-tax", "aliases": {"sylph-tax": "/usr/local/bin/sylph-tax", "idle3.13": "/usr/local/bin/idle3.13", "pydoc3.13": "/usr/local/bin/pydoc3.13", "python3.13": "/usr/local/bin/python3.13", "python3.13-config": "/usr/local/bin/python3.13-config", "numpy-config": "/usr/local/bin/numpy-config", "normalizer": "/usr/local/bin/normalizer"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sylph-tax.
singularity registry hpc automated addition for sylph-tax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sylph-tax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sylph-tax:1.8.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sylph-tax/1.8.0--pyhdfd78af_0
$ module help quay.io/biocontainers/sylph-tax/1.8.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sylph-tax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sylph-tax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sylph-tax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sylph-tax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sylph-tax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sylph-tax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sylph-tax

```bash
$ singularity exec <container> /usr/local/bin/sylph-tax
$ podman run --it --rm --entrypoint /usr/local/bin/sylph-tax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sylph-tax   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### numpy-config

```bash
$ singularity exec <container> /usr/local/bin/numpy-config
$ podman run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/numpy-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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