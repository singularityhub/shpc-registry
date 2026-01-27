---
layout: container
name:  "quay.io/biocontainers/bioconductor-stringdb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-stringdb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-stringdb/container.yaml"
updated_at: "2026-01-27 04:45:16.428760"
latest: "2.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-stringdb"

versions:
 - "2.6.0--r41hdfd78af_0"
 - "2.10.0--r42hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
 - "2.14.0--r43hdfd78af_0"
 - "2.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-stringdb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-stringdb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-stringdb", "latest": {"2.18.0--r44hdfd78af_0": "sha256:8a14a0a3a44b4190b98e9cbdb1155ff39cba9a74912dff359b8155b9a569d30f"}, "tags": {"2.6.0--r41hdfd78af_0": "sha256:a76f257aa8c88cb54a57f72062f812a3fd0d5ad1bd3c727c3650e4b9a85f0cc5", "2.10.0--r42hdfd78af_0": "sha256:aff2254bc480fa947e6499a64fb8e5fc9281b643ca799da33773cf6c2db71c9c", "2.12.0--r43hdfd78af_0": "sha256:f45eaa471ace229b110168d780b0af0da2065b8bef8162b9bee44ba96f1d4641", "2.14.0--r43hdfd78af_0": "sha256:e25854fdfffe95a186abcb44e6ed40f2fe15118bb4b97cd5d07ea97db36e2867", "2.18.0--r44hdfd78af_0": "sha256:8a14a0a3a44b4190b98e9cbdb1155ff39cba9a74912dff359b8155b9a569d30f"}, "docker": "quay.io/biocontainers/bioconductor-stringdb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-stringdb.
shpc-registry automated BioContainers addition for bioconductor-stringdb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-stringdb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-stringdb:2.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-stringdb/2.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-stringdb/2.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-stringdb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stringdb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-stringdb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-stringdb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-stringdb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-stringdb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-stringdb

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