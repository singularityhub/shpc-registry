---
layout: container
name:  "quay.io/biocontainers/bioconductor-tidybulk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tidybulk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tidybulk/container.yaml"
updated_at: "2025-07-26 04:06:33.139081"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tidybulk"

versions:
 - "1.6.1--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.2--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tidybulk"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tidybulk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tidybulk", "latest": {"1.18.0--r44hdfd78af_0": "sha256:d433fc451d43dbb4cae52d608c23c3dc93212b4c67fa4dcdb15677d28b20cad6"}, "tags": {"1.6.1--r41hdfd78af_0": "sha256:309f25d783e45393b84893712581efa4614a71679e7c4eecc239909bdef6ad9b", "1.10.0--r42hdfd78af_0": "sha256:9985d7ed2dd7cdbb3fb06041e0cbdc15aabd43bdb32b94f2b87561825b1cd39d", "1.12.0--r43hdfd78af_0": "sha256:0fdd08c234b831f952ce3aade3611a2f56029b4ac2036be15f4f2fe6ae66223f", "1.14.2--r43hdfd78af_0": "sha256:a7214683405cd426df92d0c2dd6ea01a2c1d174b6f11d16e8ef7005b64949a2b", "1.18.0--r44hdfd78af_0": "sha256:d433fc451d43dbb4cae52d608c23c3dc93212b4c67fa4dcdb15677d28b20cad6"}, "docker": "quay.io/biocontainers/bioconductor-tidybulk"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tidybulk.
shpc-registry automated BioContainers addition for bioconductor-tidybulk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tidybulk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tidybulk:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tidybulk/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tidybulk/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tidybulk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidybulk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tidybulk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tidybulk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tidybulk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tidybulk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tidybulk

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