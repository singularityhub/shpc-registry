---
layout: container
name:  "bids/hcppipelines"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/hcppipelines/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/hcppipelines/container.yaml"
updated_at: "2025-01-06 02:56:12.464534"
latest: "v4.3.0-3"
container_url: "https://hub.docker.com/r/bids/hcppipelines"

versions:
 - "latest"
 - "v4.1.3-1"
 - "v4.3.0-2"
 - "v4.3.0-3"
description: "BIDS-ified HPC Piplines to process MRI data for the Human Connectome Project (https://github.com/BIDS-Apps/HCPPipelines)"
config: {"docker": "bids/hcppipelines", "url": "https://hub.docker.com/r/bids/hcppipelines", "maintainer": "@vsoch", "description": "BIDS-ified HPC Piplines to process MRI data for the Human Connectome Project (https://github.com/BIDS-Apps/HCPPipelines)", "latest": {"v4.3.0-3": "sha256:f4c532880bbf65e7fb457b41005e1bd3f6049657371b36a22b6ac44dd59236e2"}, "tags": {"latest": "sha256:f4c532880bbf65e7fb457b41005e1bd3f6049657371b36a22b6ac44dd59236e2", "v4.1.3-1": "sha256:aea536f1dde005bc0e30451a42709d436146e373c2088b10614b5d3a1614b52b", "v4.3.0-2": "sha256:2834881a48f6849b306f59ac604b46016b06c402ed0ed5e0d03ef98964097154", "v4.3.0-3": "sha256:f4c532880bbf65e7fb457b41005e1bd3f6049657371b36a22b6ac44dd59236e2"}, "filter": ["v*"]}
---

This module is a singularity container wrapper for bids/hcppipelines.
BIDS-ified HPC Piplines to process MRI data for the Human Connectome Project (https://github.com/BIDS-Apps/HCPPipelines)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/hcppipelines
```

Or a specific version:

```bash
$ shpc install bids/hcppipelines:v4.3.0-3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/hcppipelines/v4.3.0-3
$ module help bids/hcppipelines/v4.3.0-3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hcppipelines-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hcppipelines-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hcppipelines-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hcppipelines-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hcppipelines-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hcppipelines-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### hcppipelines

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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