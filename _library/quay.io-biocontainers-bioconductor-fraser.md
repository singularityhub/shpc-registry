---
layout: container
name:  "quay.io/biocontainers/bioconductor-fraser"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fraser/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fraser/container.yaml"
updated_at: "2024-09-09 05:45:27.221639"
latest: "1.99.4--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fraser"

versions:
 - "1.6.1--r41hc247a5b_2"
 - "1.10.0--r42hc247a5b_0"
 - "1.10.0--r42hf17093f_1"
 - "1.12.1--r43hf17093f_0"
 - "1.14.0--r43hf17093f_0"
 - "1.99.4--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fraser"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fraser", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fraser", "latest": {"1.99.4--r43hf17093f_0": "sha256:355493fc464ff74f75dd5ac0b37a1874e5161da766fec960904ffdd0e66b48ba"}, "tags": {"1.6.1--r41hc247a5b_2": "sha256:96a57a428bd816e508ffe1bfeeed028ebb58019aead777fc56354873699abbbb", "1.10.0--r42hc247a5b_0": "sha256:c899a2844efa30b0085897fca3cf8c7cad0d6e109c2cc1f0dcfe84a4e5a948ea", "1.10.0--r42hf17093f_1": "sha256:679c2a8317958e5f1ca440773f4c63daa9e244217d5fc388b470b06569063804", "1.12.1--r43hf17093f_0": "sha256:bb5671e6e4d345b97255867ecc650c2684b62e32c8412621bfc89d479cd8d074", "1.14.0--r43hf17093f_0": "sha256:04c83f797133e381a66c53eb845a8338930c598fbb4c8ff59b2ec7d884448588", "1.99.4--r43hf17093f_0": "sha256:355493fc464ff74f75dd5ac0b37a1874e5161da766fec960904ffdd0e66b48ba"}, "docker": "quay.io/biocontainers/bioconductor-fraser"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fraser.
shpc-registry automated BioContainers addition for bioconductor-fraser
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fraser
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fraser:1.99.4--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fraser/1.99.4--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-fraser/1.99.4--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fraser-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fraser-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fraser-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fraser-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fraser-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fraser-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fraser

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