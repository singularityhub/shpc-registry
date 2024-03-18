---
layout: container
name:  "quay.io/biocontainers/bioconductor-hem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hem/container.yaml"
updated_at: "2024-03-18 03:27:42.141868"
latest: "1.74.0--r43ha9d7317_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hem"

versions:
 - "1.66.0--r41hc0cfd56_2"
 - "1.70.0--r42hc0cfd56_0"
 - "1.70.0--r42ha9d7317_1"
 - "1.72.0--r43ha9d7317_0"
 - "1.74.0--r43ha9d7317_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hem", "latest": {"1.74.0--r43ha9d7317_0": "sha256:998d08ae80c6afad2b5a30c4686e40e70238f61985b6005d0f1ec734f468a9bc"}, "tags": {"1.66.0--r41hc0cfd56_2": "sha256:f343026ca1a51388de57d91a6b7b0f403543773ee85a10c597b66bc2958c37c2", "1.70.0--r42hc0cfd56_0": "sha256:e3814ad5f3a4bf7aefbb354cfd2e2e5c87947a22a48692f193e1a1f7f412c62f", "1.70.0--r42ha9d7317_1": "sha256:9c94d15a865f7d1a7e2e555b444919242c4c271698353b576d249b1725ac05e3", "1.72.0--r43ha9d7317_0": "sha256:c1edf55d8349a690518c50342d58dff5536523976bb89641cbcca5b39fe51b31", "1.74.0--r43ha9d7317_0": "sha256:998d08ae80c6afad2b5a30c4686e40e70238f61985b6005d0f1ec734f468a9bc"}, "docker": "quay.io/biocontainers/bioconductor-hem"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hem.
shpc-registry automated BioContainers addition for bioconductor-hem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hem:1.74.0--r43ha9d7317_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hem/1.74.0--r43ha9d7317_0
$ module help quay.io/biocontainers/bioconductor-hem/1.74.0--r43ha9d7317_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hem

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