---
layout: container
name:  "quay.io/biocontainers/cramino"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cramino/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cramino/container.yaml"
updated_at: "2025-10-02 03:01:44.231791"
latest: "1.1.0--h3dc2dae_0"
container_url: "https://biocontainers.pro/tools/cramino"
aliases:
 - "cramino"
versions:
 - "0.9.7--h1f4ba0c_0"
 - "0.9.7--h5076881_2"
 - "0.9.9--h5076881_0"
 - "0.10.0--h5076881_0"
 - "0.13.0--h5076881_0"
 - "0.11.1--h5076881_0"
 - "0.13.1--h5076881_0"
 - "0.14.5--h5076881_0"
 - "0.15.0--h2e7e638_0"
 - "0.15.0--h3dc2dae_1"
 - "0.16.0--h3dc2dae_0"
 - "1.0.0--h3dc2dae_0"
 - "0.17.0--h3dc2dae_0"
 - "1.1.0--h3dc2dae_0"
description: "singularity registry hpc automated addition for cramino"
config: {"url": "https://biocontainers.pro/tools/cramino", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cramino", "latest": {"1.1.0--h3dc2dae_0": "sha256:a0ed72cbb52240e6cb0085bea16f5356b3d790621281dd11cecc2f5173e5f791"}, "tags": {"0.9.7--h1f4ba0c_0": "sha256:e7f991ca405c3f613489a6e501225ab265ba39ae7b01e8cdedbdca2abcd26e9c", "0.9.7--h5076881_2": "sha256:314c0746d7a6b987e4677394bc810fcfffef0ff655da417c48dede27984965f2", "0.9.9--h5076881_0": "sha256:059b1e148861c50a15a92e1ac2c2ef0e1e405ff8c731c821b8527ac955d37edd", "0.10.0--h5076881_0": "sha256:f6aad86b3d8faaf42b2b6f83889d1523996cae1befc9c381a1f24c7adafc4e8f", "0.13.0--h5076881_0": "sha256:b4aacd4e0b38bce572405928428cc5f15ba4a9d032eb34ebdb12d122ede124f7", "0.11.1--h5076881_0": "sha256:e9e4b5e1148685be3a75acd0115d9b19ede7d53ca6481a23bb517c55203e21df", "0.13.1--h5076881_0": "sha256:38eab88817002dff00b2fde9ab968c3590f1a0b57e6b74291bfc96500c98cd5e", "0.14.5--h5076881_0": "sha256:2344aed014225f96ef8c38d3ab7b639896b0cbba40f855db0de6c3ec00ff325c", "0.15.0--h2e7e638_0": "sha256:e80b80e4b0b233ae3dc0827d3b4d65561396ec99569436885c2534171ca675a2", "0.15.0--h3dc2dae_1": "sha256:d290adb8c38de7454b372a2a1ce507c45f2f0f2049b327972e91967605337bc4", "0.16.0--h3dc2dae_0": "sha256:97d78c137661daee46593b4206bcc14f1410a17933067cf586d32dd63707c513", "1.0.0--h3dc2dae_0": "sha256:0caaed3e75d3da3cddb3025cf5b5caf490b08cc0ac0b34eda216c56caabc01dc", "0.17.0--h3dc2dae_0": "sha256:c3f7bd77df9825d552c8453e3f056f65ce92f4555b3d78e3097e6aebddbaa648", "1.1.0--h3dc2dae_0": "sha256:a0ed72cbb52240e6cb0085bea16f5356b3d790621281dd11cecc2f5173e5f791"}, "docker": "quay.io/biocontainers/cramino", "aliases": {"cramino": "/usr/local/bin/cramino"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cramino.
singularity registry hpc automated addition for cramino
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cramino
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cramino:1.1.0--h3dc2dae_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cramino/1.1.0--h3dc2dae_0
$ module help quay.io/biocontainers/cramino/1.1.0--h3dc2dae_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cramino-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cramino-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cramino-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cramino-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cramino-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cramino-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cramino

```bash
$ singularity exec <container> /usr/local/bin/cramino
$ podman run --it --rm --entrypoint /usr/local/bin/cramino   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cramino   -v ${PWD} -w ${PWD} <container> -c " $@"
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