---
layout: container
name:  "quay.io/biocontainers/seqhax"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/seqhax/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/seqhax/container.yaml"
updated_at: "2025-03-04 03:17:58.357550"
latest: "0.8.6--h43eeafb_1"
container_url: "https://biocontainers.pro/tools/seqhax"
aliases:
 - "pecheck-wrapper.py"
 - "seqhax"
versions:
 - "0.7.2--h5b5514e_3"
 - "0.7.2--h43eeafb_5"
 - "0.8.6--h6ab5fc9_0"
 - "0.8.6--h43eeafb_1"
description: "shpc-registry automated BioContainers addition for seqhax"
config: {"url": "https://biocontainers.pro/tools/seqhax", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for seqhax", "latest": {"0.8.6--h43eeafb_1": "sha256:7f5a67b939ea04db4b26661c8f877ccce6425130dbf9850aab19a5e7b02bfb01"}, "tags": {"0.7.2--h5b5514e_3": "sha256:9ff07f67ae32efe67dbdcfc5db9960f971f491372648dacabf1d5c703cb07f51", "0.7.2--h43eeafb_5": "sha256:d9e7807c273f509194dfa59c51aff9e03aea1875e5f47598e49acf0c51f80ebb", "0.8.6--h6ab5fc9_0": "sha256:6ef645eefa76dcdda425402b0bd4715b32dd9c7fabd51f2efa20b641287b44ac", "0.8.6--h43eeafb_1": "sha256:7f5a67b939ea04db4b26661c8f877ccce6425130dbf9850aab19a5e7b02bfb01"}, "docker": "quay.io/biocontainers/seqhax", "aliases": {"pecheck-wrapper.py": "/usr/local/bin/pecheck-wrapper.py", "seqhax": "/usr/local/bin/seqhax"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/seqhax.
shpc-registry automated BioContainers addition for seqhax
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/seqhax
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/seqhax:0.8.6--h43eeafb_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/seqhax/0.8.6--h43eeafb_1
$ module help quay.io/biocontainers/seqhax/0.8.6--h43eeafb_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### seqhax-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### seqhax-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### seqhax-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### seqhax-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### seqhax-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### seqhax-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pecheck-wrapper.py

```bash
$ singularity exec <container> /usr/local/bin/pecheck-wrapper.py
$ podman run --it --rm --entrypoint /usr/local/bin/pecheck-wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pecheck-wrapper.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqhax

```bash
$ singularity exec <container> /usr/local/bin/seqhax
$ podman run --it --rm --entrypoint /usr/local/bin/seqhax   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqhax   -v ${PWD} -w ${PWD} <container> -c " $@"
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