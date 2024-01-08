---
layout: container
name:  "quay.io/biocontainers/verifybamid2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/verifybamid2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/verifybamid2/container.yaml"
updated_at: "2024-01-08 03:14:47.230780"
latest: "2.0.1--h81e4b3e_10"
container_url: "https://biocontainers.pro/tools/verifybamid2"
aliases:
 - "verifybamid2"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "2.0.1--h19d48f6_8"
 - "2.0.1--h6a62bbb_9"
 - "2.0.1--h81e4b3e_10"
description: "shpc-registry automated BioContainers addition for verifybamid2"
config: {"url": "https://biocontainers.pro/tools/verifybamid2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for verifybamid2", "latest": {"2.0.1--h81e4b3e_10": "sha256:7f0e71d417ab331e5f2378062b3db5b8a47334e0a8f4d46e7d608dbb488ac6b0"}, "tags": {"2.0.1--h19d48f6_8": "sha256:66df5df3fa382b9891bf9426e6d6ec2783b2c01e1a0df333910d2e518ca38083", "2.0.1--h6a62bbb_9": "sha256:f46ce7c1924dd85decb0447cdbbfdedb1e83e6d93382f850eefa9bb8fd1b43d5", "2.0.1--h81e4b3e_10": "sha256:7f0e71d417ab331e5f2378062b3db5b8a47334e0a8f4d46e7d608dbb488ac6b0"}, "docker": "quay.io/biocontainers/verifybamid2", "aliases": {"verifybamid2": "/usr/local/bin/verifybamid2", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/verifybamid2.
shpc-registry automated BioContainers addition for verifybamid2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/verifybamid2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/verifybamid2:2.0.1--h81e4b3e_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/verifybamid2/2.0.1--h81e4b3e_10
$ module help quay.io/biocontainers/verifybamid2/2.0.1--h81e4b3e_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### verifybamid2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### verifybamid2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### verifybamid2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### verifybamid2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### verifybamid2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### verifybamid2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### verifybamid2

```bash
$ singularity exec <container> /usr/local/bin/verifybamid2
$ podman run --it --rm --entrypoint /usr/local/bin/verifybamid2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/verifybamid2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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