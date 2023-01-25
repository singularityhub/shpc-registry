---
layout: container
name:  "quay.io/biocontainers/rust-bio-tools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/rust-bio-tools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/rust-bio-tools/container.yaml"
updated_at: "2023-01-25 03:03:08.318736"
latest: "0.19.5--heda7bfa_0"
container_url: "https://biocontainers.pro/tools/rust-bio-tools"
aliases:
 - "rbt"
 - "starcode"
versions:
 - "0.9.2--h46ad9a4_1"
 - "0.19.5--heda7bfa_0"
 - "0.18.1--heda7bfa_0"
 - "0.17.0--heda7bfa_0"
 - "0.16.0--heda7bfa_0"
 - "0.15.1--heda7bfa_0"
description: "shpc-registry automated BioContainers addition for rust-bio-tools"
config: {"url": "https://biocontainers.pro/tools/rust-bio-tools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for rust-bio-tools", "latest": {"0.19.5--heda7bfa_0": "sha256:c2c4ccce7c0690f9321506856951db945d04e05a641b8afbedf7f330f7546ca7"}, "tags": {"0.9.2--h46ad9a4_1": "sha256:7ab14141f8438fe52f5257e8a2d202fbd58841d129049ab9e2c87c862df601e2", "0.19.5--heda7bfa_0": "sha256:c2c4ccce7c0690f9321506856951db945d04e05a641b8afbedf7f330f7546ca7", "0.18.1--heda7bfa_0": "sha256:4b6c0f2249541c6f214c968139ab5c58fec35f39c6c2528214bbb617e66f4fdc", "0.17.0--heda7bfa_0": "sha256:7c2fd7f9f3e2ea4d007d54335286db897b14abafbf6d39ecd871a3badf100f67", "0.16.0--heda7bfa_0": "sha256:15762d3ffd9f0dd77a157f9fc6191dad0d68cb62ec63afc1a6f060817a0e87fd", "0.15.1--heda7bfa_0": "sha256:9852d1f1c4edc914898409f631911193e44aa7d1bcc9f003f8a922749a5b55b1"}, "docker": "quay.io/biocontainers/rust-bio-tools", "aliases": {"rbt": "/usr/local/bin/rbt", "starcode": "/usr/local/bin/starcode"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/rust-bio-tools.
shpc-registry automated BioContainers addition for rust-bio-tools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/rust-bio-tools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/rust-bio-tools:0.19.5--heda7bfa_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/rust-bio-tools/0.19.5--heda7bfa_0
$ module help quay.io/biocontainers/rust-bio-tools/0.19.5--heda7bfa_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### rust-bio-tools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### rust-bio-tools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### rust-bio-tools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### rust-bio-tools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### rust-bio-tools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### rust-bio-tools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### rbt

```bash
$ singularity exec <container> /usr/local/bin/rbt
$ podman run --it --rm --entrypoint /usr/local/bin/rbt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rbt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### starcode

```bash
$ singularity exec <container> /usr/local/bin/starcode
$ podman run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/starcode   -v ${PWD} -w ${PWD} <container> -c " $@"
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