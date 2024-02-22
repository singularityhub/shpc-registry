---
layout: container
name:  "quay.io/biocontainers/bioconductor-signaturesearch"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-signaturesearch/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-signaturesearch/container.yaml"
updated_at: "2024-02-22 02:53:59.945834"
latest: "1.16.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-signaturesearch"
aliases:
 - "glpsol"
versions:
 - "1.8.2--r41hc247a5b_1"
 - "1.12.0--r42hc247a5b_0"
 - "1.12.0--r42hf17093f_1"
 - "1.14.0--r43hf17093f_0"
 - "1.16.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-signaturesearch"
config: {"url": "https://biocontainers.pro/tools/bioconductor-signaturesearch", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-signaturesearch", "latest": {"1.16.0--r43hf17093f_0": "sha256:8013546e6c14d4c83cf090521abadc623b7d5bed01f65de5826e2b7e6d8d6fe4"}, "tags": {"1.8.2--r41hc247a5b_1": "sha256:2fef21aac2d2c88704d657c70efdc3e7c3c8b56c2d8764c5e980f8caba4b528e", "1.12.0--r42hc247a5b_0": "sha256:c800242d61959872b6f7f265813e564fa91bbfcd01c8e524b916140f6f21e4cd", "1.12.0--r42hf17093f_1": "sha256:b23d68c1df756463b6523fe4f8636ece7d41251a778a27dd4298c194785716a8", "1.14.0--r43hf17093f_0": "sha256:715f95f6a3098d8ab81b9d996544bd93ebc30ec6a44d3c287102cb35ee315b24", "1.16.0--r43hf17093f_0": "sha256:8013546e6c14d4c83cf090521abadc623b7d5bed01f65de5826e2b7e6d8d6fe4"}, "docker": "quay.io/biocontainers/bioconductor-signaturesearch", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-signaturesearch.
shpc-registry automated BioContainers addition for bioconductor-signaturesearch
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-signaturesearch
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-signaturesearch:1.16.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-signaturesearch/1.16.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-signaturesearch/1.16.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-signaturesearch-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-signaturesearch-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-signaturesearch-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-signaturesearch-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-signaturesearch-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-signaturesearch-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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