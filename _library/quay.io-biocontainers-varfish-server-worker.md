---
layout: container
name:  "quay.io/biocontainers/varfish-server-worker"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/varfish-server-worker/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/varfish-server-worker/container.yaml"
updated_at: "2024-07-25 03:13:10.045440"
latest: "0.12.0--hb3cd794_0"
container_url: "https://biocontainers.pro/tools/varfish-server-worker"
aliases:
 - "varfish-server-worker"
versions:
 - "0.4.0--h87f3376_0"
 - "0.5.0--h87f3376_0"
 - "0.5.1--h87f3376_0"
 - "0.6.1--h87f3376_1"
 - "0.6.1--hdbdd923_2"
 - "0.9.0--hb3cd794_0"
 - "0.8.0--hb3cd794_0"
 - "0.7.0--hb3cd794_0"
 - "0.10.1--hb3cd794_0"
 - "0.10.2--hb3cd794_0"
 - "0.11.0--hb3cd794_0"
 - "0.10.2--hb3cd794_1"
 - "0.12.0--hb3cd794_0"
description: "singularity registry hpc automated addition for varfish-server-worker"
config: {"url": "https://biocontainers.pro/tools/varfish-server-worker", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for varfish-server-worker", "latest": {"0.12.0--hb3cd794_0": "sha256:b57e58188a3bd1f8409b8ea15be47869d8e548724d0eca25c3b3f54c71910dfa"}, "tags": {"0.4.0--h87f3376_0": "sha256:d98a6cc167a7a7096c1322483495f5cecfa45c5dcd864f196f58bf0957072c27", "0.5.0--h87f3376_0": "sha256:83c0c620d078b7ebc146abb6aaa269b24e2dd50622633aa7ecdee120b9d205a3", "0.5.1--h87f3376_0": "sha256:85c7fe4b0c83b2d709903f8ef83982005fc9a28f14fb997e3a64acd2059e6282", "0.6.1--h87f3376_1": "sha256:f851e757827445fb65e3d7196fb98a685ef625031a2d3b716331a1df1328dbf5", "0.6.1--hdbdd923_2": "sha256:d02a6b7b161ebec0707e6df43342656bb365b77427e636f39039d3bc4ae739e0", "0.9.0--hb3cd794_0": "sha256:afa7321022f4daeaa112a891c24ad46188b10745bd563733a7edd8c8a09619f4", "0.8.0--hb3cd794_0": "sha256:7170d253687206302418015d9b1d4334d16508dc034e8c1dfa0d64b62066cfae", "0.7.0--hb3cd794_0": "sha256:9ef839887f3cadf4d7dbad02814201301da5e5d4a7928320b856859dc496ff09", "0.10.1--hb3cd794_0": "sha256:0f28a0747b1693c35a87f647613e18f85be521794d9c41304f00b0dc113842c5", "0.10.2--hb3cd794_0": "sha256:236733e299cdd03945f9bc8f232698b40273ede87cf0bbd38338b94da6ee79be", "0.11.0--hb3cd794_0": "sha256:fae1cf19279473bfeedda1429de2bddb355e7742b5c87a327db940debd2cc033", "0.10.2--hb3cd794_1": "sha256:c641515104936c4051ff154b6f17b3c159898e9519451402305962c4ddce9256", "0.12.0--hb3cd794_0": "sha256:b57e58188a3bd1f8409b8ea15be47869d8e548724d0eca25c3b3f54c71910dfa"}, "docker": "quay.io/biocontainers/varfish-server-worker", "aliases": {"varfish-server-worker": "/usr/local/bin/varfish-server-worker"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/varfish-server-worker.
singularity registry hpc automated addition for varfish-server-worker
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/varfish-server-worker
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/varfish-server-worker:0.12.0--hb3cd794_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/varfish-server-worker/0.12.0--hb3cd794_0
$ module help quay.io/biocontainers/varfish-server-worker/0.12.0--hb3cd794_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### varfish-server-worker-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### varfish-server-worker-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### varfish-server-worker-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### varfish-server-worker-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### varfish-server-worker-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### varfish-server-worker-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### varfish-server-worker

```bash
$ singularity exec <container> /usr/local/bin/varfish-server-worker
$ podman run --it --rm --entrypoint /usr/local/bin/varfish-server-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/varfish-server-worker   -v ${PWD} -w ${PWD} <container> -c " $@"
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