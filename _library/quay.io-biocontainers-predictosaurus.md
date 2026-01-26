---
layout: container
name:  "quay.io/biocontainers/predictosaurus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/predictosaurus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/predictosaurus/container.yaml"
updated_at: "2026-01-26 04:42:39.443391"
latest: "0.7.4--hcb96839_0"
container_url: "https://biocontainers.pro/tools/predictosaurus"
aliases:
 - "predictosaurus"
versions:
 - "0.2.2--hcb96839_0"
 - "0.2.6--hcb96839_0"
 - "0.2.9--hcb96839_0"
 - "0.2.10--hcb96839_0"
 - "0.3.2--hcb96839_0"
 - "0.4.2--hcb96839_0"
 - "0.6.0--hcb96839_0"
 - "0.5.0--hcb96839_0"
 - "0.7.4--hcb96839_0"
description: "singularity registry hpc automated addition for predictosaurus"
config: {"url": "https://biocontainers.pro/tools/predictosaurus", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for predictosaurus", "latest": {"0.7.4--hcb96839_0": "sha256:8d4e6cb8bdd15068893b5f2981a157433d41cfcfbc9d41d2124999ed16d9ecdf"}, "tags": {"0.2.2--hcb96839_0": "sha256:1d54fbe56d05b18bd3d1738b5a7b6003453fcd728cbcf5c375a4c293a57713f8", "0.2.6--hcb96839_0": "sha256:5b55b9230c15f7522e9cc28cae31174e0017a09f8dd05b5b1a17430e5d321462", "0.2.9--hcb96839_0": "sha256:b7f0dbe4ace67b6641a193141ffcdcba43897b0b7a624b1131f2f06799a973ca", "0.2.10--hcb96839_0": "sha256:e80342be635429d7a5a54f69d028ffcd83fefb31da37485603d03ed76f9e6f65", "0.3.2--hcb96839_0": "sha256:387aba70be685e80e480e25508dcb82e04d026c6b9521c7e2302e3973611f0b3", "0.4.2--hcb96839_0": "sha256:47509b683eff4a319bd63bd8388348465282c46bdb6ca291aee525c4e2d113f5", "0.6.0--hcb96839_0": "sha256:d5d61fda412516e81688e84af8ed100b88c1fbe76783af5b439e306b71134c79", "0.5.0--hcb96839_0": "sha256:b0148243f80c6faa8559220339b00d8ef0225bf59717ddaec96990697bf16441", "0.7.4--hcb96839_0": "sha256:8d4e6cb8bdd15068893b5f2981a157433d41cfcfbc9d41d2124999ed16d9ecdf"}, "docker": "quay.io/biocontainers/predictosaurus", "aliases": {"predictosaurus": "/usr/local/bin/predictosaurus"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/predictosaurus.
singularity registry hpc automated addition for predictosaurus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/predictosaurus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/predictosaurus:0.7.4--hcb96839_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/predictosaurus/0.7.4--hcb96839_0
$ module help quay.io/biocontainers/predictosaurus/0.7.4--hcb96839_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### predictosaurus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### predictosaurus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### predictosaurus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### predictosaurus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### predictosaurus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### predictosaurus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### predictosaurus

```bash
$ singularity exec <container> /usr/local/bin/predictosaurus
$ podman run --it --rm --entrypoint /usr/local/bin/predictosaurus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/predictosaurus   -v ${PWD} -w ${PWD} <container> -c " $@"
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