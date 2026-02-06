---
layout: container
name:  "quay.io/biocontainers/scripps-msms"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scripps-msms/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/scripps-msms/container.yaml"
updated_at: "2026-02-06 05:01:34.999787"
latest: "2.6.1--h9ee0642_0"
container_url: "https://biocontainers.pro/tools/scripps-msms"
aliases:
 - "msms"
 - "pdb_to_xyzr"
 - "pdb_to_xyzrn"
versions:
 - "2.6.1--h9ee0642_0"
description: "singularity registry hpc automated addition for scripps-msms"
config: {"url": "https://biocontainers.pro/tools/scripps-msms", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for scripps-msms", "latest": {"2.6.1--h9ee0642_0": "sha256:5946560ae7b34324f4929c71e598976b36aee7a473ad2a8133ee76fa70421c6f"}, "tags": {"2.6.1--h9ee0642_0": "sha256:5946560ae7b34324f4929c71e598976b36aee7a473ad2a8133ee76fa70421c6f"}, "docker": "quay.io/biocontainers/scripps-msms", "aliases": {"msms": "/usr/local/bin/msms", "pdb_to_xyzr": "/usr/local/bin/pdb_to_xyzr", "pdb_to_xyzrn": "/usr/local/bin/pdb_to_xyzrn"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/scripps-msms.
singularity registry hpc automated addition for scripps-msms
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scripps-msms
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scripps-msms:2.6.1--h9ee0642_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scripps-msms/2.6.1--h9ee0642_0
$ module help quay.io/biocontainers/scripps-msms/2.6.1--h9ee0642_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scripps-msms-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scripps-msms-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scripps-msms-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scripps-msms-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scripps-msms-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scripps-msms-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### msms

```bash
$ singularity exec <container> /usr/local/bin/msms
$ podman run --it --rm --entrypoint /usr/local/bin/msms   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msms   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_to_xyzr

```bash
$ singularity exec <container> /usr/local/bin/pdb_to_xyzr
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdb_to_xyzrn

```bash
$ singularity exec <container> /usr/local/bin/pdb_to_xyzrn
$ podman run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzrn   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdb_to_xyzrn   -v ${PWD} -w ${PWD} <container> -c " $@"
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