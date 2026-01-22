---
layout: container
name:  "quay.io/biocontainers/r-mixkernel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-mixkernel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-mixkernel/container.yaml"
updated_at: "2026-01-22 04:21:54.450405"
latest: "0.9--r43h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-mixkernel"

versions:
 - "0.8--r41h3342da4_0"
 - "0.8--r42h3342da4_1"
 - "0.8--r43h3342da4_2"
 - "0.9--r43h3342da4_0"
description: "shpc-registry automated BioContainers addition for r-mixkernel"
config: {"url": "https://biocontainers.pro/tools/r-mixkernel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-mixkernel", "latest": {"0.9--r43h3342da4_0": "sha256:8868be61506b184f990f40f750bfd4c053b1dcb51ba7f61412e87fe96cfbf038"}, "tags": {"0.8--r41h3342da4_0": "sha256:1dcba1c67234799697602fc257841fef00f57041cc55fcc845bd3977d31009e4", "0.8--r42h3342da4_1": "sha256:225dce09dd46b47123e8bb972740bb85366baef811d8cb047e3148d1ba76968f", "0.8--r43h3342da4_2": "sha256:0e47a698d84ff6c6c09350a67da6b25dd3bc8abe65fe01dcafa3e74903231dec", "0.9--r43h3342da4_0": "sha256:8868be61506b184f990f40f750bfd4c053b1dcb51ba7f61412e87fe96cfbf038"}, "docker": "quay.io/biocontainers/r-mixkernel"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-mixkernel.
shpc-registry automated BioContainers addition for r-mixkernel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-mixkernel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-mixkernel:0.9--r43h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-mixkernel/0.9--r43h3342da4_0
$ module help quay.io/biocontainers/r-mixkernel/0.9--r43h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-mixkernel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-mixkernel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-mixkernel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-mixkernel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-mixkernel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-mixkernel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-mixkernel

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