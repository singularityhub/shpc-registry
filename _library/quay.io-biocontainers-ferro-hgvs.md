---
layout: container
name:  "quay.io/biocontainers/ferro-hgvs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ferro-hgvs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ferro-hgvs/container.yaml"
updated_at: "2026-06-09 08:57:46.760294"
latest: "0.6.0--h1f77f1e_0"
container_url: "https://biocontainers.pro/tools/ferro-hgvs"
aliases:
 - "ferro"
 - "ferro-benchmark"
versions:
 - "0.1.0--h521612f_0"
 - "0.4.0--h1f77f1e_0"
 - "0.3.0--h521612f_0"
 - "0.6.0--h1f77f1e_0"
 - "0.5.0--h1f77f1e_0"
 - "0.4.1--h1f77f1e_0"
description: "singularity registry hpc automated addition for ferro-hgvs"
config: {"url": "https://biocontainers.pro/tools/ferro-hgvs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ferro-hgvs", "latest": {"0.6.0--h1f77f1e_0": "sha256:c3a5746b56c08f5b9978025e005938e8976cba6d7118bf99e7e0f8f563e10b6a"}, "tags": {"0.1.0--h521612f_0": "sha256:1d94d0a5714b06d99a43240166b13a3cdea6b70322492125f7c411be5959b76d", "0.4.0--h1f77f1e_0": "sha256:769eb8e90d50732ccd1f9f85bb9a8eb27abfa3ff2f5825b40d0095b8a4feb90a", "0.3.0--h521612f_0": "sha256:56ab0e53401916f2d1b287cb273f84f6b77e6e81e2b4998dd0bbfa1aa5bd8837", "0.6.0--h1f77f1e_0": "sha256:c3a5746b56c08f5b9978025e005938e8976cba6d7118bf99e7e0f8f563e10b6a", "0.5.0--h1f77f1e_0": "sha256:c87ded17a0f98476afc0196b94ff1955092b376931b4dc72b4e54583c7a02e51", "0.4.1--h1f77f1e_0": "sha256:fe97d48876f38b9b7c7a1115c9dbe6adbca591ba3351e7b8fbd7fdacf9ca1487"}, "docker": "quay.io/biocontainers/ferro-hgvs", "aliases": {"ferro": "/usr/local/bin/ferro", "ferro-benchmark": "/usr/local/bin/ferro-benchmark"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ferro-hgvs.
singularity registry hpc automated addition for ferro-hgvs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ferro-hgvs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ferro-hgvs:0.6.0--h1f77f1e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ferro-hgvs/0.6.0--h1f77f1e_0
$ module help quay.io/biocontainers/ferro-hgvs/0.6.0--h1f77f1e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ferro-hgvs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ferro-hgvs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ferro-hgvs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ferro-hgvs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ferro-hgvs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ferro-hgvs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ferro

```bash
$ singularity exec <container> /usr/local/bin/ferro
$ podman run --it --rm --entrypoint /usr/local/bin/ferro   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ferro   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ferro-benchmark

```bash
$ singularity exec <container> /usr/local/bin/ferro-benchmark
$ podman run --it --rm --entrypoint /usr/local/bin/ferro-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ferro-benchmark   -v ${PWD} -w ${PWD} <container> -c " $@"
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