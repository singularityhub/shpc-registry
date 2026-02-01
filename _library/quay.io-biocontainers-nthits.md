---
layout: container
name:  "quay.io/biocontainers/nthits"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nthits/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nthits/container.yaml"
updated_at: "2026-02-01 05:05:58.195425"
latest: "1.0.3--h9948957_2"
container_url: "https://biocontainers.pro/tools/nthits"
aliases:
 - "nthits"
versions:
 - "0.0.1--h9f5acd7_2"
 - "1.0.1--h9f5acd7_0"
 - "1.0.1--h4ac6f70_1"
 - "1.0.2--h4ac6f70_0"
 - "1.0.3--h4ac6f70_0"
 - "1.0.3--h4ac6f70_1"
 - "1.0.3--h9948957_2"
description: "shpc-registry automated BioContainers addition for nthits"
config: {"url": "https://biocontainers.pro/tools/nthits", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nthits", "latest": {"1.0.3--h9948957_2": "sha256:1a213f9027b30437193d246c59087c7aa1ba1b585a25858fa14ca3b53e8ad7e2"}, "tags": {"0.0.1--h9f5acd7_2": "sha256:9667ed7a20486f393f6ea6b78f77d70a26414769ccad4a5910b1981be0107cd2", "1.0.1--h9f5acd7_0": "sha256:f0b8562f8a3546ad91f3ab89620ace3cf85bf2197cca2164a37bd2341e886189", "1.0.1--h4ac6f70_1": "sha256:339c93321fc09996c023c74d3d0623bc2eeba8fbd85fed8c0b863cfa9b0dbe13", "1.0.2--h4ac6f70_0": "sha256:6ac444bf37cc3f06e3f121863ebabbd747e55b5452a9aed97565325b409b1839", "1.0.3--h4ac6f70_0": "sha256:2426ab94a824c4559ccf9f2e55c755690537c64b73bb983eae33a61b14428f3c", "1.0.3--h4ac6f70_1": "sha256:ce89c745a347f2a638dc47d9a4d5c8aa933d2779108738a8ef6ad2e9847489ac", "1.0.3--h9948957_2": "sha256:1a213f9027b30437193d246c59087c7aa1ba1b585a25858fa14ca3b53e8ad7e2"}, "docker": "quay.io/biocontainers/nthits", "aliases": {"nthits": "/usr/local/bin/nthits"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nthits.
shpc-registry automated BioContainers addition for nthits
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nthits
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nthits:1.0.3--h9948957_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nthits/1.0.3--h9948957_2
$ module help quay.io/biocontainers/nthits/1.0.3--h9948957_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nthits-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nthits-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nthits-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nthits-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nthits-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nthits-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nthits

```bash
$ singularity exec <container> /usr/local/bin/nthits
$ podman run --it --rm --entrypoint /usr/local/bin/nthits   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nthits   -v ${PWD} -w ${PWD} <container> -c " $@"
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