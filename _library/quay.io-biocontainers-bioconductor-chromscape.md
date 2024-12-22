---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromscape"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromscape/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromscape/container.yaml"
updated_at: "2024-12-22 03:15:44.663401"
latest: "1.12.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromscape"
aliases:
 - "pandoc-server"
 - "glpsol"
 - "pandoc"
versions:
 - "1.4.0--r41hc247a5b_2"
 - "1.8.0--r42hc247a5b_0"
 - "1.8.0--r42hf17093f_1"
 - "1.10.0--r43hf17093f_0"
 - "1.12.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromscape"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromscape", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromscape", "latest": {"1.12.0--r43hf17093f_0": "sha256:512d07c26bbe320b07dcd4183fc64c0f334b765feaf0890da76790132ec02e87"}, "tags": {"1.4.0--r41hc247a5b_2": "sha256:4dae9f97dfb806e221126735c10e9b996922615194df9cf0846434a57b5c8ecc", "1.8.0--r42hc247a5b_0": "sha256:130c607c31cde9c515d9788fb863aa7c02221c78a56a9d7babfcb771dfdd3c32", "1.8.0--r42hf17093f_1": "sha256:bda182c80bde85d9e93361b8c565ad6d24b8a407d4db8aca3e2679db0ab716c0", "1.10.0--r43hf17093f_0": "sha256:88385c3736f66e785f391f8eb3c5a65bb11963f7a454f49f9071f47db58b1158", "1.12.0--r43hf17093f_0": "sha256:512d07c26bbe320b07dcd4183fc64c0f334b765feaf0890da76790132ec02e87"}, "docker": "quay.io/biocontainers/bioconductor-chromscape", "aliases": {"pandoc-server": "/usr/local/bin/pandoc-server", "glpsol": "/usr/local/bin/glpsol", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromscape.
shpc-registry automated BioContainers addition for bioconductor-chromscape
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromscape
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromscape:1.12.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromscape/1.12.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-chromscape/1.12.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromscape-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromscape-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromscape-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromscape-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromscape-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromscape-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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