---
layout: container
name:  "quay.io/biocontainers/seqkit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqkit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqkit/container.yaml"
updated_at: "2024-07-08 03:21:21.331591"
latest: "2.8.2--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/seqkit"
aliases:
 - "seqkit"
versions:
 - "2.3.1--h9ee0642_0"
 - "2.4.0--h9ee0642_0"
 - "2.5.0--h9ee0642_0"
 - "2.5.1--h9ee0642_0"
 - "2.6.1--h9ee0642_0"
 - "2.7.0--h9ee0642_0"
 - "2.8.0--h9ee0642_1"
 - "2.8.1--h9ee0642_0"
 - "2.8.2--h9ee0642_0"
description: "shpc-registry automated BioContainers addition for seqkit"
config: {"url": "https://biocontainers.pro/tools/seqkit", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqkit", "latest": {"2.8.2--h9ee0642_0": "sha256:a087c482d265d4209f2e2bd8f44550b0c79616c24f0f64d1f0f08d354bccd101"}, "tags": {"2.3.1--h9ee0642_0": "sha256:2f3cb2be9909165a153e9b9bef2956d1d7ef7ee4c6f08984ff07f7562c3d7327", "2.4.0--h9ee0642_0": "sha256:515f803edad2f7fafd94daa78251218d094a03f1eb55ebac483c3e040e032f36", "2.5.0--h9ee0642_0": "sha256:0e2d27de945005e56ab9962c4ac03a2de362708efd88fce12284652896193823", "2.5.1--h9ee0642_0": "sha256:19909297560a4e91a72bca1c2ee26c16b45a2a12e211b6f1434098c419ec840f", "2.6.1--h9ee0642_0": "sha256:67c9a1cfeafbccfd43bbd1fbb80646c9faa06a50b22c8ea758c3c84268b6765d", "2.7.0--h9ee0642_0": "sha256:659261ee78d23252b24803197166331f7c1cf2364f8f8edd04fa10c8fba8ac20", "2.8.0--h9ee0642_1": "sha256:cd5ef90c40687084d85f7e1ae2e5e6786a0fd5300c607693491050ee1c7538e7", "2.8.1--h9ee0642_0": "sha256:750aa755b224c3e887f1a58e587d4d8ff19308208850939ff4b2e3a329f51795", "2.8.2--h9ee0642_0": "sha256:a087c482d265d4209f2e2bd8f44550b0c79616c24f0f64d1f0f08d354bccd101"}, "docker": "quay.io/biocontainers/seqkit", "aliases": {"seqkit": "/usr/local/bin/seqkit"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqkit.
shpc-registry automated BioContainers addition for seqkit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqkit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqkit:2.8.2--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqkit/2.8.2--h9ee0642_0
$ module help quay.io/biocontainers/seqkit/2.8.2--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqkit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqkit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqkit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqkit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqkit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqkit-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### seqkit

```bash
$ singularity exec <container> /usr/local/bin/seqkit
$ podman run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqkit   -v ${PWD} -w ${PWD} <container> -c " $@"
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