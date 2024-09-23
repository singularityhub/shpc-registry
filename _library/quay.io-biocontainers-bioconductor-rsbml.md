---
layout: container
name:  "quay.io/biocontainers/bioconductor-rsbml"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rsbml/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rsbml/container.yaml"
updated_at: "2024-09-23 03:33:19.754090"
latest: "2.60.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rsbml"

versions:
 - "2.52.0--r41hc247a5b_2"
 - "2.56.0--r42hc247a5b_0"
 - "2.56.0--r42hf17093f_1"
 - "2.58.0--r43hf17093f_0"
 - "2.60.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rsbml"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rsbml", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rsbml", "latest": {"2.60.0--r43hf17093f_0": "sha256:51df079c3d8ec4558067544e2684896227604d8e44bf0fcfff9903cdd0164b13"}, "tags": {"2.52.0--r41hc247a5b_2": "sha256:aa1e274e4cf51299daadaf5a57c3a639a920fb970fc342422ca0721aaf24e106", "2.56.0--r42hc247a5b_0": "sha256:7af5b8692c7a78e4da1ad4ef00b5b9c57b273a06f3b6e37ccae03f35fab0e6c6", "2.56.0--r42hf17093f_1": "sha256:14dbafdc4f3be53b2bce1db49c514d3d1d22b17dbdf6e41b5e94084d0f3f0ae8", "2.58.0--r43hf17093f_0": "sha256:adbcfc9e8ddd295123f1cb056ad6e3fd2633c62aad2602621a4b08020c212aae", "2.60.0--r43hf17093f_0": "sha256:51df079c3d8ec4558067544e2684896227604d8e44bf0fcfff9903cdd0164b13"}, "docker": "quay.io/biocontainers/bioconductor-rsbml"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rsbml.
shpc-registry automated BioContainers addition for bioconductor-rsbml
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rsbml
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rsbml:2.60.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rsbml/2.60.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-rsbml/2.60.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rsbml-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsbml-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsbml-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rsbml-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rsbml-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rsbml-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rsbml

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