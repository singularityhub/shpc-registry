---
layout: container
name:  "quay.io/biocontainers/bioconductor-garfield"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-garfield/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-garfield/container.yaml"
updated_at: "2025-11-20 03:50:24.452458"
latest: "1.34.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-garfield"

versions:
 - "1.22.0--r41hc247a5b_2"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_2"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_1"
 - "1.30.0--r43hf17093f_2"
 - "1.30.0--r43hf17093f_3"
 - "1.34.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-garfield"
config: {"url": "https://biocontainers.pro/tools/bioconductor-garfield", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-garfield", "latest": {"1.34.0--r44he5774e6_0": "sha256:553a5fa65e232cd8fda23976fff71b69c0758ee8d64891f21ba4f7203ff2c748"}, "tags": {"1.22.0--r41hc247a5b_2": "sha256:5ba919c6995637125ddc51ed4b9b17af730f1bc778557e2663611a3ffaed51b4", "1.26.0--r42hc247a5b_0": "sha256:5debbccbc9065d4ea9367300ecbc6e35caedc690e30b8eb699ea2c5e9f9d9dde", "1.26.0--r42hf17093f_2": "sha256:4580122bdbd2bd16a46c06d678f54496c334c6b44c3d73b83dde3f4f40fea26d", "1.28.0--r43hf17093f_0": "sha256:9b76fa5f3348d0d0450b62964f178bf29d7f132ebe5e69b28d936e278de0727f", "1.30.0--r43hf17093f_1": "sha256:f12f1a90a99e395a762f2e7a9450c1618594499d41b3b6ccf2e2ea943458acfa", "1.30.0--r43hf17093f_2": "sha256:2ea529a5d280a80ab4cad2126b2985e49b01763775eb7676fde726fe01b9c51d", "1.30.0--r43hf17093f_3": "sha256:3f0e497bc0243f3685cf112fde41c04ff38b83fe7ed74b7f46edee03416c763c", "1.34.0--r44he5774e6_0": "sha256:553a5fa65e232cd8fda23976fff71b69c0758ee8d64891f21ba4f7203ff2c748"}, "docker": "quay.io/biocontainers/bioconductor-garfield"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-garfield.
shpc-registry automated BioContainers addition for bioconductor-garfield
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-garfield
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-garfield:1.34.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-garfield/1.34.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-garfield/1.34.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-garfield-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-garfield-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-garfield-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-garfield-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-garfield-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-garfield-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-garfield

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