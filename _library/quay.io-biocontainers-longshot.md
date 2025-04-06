---
layout: container
name:  "quay.io/biocontainers/longshot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/longshot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/longshot/container.yaml"
updated_at: "2025-04-06 03:50:22.765098"
latest: "1.0.0--h8dc4d9d_3"
container_url: "https://biocontainers.pro/tools/longshot"
aliases:
 - "longshot"
versions:
 - "v0.3.5--h80880c6_0"
 - "0.4.5--hc4ca7c3_0"
 - "0.4.5--hd175d40_2"
 - "1.0.0--hd4f2111_0"
 - "0.3.5--h80880c6_0"
 - "1.0.0--hd4f2111_1"
 - "1.0.0--hd4f2111_2"
 - "1.0.0--h8dc4d9d_3"
description: "shpc-registry automated BioContainers addition for longshot"
config: {"url": "https://biocontainers.pro/tools/longshot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for longshot", "latest": {"1.0.0--h8dc4d9d_3": "sha256:420bc9cd43ff4c8fa3d1d02d7797e810f2bfe0c75ad290ac30887860afbdc397"}, "tags": {"v0.3.5--h80880c6_0": "sha256:21d5002f3f61ca69eb46d19f0e6bebfb85516adb2efe5381cba82a14dee3a10b", "0.4.5--hc4ca7c3_0": "sha256:2875eb55c1c48050e3cc7bb218710e2dccd6f5c43b9065b9debb7d8b96490f05", "0.4.5--hd175d40_2": "sha256:1bf8278e82945cc7a8ca7eee3a71a84c43dd89f598da5cb64f458ae9cc535af8", "1.0.0--hd4f2111_0": "sha256:52494d2eabe6c6c3f34d91331b1b96a120dd50616e9702f4c6c53ca193e1ced0", "0.3.5--h80880c6_0": "sha256:1581c4f1fe8d53b5310c5d0d5a26ff10cddbf1192e17dba47ed45604c5e211d8", "1.0.0--hd4f2111_1": "sha256:4ef1476883b376b0a91a010f9c011fb23670d29410b4974ca1421aadad30d7b9", "1.0.0--hd4f2111_2": "sha256:a4cabce7ec05a66b9f05b7643caca2d337efbf7035969ac48ca3f9faafbd192f", "1.0.0--h8dc4d9d_3": "sha256:420bc9cd43ff4c8fa3d1d02d7797e810f2bfe0c75ad290ac30887860afbdc397"}, "docker": "quay.io/biocontainers/longshot", "aliases": {"longshot": "/usr/local/bin/longshot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/longshot.
shpc-registry automated BioContainers addition for longshot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/longshot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/longshot:1.0.0--h8dc4d9d_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/longshot/1.0.0--h8dc4d9d_3
$ module help quay.io/biocontainers/longshot/1.0.0--h8dc4d9d_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### longshot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### longshot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### longshot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### longshot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### longshot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### longshot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### longshot

```bash
$ singularity exec <container> /usr/local/bin/longshot
$ podman run --it --rm --entrypoint /usr/local/bin/longshot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/longshot   -v ${PWD} -w ${PWD} <container> -c " $@"
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