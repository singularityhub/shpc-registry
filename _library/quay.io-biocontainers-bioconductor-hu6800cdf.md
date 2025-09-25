---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu6800cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu6800cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu6800cdf/container.yaml"
updated_at: "2025-09-25 03:07:38.593013"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-hu6800cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-hu6800cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu6800cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu6800cdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:963f99f12a81a0c1329a8239d7f5b1522041b957288e9840198309a87bf14df9"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:92deda7eef304eea5501e23cc5e89976e96a3764d107a3057644008747e319b5", "2.18.0--r42hdfd78af_10": "sha256:9a86b7f0b730937e34985617c05dc081a9a505523715356ba1700c6d51cbb5b0", "2.18.0--r43hdfd78af_11": "sha256:3a1e6ea1d01498e7699cbfc64cf6378125901ac34a7d730ca22dcbafb6321580", "2.18.0--r43hdfd78af_12": "sha256:d78f33c51f24dc73bec3f2fcff96037b8fb5a4e43c1bdc1748ae1e3837b14757", "2.18.0--r44hdfd78af_13": "sha256:963f99f12a81a0c1329a8239d7f5b1522041b957288e9840198309a87bf14df9"}, "docker": "quay.io/biocontainers/bioconductor-hu6800cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu6800cdf.
shpc-registry automated BioContainers addition for bioconductor-hu6800cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800cdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu6800cdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-hu6800cdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu6800cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu6800cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu6800cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu6800cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu6800cdf

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