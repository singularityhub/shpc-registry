---
layout: container
name:  "bids/brainiak-srm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/brainiak-srm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/brainiak-srm/container.yaml"
updated_at: "2023-10-31 02:24:19.344520"
latest: "unstable"
container_url: "https://hub.docker.com/r/bids/brainiak-srm"

versions:
 - "latest"
 - "unstable"
description: "Shared Response Model (SRM) from the Brain Imaging Analysis Kit (BrainIAK) (https://github.com/BIDS-Apps/brainiak-srm)"
config: {"docker": "bids/brainiak-srm", "latest": {"unstable": "sha256:d646b5f6e249c26fbbbbf1ac88290f0736e34fa4312294183a2590d7afe894a7"}, "tags": {"latest": "sha256:5ff856420a178be4e8150e574251a44885451050e9803515269e5ff15cd67430", "unstable": "sha256:d646b5f6e249c26fbbbbf1ac88290f0736e34fa4312294183a2590d7afe894a7"}, "filter": ["v*"], "maintainer": "@vsoch", "description": "Shared Response Model (SRM) from the Brain Imaging Analysis Kit (BrainIAK) (https://github.com/BIDS-Apps/brainiak-srm)", "url": "https://hub.docker.com/r/bids/brainiak-srm"}
---

This module is a singularity container wrapper for bids/brainiak-srm.
Shared Response Model (SRM) from the Brain Imaging Analysis Kit (BrainIAK) (https://github.com/BIDS-Apps/brainiak-srm)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/brainiak-srm
```

Or a specific version:

```bash
$ shpc install bids/brainiak-srm:unstable
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/brainiak-srm/unstable
$ module help bids/brainiak-srm/unstable
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### brainiak-srm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### brainiak-srm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### brainiak-srm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### brainiak-srm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### brainiak-srm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### brainiak-srm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### brainiak-srm

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