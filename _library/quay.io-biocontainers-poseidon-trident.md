---
layout: container
name:  "quay.io/biocontainers/poseidon-trident"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/poseidon-trident/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/poseidon-trident/container.yaml"
updated_at: "2024-11-29 03:14:03.435801"
latest: "1.5.7.0--hf48d1a7_0"
container_url: "https://biocontainers.pro/tools/poseidon-trident"
aliases:
 - "trident"
versions:
 - "0.28.0--h9325052_0"
 - "1.1.6.0--h9325052_0"
 - "1.1.11.0--h9325052_0"
 - "1.1.11.0--hf48d1a7_2"
 - "1.2.0.0--hf48d1a7_0"
 - "1.3.0.4--hf48d1a7_0"
 - "1.4.1.0--hf48d1a7_0"
 - "1.5.0.1--hf48d1a7_0"
 - "1.5.4.0--hf48d1a7_0"
 - "1.5.7.0--hf48d1a7_0"
description: "shpc-registry automated BioContainers addition for poseidon-trident"
config: {"url": "https://biocontainers.pro/tools/poseidon-trident", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for poseidon-trident", "latest": {"1.5.7.0--hf48d1a7_0": "sha256:3dfd62cb219122a933c8ab8c9b0923699653d9165019f22d141b2b5fad01f5d4"}, "tags": {"0.28.0--h9325052_0": "sha256:3a6f2f51c9322434446b730231f9310ec146579f708287b1e88a97c53de1120f", "1.1.6.0--h9325052_0": "sha256:8286f010e2227d0bcd3440e173e34b07c0c841ebaab0f0fd5fbd0bb73266e62d", "1.1.11.0--h9325052_0": "sha256:0b7450aeb4bfa7ff55621f6c5196cca92d5b527b7f70469291f9c2eb5ecf0ea0", "1.1.11.0--hf48d1a7_2": "sha256:4b8134739174c485a3e31037012fe6a6d4d9a16684c1089e175c2f3091a2560a", "1.2.0.0--hf48d1a7_0": "sha256:6f16c48ddf20972ae397c8604f4ce38abfaef6cf8194583d57b03be4f2c65dea", "1.3.0.4--hf48d1a7_0": "sha256:c15a7190a15cf5836e2b037222d58aca6a63309f339d52fce8579a0e1e928d38", "1.4.1.0--hf48d1a7_0": "sha256:67bda2d5f42e80066169c662e8bede1154a763cbee080ffd2dd9d7182b9c8252", "1.5.0.1--hf48d1a7_0": "sha256:569a1440d53aaf4f0af44989a6dd5910927eef9c981f1d4a9a56fdba5d3fdcd7", "1.5.4.0--hf48d1a7_0": "sha256:fe00d69e76885fbe4abebfc968be0cd886621d51e5b18384eb42c3a15ade0755", "1.5.7.0--hf48d1a7_0": "sha256:3dfd62cb219122a933c8ab8c9b0923699653d9165019f22d141b2b5fad01f5d4"}, "docker": "quay.io/biocontainers/poseidon-trident", "aliases": {"trident": "/usr/local/bin/trident"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/poseidon-trident.
shpc-registry automated BioContainers addition for poseidon-trident
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/poseidon-trident
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/poseidon-trident:1.5.7.0--hf48d1a7_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/poseidon-trident/1.5.7.0--hf48d1a7_0
$ module help quay.io/biocontainers/poseidon-trident/1.5.7.0--hf48d1a7_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### poseidon-trident-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### poseidon-trident-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### poseidon-trident-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### poseidon-trident-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### poseidon-trident-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### poseidon-trident-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trident

```bash
$ singularity exec <container> /usr/local/bin/trident
$ podman run --it --rm --entrypoint /usr/local/bin/trident   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trident   -v ${PWD} -w ${PWD} <container> -c " $@"
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