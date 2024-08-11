---
layout: container
name:  "quay.io/biocontainers/bioconductor-diffbind"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-diffbind/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-diffbind/container.yaml"
updated_at: "2024-08-11 03:16:37.382913"
latest: "3.12.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-diffbind"

versions:
 - "3.4.11--r41hc247a5b_1"
 - "3.8.0--r42hc247a5b_0"
 - "3.10.0--r43hf17093f_0"
 - "3.12.0--r43hf17093f_0"
 - "3.12.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-diffbind"
config: {"url": "https://biocontainers.pro/tools/bioconductor-diffbind", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-diffbind", "latest": {"3.12.0--r43hf17093f_1": "sha256:9c65c7f18a9a3a26e7ef906f13413a9f9d758a8769b44fed8439c70e84618ee7"}, "tags": {"3.4.11--r41hc247a5b_1": "sha256:6c4dc11db8dbe34f4bd342b1f711548c25546414b82adfac52a2e7b7d498062b", "3.8.0--r42hc247a5b_0": "sha256:a69772d79a39a3b3328524f4b81112582a8a96059941ad1a736a465e24b5953c", "3.10.0--r43hf17093f_0": "sha256:974ae104d1f06120334bf2b51db181b2d758ff7cf6d3f1cab83d82bc5328f446", "3.12.0--r43hf17093f_0": "sha256:0420d7fbc00cf2e7933bbde2de43863b73549f344365ab097b48380d0330a65b", "3.12.0--r43hf17093f_1": "sha256:9c65c7f18a9a3a26e7ef906f13413a9f9d758a8769b44fed8439c70e84618ee7"}, "docker": "quay.io/biocontainers/bioconductor-diffbind"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-diffbind.
shpc-registry automated BioContainers addition for bioconductor-diffbind
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-diffbind
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-diffbind:3.12.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-diffbind/3.12.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-diffbind/3.12.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-diffbind-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffbind-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-diffbind-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-diffbind-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-diffbind-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-diffbind-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-diffbind

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